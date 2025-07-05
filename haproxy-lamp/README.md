# **HAproxy LAMP Ansible Demo**

- haproxy-lamp 项目中使用多个自定义角色部署 Apache HTTPD 服务器与 PHP 应用，此应用可对接后端 MariaDB 数据库。
- HAProxy 实现客户端流量的反向代理至后端 Web 服务器。
- Ansible Playbook 运行环境：RHEL 9.x
- 项目使用方法：

  ```bash
  [devops@workstation ~]$ cd haproxy-lamp/
  [devops@workstation haproxy-lamp]$ ansible-navigator run site.yml
  # 运行 playbook，部署多个应用。

  # 多次访问 HAProxy 服务所在的 serverc 节点，可见流量被代理至不同后端，并且完成数据库查询。
  [devops@workstation haproxy-lamp]$ curl http://serverc.lab.example.com/index.php
  Current hostname: serverb.lab.example.com<br>Database connect successfully<br>Show Databases List: <br> ansible
   information_schema
   mysql
   performance_schema

  [devops@workstation haproxy-lamp]$ curl http://serverc.lab.example.com/index.php
  Current hostname: servera.lab.example.com<br>Database connect successfully<br>Show Databases List: <br> ansible
   information_schema
   mysql
   performance_schema
  ```
