# FIO 文件系统性能测试

## 项目说明

- 示例用于 FIO 对已有文件系统的性能测试，包括顺序读写、随机读写、混合读写，用以发现存在的潜在性能问题。
- 测试结果通过结构化提取 JSON 后获得核心性能数据。
- 提取的结构化数据通过 LLM 分析后生成分析报告以供参考，LLM 可以是 Qwen3、DeepSeek、Kimi、GLM 等公共模型，也可以换成私有化部署的模型。

## 项目使用

```bash
$ cd fio-fstest/
$ vim vars/llm.yml
  ...
  llm_api_key: sk-...    # 修改为个人的 API KEY（提前申请相关模型的 API KEY）
  ...

$ ansible-navigator run -m stdout 20-llm_api_call.yml
# 可选步骤：测试与 LLM API 的连通性与认证可用性
# 成功执行后在当前目录中生成 Markdown 文件

$ ansible-navigator run -m stdout 10-fio_async_test.yml
# 核心步骤：FIO 测试，指标结构化输出与 LLM 分析

$ ansible-navigator run -m stdout 10-fio_async_test.yml --tag cleanup_tmp
# 清除测试临时文件
```

## 结果检查

打开 results 目录中的 FINAL-REPORT.md 文件，可链接至不同受管主机节点的分析文件。

