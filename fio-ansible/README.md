# Ansible 自动化 FIO 文件系统测试示例

## 项目说明

- 示例用于 FIO 对已有文件系统的性能测试，包括顺序读写、随机读写、混合读写。
- 测试结果通过结构化提取后获得核心性能数据。
- 提取的数据通过 LLM 分析后生成分析报告以供参考。

## 项目使用

```bash
$ cd fio-ansible/
$ vim vars/llm.yml
  ...
  llm_api_key:     # 修改为你的 API KEY 
  ...

$ ansible-navigator run -m stdout 20-llm_api_call.yml
# 可选步骤：测试与 LLM API 的连通性与认证可用性

$ ansible-navigator run -m stdout 10-fio_async_test.yml
# 核心步骤：FIO 测试，指标结构化输出与 LLM 分析

$ ansible-navigator run -m stdout 10-fio_async_test.yml --cleanup_tmp
# 清除测试临时文件
```

