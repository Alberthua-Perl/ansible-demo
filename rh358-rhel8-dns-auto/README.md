## 关于本实验 DNS 架构的说明

- bastion.lab.example.com 节点中使用子域委托（`subdomain delegated`）将 backend.lab.example.com 委托至 serverb.lab.example.com 节点。
- 在 bastion.lab.example.com 节点的区域配置文件中存在 `backend       IN  NS        serverb.lab.example.com.` 的资源记录。
- 该实验中的主 DNS 名称服务器为 `serverb.lab.example.com` 并且作为权威名称服务器（`SOA`）。
