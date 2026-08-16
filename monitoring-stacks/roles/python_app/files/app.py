#!/usr/bin/env python3
"""
Prometheus 监控示例应用
使用 prometheus_client SDK 暴露自定义业务指标
"""

import time
import random
import threading
from flask import Flask, jsonify
from prometheus_client import (
    Counter, Histogram, Gauge, generate_latest,
    CONTENT_TYPE_LATEST, CollectorRegistry
)

app = Flask(__name__)
registry = CollectorRegistry()

# ==================== 业务指标定义 ====================
http_requests_total = Counter(
    'http_requests_total', 'Total HTTP requests',
    ['method', 'endpoint', 'status'], registry=registry
)

http_request_duration_seconds = Histogram(
    'http_request_duration_seconds', 'HTTP request duration in seconds',
    ['method', 'endpoint'],
    buckets=[0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0],
    registry=registry
)

app_active_connections = Gauge(
    'app_active_connections', 'Number of active connections', registry=registry
)

app_errors_total = Counter(
    'app_errors_total', 'Total application errors',
    ['error_type'], registry=registry
)

app_cpu_usage_percent = Gauge(
    'app_cpu_usage_percent', 'Simulated application CPU usage percent', registry=registry
)

app_memory_usage_bytes = Gauge(
    'app_memory_usage_bytes', 'Simulated application memory usage in bytes', registry=registry
)

app_queue_depth = Gauge(
    'app_queue_depth', 'Current queue depth', registry=registry
)

db_query_duration_seconds = Histogram(
    'db_query_duration_seconds', 'Database query duration in seconds',
    buckets=[0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0],
    registry=registry
)

# ==================== 模拟后台任务 ====================
def background_metrics_simulator():
    while True:
        cpu = random.gauss(45, 20)
        if random.random() < 0.05:
            cpu = random.uniform(85, 98)
        app_cpu_usage_percent.set(max(0, min(100, cpu)))

        mem_mb = random.gauss(512, 150)
        if random.random() < 0.03:
            mem_mb = random.uniform(1800, 2200)
        app_memory_usage_bytes.set(max(100, mem_mb * 1024 * 1024))

        queue = random.gauss(10, 5)
        if random.random() < 0.02:
            queue = random.uniform(80, 120)
        app_queue_depth.set(max(0, queue))

        app_active_connections.set(random.randint(5, 50))
        time.sleep(5)

simulator_thread = threading.Thread(target=background_metrics_simulator, daemon=True)
simulator_thread.start()

# ==================== HTTP 路由 ====================
@app.route('/')
def index():
    start = time.time()
    http_requests_total.labels(method='GET', endpoint='/', status='200').inc()
    delay = random.gauss(0.02, 0.01)
    if random.random() < 0.1:
        delay = random.uniform(0.6, 1.2)
    time.sleep(delay)
    http_request_duration_seconds.labels(method='GET', endpoint='/').observe(time.time() - start)
    return jsonify({"status": "ok", "service": "prometheus-demo-app"})

@app.route('/api/data')
def api_data():
    start = time.time()
    db_start = time.time()
    db_delay = random.gauss(0.05, 0.02)
    if random.random() < 0.08:
        db_delay = random.uniform(0.8, 2.0)
    time.sleep(db_delay)
    db_query_duration_seconds.observe(time.time() - db_start)
    
    if random.random() < 0.05:
        app_errors_total.labels(error_type='database_timeout').inc()
        http_requests_total.labels(method='GET', endpoint='/api/data', status='500').inc()
        http_request_duration_seconds.labels(method='GET', endpoint='/api/data').observe(time.time() - start)
        return jsonify({"error": "database timeout"}), 500
    
    http_requests_total.labels(method='GET', endpoint='/api/data', status='200').inc()
    http_request_duration_seconds.labels(method='GET', endpoint='/api/data').observe(time.time() - start)
    return jsonify({"data": list(range(random.randint(10, 100)))})

@app.route('/api/heavy')
def api_heavy():
    start = time.time()
    compute_time = random.gauss(0.3, 0.1)
    if random.random() < 0.15:
        compute_time = random.uniform(1.5, 3.0)
    time.sleep(compute_time)
    if random.random() < 0.1:
        app_memory_usage_bytes.set(random.uniform(2500, 3000) * 1024 * 1024)
    http_requests_total.labels(method='GET', endpoint='/api/heavy', status='200').inc()
    http_request_duration_seconds.labels(method='GET', endpoint='/api/heavy').observe(time.time() - start)
    return jsonify({"result": "heavy computation done", "duration": compute_time})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/metrics')
def metrics():
    return generate_latest(registry), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/error')
def trigger_error():
    app_errors_total.labels(error_type='manual_trigger').inc()
    http_requests_total.labels(method='GET', endpoint='/error', status='500').inc()
    return jsonify({"error": "manual error triggered"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
