# 📊 可视化 Prometheus 监控告警平台构建与应用自定义指标验证

## 项目说明

- 实验目标：此项目采用 Ansible 自动化方式实现可视化监控告警平台的部署与测试
- 实验环境：RH294-RHEL9.0

## 项目使用

### 1. 部署 Nginx 共享 Web 服务器以提供内部材料供应

```bash
[devops@workstation ~]$ cd ~/nginx-deployment/
[devops@workstation nginx-deployment]$ ansible-navigator run -m stdout site.yml
[devops@workstation nginx-deployment]$ sudo su -
[root@workstation ~]# cd /var/www/html/materials    # 切换 Web 材料目录
[root@workstation materials]# wget https://rh-course-materials.oss-cn-hangzhou.aliyuncs.com/monitor/prometheus-3.8.0.linux-amd64.tar.gz
[root@workstation materials]# wget https://rh-course-materials.oss-cn-hangzhou.aliyuncs.com/monitor/node_exporter-1.10.2.linux-amd64.tar.gz
[root@workstation materials]# wget https://rh-course-materials.oss-cn-hangzhou.aliyuncs.com/monitor/alertmanager-0.30.0.linux-amd64.tar.gz
[root@workstation materials]# wget https://rh-course-materials.oss-cn-hangzhou.aliyuncs.com/monitor/grafana-enterprise_12.3.3_21957728731_linux_amd64.tar.gz
```

### 2. 各个节点基础设置

```bash
[devops@workstation ~]$ cd ~/monitoring-stacks/
[devops@workstation monitoring-stacks]$ ansible-navigator run -m stdout playbooks/base_setup.yml
...
TASK [redhat.rhel_system_roles.selinux : Fail if reboot is required] *********************************************************
fatal: [servera]: FAILED! => {"changed": false, "msg": "Reboot is required to apply changes. Re-execute the role after boot."}
fatal: [serverb]: FAILED! => {"changed": false, "msg": "Reboot is required to apply changes. Re-execute the role after boot."}
fatal: [serverc]: FAILED! => {"changed": false, "msg": "Reboot is required to apply changes. Re-execute the role after boot."}
fatal: [serverd]: FAILED! => {"changed": false, "msg": "Reboot is required to apply changes. Re-execute the role after boot."}
...
# 注意：SELinux 设置为 disabled 状态时，playbook 在运行过程中 failed 中断，手动重启节点后再运行 base_setup.yml。

[devops@workstation monitoring-stacks]$ ansible all -m command -a 'systemctl reboot'
[devops@workstation monitoring-stacks]$ ansible-navigator run -m stdout playbooks/base_setup.yml
```

### 3. 部署运行可视化 Prometheus 监控告警平台与应用

方法1：分别指定不同组件独立部署运行

```bash
[devops@workstation monitoring-stacks]$ ansible-navigator run -m stdout playbooks/site.yml --tags prometheus
[devops@workstation monitoring-stacks]$ ansible-navigator run -m stdout playbooks/site.yml --tags alertmanager
# 注意：
#   prometheus 部署完成后访问 9090 端口，暂时只有自身与 alertmanager 节点处于 UP 状态，
#   直至其他节点的 node_exporter 部署运行后才将出现对应的 UP 状态。
[devops@workstation monitoring-stacks]$ ansible-navigator run -m stdout playbooks/site.yml --tags node_exporter
[devops@workstation monitoring-stacks]$ ansible-navigator run -m stdout playbooks/site.yml --tags grafana
[devops@workstation monitoring-stacks]$ ansible-navigator run -m stdout playbooks/site.yml --tags python_app
```

方法2：直接一键运行

```bash
[devops@workstation monitoring-stacks]$ ansible-navigator run -m stdout playbooks/site.yml
```

### 4. Web 浏览器验证部署与测试

访问 http://servera.lab.example.com:9090/targets 确认各节点在 prometheus 配置文件中是否被正确识别

## Ansible 故障点排除

### 1. Prometheus 告警规则文件 `roles/prometheus/templates/{node_rules.yml.j2,app_rules.yml.j2}`

Prometheus 告警规则文件中类似 `{{ $labels.instance }}` 的变量，需要被 prometheus 告警引擎解析。但 Ansible Jinja2 引擎将提前解析此类变量，因语法不匹配而直接报错。因此，需要使用 `{{ '{{ $labels.instance }}' }}` 形式替换原有变量即可解决 Ansible 运行过程中的报错。

### 2. Alertmanager 配置文件 `roles/alertmanager/templates/alertmanager.yml.j2`

Ansible Jinjia2 引擎与 Alertmanager Go 模板语法存在冲突。因此，使用 `{% raw %}` 与 `{% endraw %}` 包裹 Go 模板告知 Jinjia2 引擎不解析以原样输出。

### 3. Prometheus 角色任务文件 `prometheus/tasks/main.yml`

此任务文件中 “创建告警规则目录” 的参数 `mode:` 应设置为 `0755`。若设置为 `0644`，虽然在部署过程中不出现任何报错，但在 prometheus 部署后访问 web UI 时，将始终显示 `No rules found`，这表明无法加载各类规则文件，即使 `promtool check rule` 命令返回正确，也无法解决此问题。原因在于目录权限与文件权限的区别，目录权限中的 x 权限位允许切换至目录中加载，而文件权限位无法实现。

## 参考链接

- [📊 一键部署二进制 Prometheus+Alertmanager+Granafa 监控平台 | GitHub](https://github.com/Alberthua-Perl/sc-col/tree/master/monitor)
- [Prometheus 教程](https://www.echo.cool/docs/category/prometheus-%E6%95%99%E7%A8%8B)

