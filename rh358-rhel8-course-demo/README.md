# RH358v8.1 课堂笔记

## Chapter1

- RHEL 各版本网络服务的变化：
  
  - RHEL7：network-scripts 或 NetworkManager
  - RHEL8：network-scripts 或 NetworkManager (推荐)
  - RHEL9：network-scripts (淘汰) NetworkManager (主要)

- 课程使用 RHEL8.1 所以推荐使用 NetworkManager

- systemd 中 active 状态的示例：
  - active (running): sshd.service (用户空间进程)
  - active (exited): nfs-server.service (内核空间线程 `[nfsd]`)
  - active (waiting): sysstat-collect.timer (等待事件到来)
  - static: cockpit.service (服务之间存在依赖彼此可拉起)

- systemctl 有用的命令：
  
  ```bash
  $ systemctl list-units --type=service
  # 列举已加载的单元文件
  $ systemctl list-unit-files --type=service
  # 列举所有存在的单元文件
  systemctl list-dependencies multi-user.target
  ```

- systemctl reload 经历的阶段：hang -> load config file -> start

- systemctl reload 的进程其 PID 不变！

- NetworkManager 的使用前提：
  - 保证 `NetworkManager.service` 与 `dbus.service` 处于 running 状态
  - nmcli/nmtui 使用命令行或者图形化界面管理网络

- nmcli 中的两个概念：
  - dev：设备，nmcli 管理的设备。
  - connection：连接，可理解为具体设备的可用配置文件

- NetworkManager 配置文件存放的路径：  
  - `/etc/sysconfig/network-scripts/{ifcfg-*,route-*}`：RHEL7/8/9 均支持
  - `/etc/NetworkManager/system-connections/*`：优先级更高，配置文件以 INI 格式存在，RHEL8/9 中常见。

```bash
$ nmcli gen permissions
# 查看当前用户具有的网络操作能力(权限)
$ man 7 nmcli-examples
# 查看 nmcli 的命令使用
```

- Ansible 的发展：
  - Ansible Core + Collections + Roles：构成了分布式体系，解耦了 Ansible 引擎压力与扩展平台的架构。
  - Ansible bundle

- 实验环境中 Ansible 是 2.9.5 版本，因此属于第二种执行方式，不支持 collection 与 ansible-navigator。

- 安装 RHEL 系统角色：
  
  ```bash
  [student@workstation ~]$ sudo yum install -y rhel-system-roles
  [student@workstation ~]$ su -
  [root@workstation ~]# cd /usr/share/doc/rhel-system-roles/ && ls -lh
  # 查看所有安装的系统角色
  ```

- 注意：针对于角色而言，不直接修改角色中的任务文件，通过修改角色提供的 **`变量`** 来完成角色行为的改变！

- rhel-system-roles 中网络角色的变量查询文件：
  
  ```bash
  [root@workstation ~]# firefox file:///usr/share/doc/rhel-system-roles/network/README.html#_variables
  ```

- Ansible 收集本地的事实变量：`$ ansible localhost -m setup | less`

- Ansible `set_fact` 模块使用示例：获取指定主机的 MAC 地址

## Chapter 2

