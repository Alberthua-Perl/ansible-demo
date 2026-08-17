#!/usr/bin/env python3
"""
Prometheus 监控示例应用
使用 prometheus_client SDK 暴露自定义业务指标
"""

import time                         # 导入 time 模块，用于时间测量和延迟模拟
import random                       # 导入 random 模块，用于生成随机数和模拟概率事件
import threading                    # 导入 threading 模块，用于创建后台守护线程
from flask import Flask, jsonify    # 从 Flask 框架导入应用类和 JSON 响应工具
from prometheus_client import (     # 从 prometheus_client 导入指标类型和工具函数
    Counter, Histogram, Gauge, generate_latest,    # Counter：只增不减的计数器；Histogram：直方图，统计分布；Gauge：仪表盘，记录瞬时值；generate_latest：生成 Prometheus 文本格式指标
    CONTENT_TYPE_LATEST, CollectorRegistry         # CONTENT_TYPE_LATEST：Prometheus 指标对应的 MIME 类型；CollectorRegistry：自定义指标注册表
)   # 结束 prometheus_client 的导入语句

app = Flask(__name__)             # 创建 Flask 应用实例，__name__ 用于定位模板和静态文件路径
registry = CollectorRegistry()    # 创建独立的指标收集注册表，将自定义指标与默认进程指标隔离

# ==================== 业务指标定义 ====================
http_requests_total = Counter(                             # 定义 Counter 类型指标：统计 HTTP 请求总次数（按方法、端点、状态码分维度）
    'http_requests_total', 'Total HTTP requests',          # 指标名称：http_requests_total；帮助文本：Total HTTP requests
    ['method', 'endpoint', 'status'], registry=registry    # 标签维度：method（HTTP 方法）、endpoint（请求路径）、status（响应状态码）；注册到自定义注册表
)    # 结束 Counter 指标定义

http_request_duration_seconds = Histogram(                                      # 定义 Histogram 类型指标：统计 HTTP 请求耗时分布（按方法、端点分维度）
    'http_request_duration_seconds', 'HTTP request duration in seconds',        # 指标名称和帮助文本，描述 HTTP 请求持续时间（单位：秒）
    ['method', 'endpoint'],                                                     # 标签维度：method、endpoint（不含 status，因为耗时通常按端点聚合）
    buckets=[0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0],    # 定义直方图分桶边界（单位：秒），覆盖从 5ms 到 10s 的典型 Web 请求耗时范围
    registry=registry                                                           # 将该 Histogram 注册到自定义注册表
)    # 结束 Histogram 指标定义

app_active_connections = Gauge(                                                    # 定义 Gauge 类型指标：当前活跃连接数（可增可减的瞬时量，反映实时状态）
    'app_active_connections', 'Number of active connections', registry=registry    # 指标名称、帮助文本，并注册到自定义注册表
)    # 结束 Gauge 定义

app_errors_total = Counter(                            # 定义 Counter 类型指标：统计应用错误总次数（按错误类型分维度）
    'app_errors_total', 'Total application errors',    # 指标名称和帮助文本
    ['error_type'], registry=registry                  # 标签维度：error_type（如 database_timeout、manual_trigger）；注册到自定义注册表
)    # 结束 Counter 定义

app_cpu_usage_percent = Gauge(                                                               # 定义 Gauge 类型指标：模拟应用 CPU 使用率百分比
    'app_cpu_usage_percent', 'Simulated application CPU usage percent', registry=registry    # 指标名称、帮助文本，并注册到自定义注册表
)    # 结束 Gauge 定义

app_memory_usage_bytes = Gauge(                                                                   # 定义 Gauge 类型指标：模拟应用内存使用量（单位：字节）
    'app_memory_usage_bytes', 'Simulated application memory usage in bytes', registry=registry    # 指标名称、帮助文本，并注册到自定义注册表
)    # 结束 Gauge 定义

app_queue_depth = Gauge(                                           # 定义 Gauge 类型指标：当前队列深度/积压任务数
    'app_queue_depth', 'Current queue depth', registry=registry    # 指标名称、帮助文本，并注册到自定义注册表
)    # 结束 Gauge 定义

