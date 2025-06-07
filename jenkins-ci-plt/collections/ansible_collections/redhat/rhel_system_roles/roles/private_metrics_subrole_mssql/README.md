# performancecopilot.metrics.redhat.rhel_system_roles.private_metrics_subrole_mssql

Installs and configures Microsoft [SQL Server](https://docs.microsoft.com/en-us/sql/) metrics from the [Performance Co-Pilot](https://pcp.io/) toolkit.

## Requirements

Requires a SQL Server 2017 (or later) database server, and Python ODBC software [pyodbc](https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/).  This role does *not* install or configure those components, rather it configures PCP to extract metrics from SQL Server using them.

The SQL Server metrics are available from PCP v5.2 and later.

## Role Variables

    redhat.rhel_system_roles.private_metrics_subrole_mssql_agent_trusted: yes

Connect to SQL Server using [Windows Authentication mode](https://docs.microsoft.com/en-us/sql/relational-databases/security/choose-an-authentication-mode?view=sql-server-ver15#connecting-through-windows-authentication)

    redhat.rhel_system_roles.private_metrics_subrole_mssql_agent_username: 'sa'

Connect to SQL server using [SQL Server Authentication mode](https://docs.microsoft.com/en-us/sql/relational-databases/security/choose-an-authentication-mode?view=sql-server-ver15#connecting-through-sql-server-authentication).  This is mutually exclusive with the redhat.rhel_system_roles.private_metrics_subrole_mssql_agent_trusted authentication mode.

    redhat.rhel_system_roles.private_metrics_subrole_mssql_agent_password: 'admin'

Sets the pass phrase associated with redhat.rhel_system_roles.private_metrics_subrole_mssql_agent_username, for use when connecting with SQL Server Authentication mode (only).

    redhat.rhel_system_roles.private_metrics_subrole_mssql_agent_timeout: 2

Close the connection to SQL Server if a response is not received within this number of seconds.  Subsequent requests will result in attempts to reestablish a connection.

## Dependencies

None.

## Example Playbooks

Setup PCP SQL Server metrics using Windows Authentication mode.

```yaml
- hosts: monitoring
  roles:
    - role: performancecopilot.metrics.redhat.rhel_system_roles.private_metrics_subrole_mssql
      vars:
        redhat.rhel_system_roles.private_metrics_subrole_mssql_agent_timeout: 5
```

Setup PCP SQL Server metrics using SQL Server Authentication.

```yaml
- hosts: monitoring
  roles:
    - role: performancecopilot.metrics.redhat.rhel_system_roles.private_metrics_subrole_mssql
      vars:
        redhat.rhel_system_roles.private_metrics_subrole_mssql_agent_trusted: no
        redhat.rhel_system_roles.private_metrics_subrole_mssql_agent_username: sa
        redhat.rhel_system_roles.private_metrics_subrole_mssql_agent_password: admin
```

## License

MIT

## Author Information

An official role for PCP, maintained by the PCP developers <pcp@groups.io>