- 讨论1：[关于 bonding 与 team 在 RHEL9 中选择](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/9.0_release_notes/deprecated_functionality#deprecated-functionality_networking)

- 讨论2：bonding 与 team 具体的不同点体现在哪里？

- team 故障排错命令：
  
  ```bash
  $ teamnl <team_name> ports
  $ teamnl <team_name> getoption activeport
  # 查看活动接口
  
  $ teamdctl <team_name> set item runner.active_port <interface_name>
  # 更改活动接口
  $ teamdctl <team_name> state
  $ teamdctl <team_name> config dump
  # 获取 team 配置的 JSON 信息
  
  $ nmcli con mod <team_name> team.runner roundrobin
  # 修改 team 的 runner 模式
  ```

**练习 P73 (15min)**：自动化网络 team

## Chapter3

- DNS 的重要概念：
  - DNS 的功能
  - DNS 分层结构
  - DNS 资源的分类

**练习 P102 (15min)**：利用 unbound 名称缓存服务器来加速客户端到目标主机的访问速率

- DNS 解析的顺序：`/etc/nsswitch.conf` 文件决定了名称解析的顺序
  - files
  - dns
  - db
  - myhostname

- DNS 的额外查询命令：
  
  ```bash
  $ getent hosts [<hostname>|<fqdn>]
  # 根据 /etc/nsswitch.conf 文件中的顺序查找解析信息
  ```

- DNS 查询码：NOERROR, SERVERFAIL, NXDOMAIN, REFUSED

- 开源的 DNS 软件：BIND9, dnsmasq(dns+dhcp)

- BIND9 配置文件的路径：
  - 主配置文件：`/etc/named.conf`
  - 区域正向/反向解析文件：`/var/named/*.zone`

**重点-练习 P127 (30min)**：使用 BIND 9 配置权威名称服务器
**重点-练习 P145 (30min)**：自动化执行名称服务器配置

## Chapter4

**练习P179 (20min)**：使用 DHCP 配置 IPv4 地址分配

## Chapter5~6

略 (自学)

## Chapter7

**练习 P293 (10min)**：在 MariaDB 中使用 SQL
**练习 P324 (30min)**：自动部署 MariaDB

## Chapter8

- Apache HTTPD 的配置指令不单单是在配置的块 (block) 中，也可以在全局配置文件中出现！

**练习 P359 (10min)**：使用 Apache HTTPD 配置基本 Web 服务器
**练习 P364 (15min)**：使用 Apache HTTPD 对虚拟主机进行配置和故障排除

- 生成 client/server CA 证书：
  - 第一种：
    - 权威 CA 证书
    - client/server 端的密钥文件 (key)
    - client/server 端的签名请求文件 (csr)：由密钥文件协助生成
    - client/server 端的 CA 证书：由权威 CA 证书与 csr 文件协同生成
  - 第二种：
    - 自签名证书

**练习 P372 (15min)**：使用 Apache HTTPD 配置 HTTPS

- Nginx 的安装方法：
  - rpm 包安装：yum/dnf
  - 编译安装：系统体系架构不同编译方式存在区别
  - 容器镜像运行

- Nginx 配置目录与配置文件 (默认安装)：
  - 配置目录：
    - `/etc/nginx/` (对比 httpd 中 `/etc/httpd/conf/`)
    - `/etc/nginx/conf.d/` (对比 httpd 中 `/etc/httpd/conf.d/`)
  - 配置文件：
    - `/etc/nginx/nginx.conf` (对比 httpd 中 `/etc/httpd/conf/httpd.conf`)
    - `/etc/nginx/conf.d/*.conf` (对比 httpd 中 `/etc/httpd/conf.d/*.conf`)

**练习 P380 (15min)**：使用 Nginx 配置 Web 服务器    

## Chapter10

**练习 P466 (15min)**：导出 NFS 文件系统

- 各个服务检查配置文件的方法：
  - named:
    - named-checkconf
    - named-checkzone zone zone-file
  - dhcpd: dhcpd -t
  - httpd: httpd -t 
  - nginx: nginx -t 
  - samba: testparm

## Chapter11

- iSCSI 客户端：
  - iSCSI HBA 卡：硬件解析 iSCSI 协议 (硬件实现)
  - iSCSI initiator：软件解析 iSCSI 协议 (软件实现，无 iSCSI HBA)

- 一个目标 (targer) 上可有一个或多个 iqn (iSCSI 限定名称)

- 门户 (portal) 代表了目标可以被哪些客户端所访问与使用

- 逻辑单元号 (LUN) 是指目标中可共享的块设备或文件在 iSCSI 中的逻辑映射设备编号
