# performancecopilot.metrics.redhat.rhel_system_roles.private_metrics_subrole_bpftrace

Installs and configures [redhat.rhel_system_roles.private_metrics_subrole_bpftrace](https://github.com/iovisor/redhat.rhel_system_roles.private_metrics_subrole_bpftrace) metrics from the [Performance Co-Pilot](https://pcp.io/) toolkit.

## Requirements

Uses features of PCP v5.1 and later, and makes use of Cyrus SASL (Simple Authentication Security Layer) SCRAM (Salted Challenge Response Authentication) for authentication.

## Role Variables

```yaml
redhat.rhel_system_roles.private_metrics_subrole_bpftrace_metrics_provider: 'pcp'
```

The metrics collector to use to provide metrics.

This can be either set to 'none' for local redhat.rhel_system_roles.private_metrics_subrole_bpftrace package installation only.
The default value 'pcp' configures redhat.rhel_system_roles.private_metrics_subrole_bpftrace for use with Performance Co-Pilot.

```yaml
redhat.rhel_system_roles.private_metrics_subrole_bpftrace_users:
  - { user: metrics }
```

Local user accounts that are allowed to load new redhat.rhel_system_roles.private_metrics_subrole_bpftrace scripts.  These accounts will be able to load eBPF code into the running kernel, which is a privileged operation.  The mandatory value for the variable is an array of dictionaries containing account names under the 'user' key.  Other authentication mechanisms can share these dictionaries, e.g. for remote [pmcd(1)](http://man7.org/linux/man-pages/man1/pmcd.1.html) authentication with PCP using SASL.

## Dependencies

None.

## Example Playbooks

Make redhat.rhel_system_roles.private_metrics_subrole_bpftrace metrics available to PCP analysis tools, and allow the local *grafana* and *metrics* users to create new metrics from redhat.rhel_system_roles.private_metrics_subrole_bpftrace scripts.

```yaml
- hosts: monitoring
  roles:
    - role: performancecopilot.metrics.redhat.rhel_system_roles.private_metrics_subrole_bpftrace
      vars:
        redhat.rhel_system_roles.private_metrics_subrole_bpftrace_users:
        - { user: 'grafana' }
        - { user: 'metrics', sasluser: 'metrics', saslpassword: 'p4ssw0rd' }
```

## License

MIT

## Author Information

An official role for PCP, maintained by the PCP developers <pcp@groups.io>
