# **同步节点 SSH 公钥**

使用 `sync-sshkey.yml` playbook 可实现以下功能：

- 若当前执行 playbook 的用户不存在 SSH 公私钥，那么可自动创建，用于后续的 SSH 公钥同步。
- 若已存在 SSH 公私钥，可直接对受管节点完成 SSH 公钥同步，为之后的 playbook 执行创造条件。
