# performancecopilot.metrics.redhat.rhel_system_roles.private_metrics_subrole_grafana

Installs and configures [Grafana](https://redhat.rhel_system_roles.private_metrics_subrole_grafana.com) for use with the [Performance Co-Pilot](https://pcp.io/) toolkit.

## Requirements

Uses features of Grafana v6+.  All available PCP datasources will be installed from the [redhat.rhel_system_roles.private_metrics_subrole_grafana-pcp](https://github.com/performancecopilot/redhat.rhel_system_roles.private_metrics_subrole_grafana-pcp) package.

## Role Variables

None.

## Dependencies

None.

## Example Playbook

Setup PCP and Grafana for graphing live metrics locally using Vector.

```yaml
- hosts: monitoring
  roles:
    - role: performancecopilot.metrics.redhat.rhel_system_roles.private_metrics_subrole_grafana
    - role: performancecopilot.metrics.pcp
      vars:
        pcp_rest_api: yes
```

## License

MIT

## Author Information

An official role for PCP, maintained by the PCP developers <pcp@groups.io>