db_query_duration_seconds = Histogram(                                    # 定义 Histogram 类型指标：统计数据库查询耗时分布
    'db_query_duration_seconds', 'Database query duration in seconds',    # 指标名称和帮助文本
    buckets=[0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0],       # 定义更细粒度的分桶边界（1ms ~ 1s），适应数据库查询通常较快的特点
    registry=registry                                                     # 注册到自定义注册表
)    # 结束 Histogram 定义

# ==================== 模拟后台任务 ====================
def background_metrics_simulator():  # 定义后台指标模拟器函数，持续生成模拟的系统指标数据
    while True:  # 无限循环，持续更新模拟指标（守护线程中运行，不会阻塞主线程）
        cpu = random.gauss(45, 20)  # 生成服从正态分布的 CPU 使用率：均值 45%，标准差 20%
        if random.random() < 0.05:  # 5% 概率触发高 CPU 场景（模拟系统负载峰值或突发任务）
            cpu = random.uniform(85, 98)  # 高负载时 CPU 使用率随机落在 85%~98% 之间
        app_cpu_usage_percent.set(max(0, min(100, cpu)))  # 将 CPU 指标值限制在 0~100 范围内并更新到 Gauge（clamp 操作防止越界）

        mem_mb = random.gauss(512, 150)  # 生成服从正态分布的内存使用量（MB）：均值 512MB，标准差 150MB
        if random.random() < 0.03:  # 3% 概率触发内存激增场景（模拟内存泄漏或大数据处理）
            mem_mb = random.uniform(1800, 2200)  # 内存激增时随机分配 1800MB~2200MB
        app_memory_usage_bytes.set(max(100, mem_mb * 1024 * 1024))  # 将内存值转换为字节（MB × 1024²）并更新 Gauge，确保最小值为 100 字节

        queue = random.gauss(10, 5)  # 生成队列深度的正态分布值：均值 10，标准差 5
        if random.random() < 0.02:  # 2% 概率触发队列堆积场景（模拟消费端处理能力不足）
            queue = random.uniform(80, 120)  # 队列堆积时深度随机落在 80~120 之间
        app_queue_depth.set(max(0, queue))  # 更新队列深度 Gauge，max(0, queue) 确保队列深度不为负数

        app_active_connections.set(random.randint(5, 50))  # 随机生成 5~50 之间的活跃连接数并更新 Gauge
        time.sleep(5)  # 每 5 秒执行一次指标更新，控制模拟频率

simulator_thread = threading.Thread(target=background_metrics_simulator, daemon=True)  # 创建后台守护线程运行指标模拟器，daemon=True 表示主进程退出时自动结束该线程
simulator_thread.start()  # 启动后台指标模拟线程，开始持续生成模拟数据

# ==================== HTTP 路由 ====================
@app.route('/')  # 注册根路径路由（/），通常作为服务健康入口或首页
def index():  # 首页路由处理函数
    start = time.time()  # 记录请求开始时间戳，用于后续计算请求处理耗时
    http_requests_total.labels(method='GET', endpoint='/', status='200').inc()  # 将本次 GET / 请求计入 Counter，状态码 200（请求到达时先计数）
    delay = random.gauss(0.02, 0.01)  # 生成首页响应延迟，服从正态分布：均值 20ms，标准差 10ms
    if random.random() < 0.1:  # 10% 概率模拟慢响应场景（如后端依赖延迟、GC 停顿等）
        delay = random.uniform(0.6, 1.2)  # 慢响应时延迟随机落在 600ms~1200ms
    time.sleep(delay)  # 模拟请求处理耗时（time.sleep 阻塞当前线程）
    http_request_duration_seconds.labels(method='GET', endpoint='/').observe(time.time() - start)  # 将本次请求的实际耗时（当前时间 - 开始时间）记录到 Histogram 中
    return jsonify({"status": "ok", "service": "prometheus-demo-app"})  # 返回 JSON 格式的响应，包含状态 ok 和服务名称标识

@app.route('/api/data')  # 注册数据查询 API 路由（/api/data），模拟数据库查询场景
def api_data():  # 数据查询接口处理函数
    start = time.time()  # 记录整个请求的开始时间
    db_start = time.time()  # 记录数据库查询的开始时间，用于单独统计 DB 耗时
    db_delay = random.gauss(0.05, 0.02)  # 生成数据库查询延迟，服从正态分布：均值 50ms，标准差 20ms
    if random.random() < 0.08:  # 8% 概率模拟数据库慢查询（如索引缺失、锁竞争、网络抖动）
        db_delay = random.uniform(0.8, 2.0)  # 慢查询时延迟随机落在 800ms~2000ms
    time.sleep(db_delay)  # 模拟数据库查询执行耗时
    db_query_duration_seconds.observe(time.time() - db_start)  # 将数据库查询的实际耗时记录到 db_query_duration_seconds Histogram
    
    if random.random() < 0.05:  # 5% 概率模拟数据库超时错误（如连接池耗尽、查询超时）
        app_errors_total.labels(error_type='database_timeout').inc()  # 数据库超时错误计数器 +1，标签为 database_timeout
        http_requests_total.labels(method='GET', endpoint='/api/data', status='500').inc()  # 记录本次 /api/data 请求返回状态码 500
        http_request_duration_seconds.labels(method='GET', endpoint='/api/data').observe(time.time() - start)  # 记录 /api/data 请求的总耗时（包含 DB 查询和错误处理）
        return jsonify({"error": "database timeout"}), 500  # 返回 500 错误响应，提示数据库超时
    
    http_requests_total.labels(method='GET', endpoint='/api/data', status='200').inc()  # 正常流程：记录 /api/data 请求状态码 200
    http_request_duration_seconds.labels(method='GET', endpoint='/api/data').observe(time.time() - start)  # 记录 /api/data 正常请求的总耗时
    return jsonify({"data": list(range(random.randint(10, 100)))})  # 返回随机长度（10~99）的数据列表，模拟正常查询结果

@app.route('/api/heavy')  # 注册重计算 API 路由（/api/heavy），模拟 CPU 密集型任务
def api_heavy():  # 重计算接口处理函数
    start = time.time()  # 记录请求开始时间
    compute_time = random.gauss(0.3, 0.1)  # 生成计算耗时，服从正态分布：均值 300ms，标准差 100ms
    if random.random() < 0.15:  # 15% 概率触发超长计算任务（如复杂算法、大数据量处理）
        compute_time = random.uniform(1.5, 3.0)  # 超长计算耗时随机落在 1.5s~3.0s
    time.sleep(compute_time)  # 模拟 CPU 密集型计算耗时
    if random.random() < 0.1:  # 10% 概率触发内存飙升（模拟计算过程中大量数据加载到内存）
        app_memory_usage_bytes.set(random.uniform(2500, 3000) * 1024 * 1024)  # 模拟内存飙升至 2500MB~3000MB（字节单位）
    http_requests_total.labels(method='GET', endpoint='/api/heavy', status='200').inc()  # 记录 /api/heavy 请求状态码 200
    http_request_duration_seconds.labels(method='GET', endpoint='/api/heavy').observe(time.time() - start)  # 记录 /api/heavy 请求总耗时
    return jsonify({"result": "heavy computation done", "duration": compute_time})  # 返回计算结果及实际耗时

@app.route('/health')  # 注册健康检查路由（/health），供负载均衡器或 Kubernetes 探针使用
def health():  # 健康检查处理函数
    return jsonify({"status": "healthy"})  # 返回简单的健康状态 JSON 响应，HTTP 默认状态码 200

@app.route('/metrics')  # 注册 Prometheus 指标暴露路由（/metrics 为 Prometheus 默认抓取端点）
def metrics():  # 指标暴露处理函数
    return generate_latest(registry), 200, {'Content-Type': CONTENT_TYPE_LATEST}  # 以 Prometheus 文本格式返回注册表中的所有指标；HTTP 200；设置正确的 Content-Type

@app.route('/error')  # 注册手动触发错误的路由（/error），用于测试告警规则或错误处理逻辑
def trigger_error():  # 手动触发错误处理函数
    app_errors_total.labels(error_type='manual_trigger').inc()  # 手动触发错误计数器 +1，标签为 manual_trigger
    http_requests_total.labels(method='GET', endpoint='/error', status='500').inc()  # 记录 /error 请求状态码 500
    return jsonify({"error": "manual error triggered"}), 500  # 返回 500 错误响应，提示手动触发成功

if __name__ == '__main__':  # 当直接运行本脚本时（非被导入为模块时）执行以下代码块
    app.run(host='0.0.0.0', port=5000, threaded=True)  # 启动 Flask 开发服务器：host='0.0.0.0' 监听所有网卡；port=5000；threaded=True 启用多线程处理并发