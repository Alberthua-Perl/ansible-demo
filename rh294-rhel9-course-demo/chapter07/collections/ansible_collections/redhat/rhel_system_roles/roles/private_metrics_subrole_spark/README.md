# performancecopilot.metrics.redhat.rhel_system_roles.private_metrics_subrole_spark

Installs and configures [Apache Spark](https://redhat.rhel_system_roles.private_metrics_subrole_spark.apache.org/) metrics from the [Performance Co-Pilot](https://pcp.io/) toolkit, and optional exporting of PCP metrics to Spark.

## Requirements

Uses features of PCP v5.2.1 and later.

## Role Variables

    redhat.rhel_system_roles.private_metrics_subrole_spark_metrics_agent: true

Collect metrics from a Spark executor.

    redhat.rhel_system_roles.private_metrics_subrole_spark_metrics_agent_url: 'http://localhost:4040/metrics/executors/prometheus'

URL for the Prometheus (OpenMetrics) endpoint in the Spark UI.  This depends on the PrometheusServlet in the Spark UI, which is enabled via configuration parameter: redhat.rhel_system_roles.private_metrics_subrole_spark.ui.prometheus.enabled=true (the default is false).  This role does not configure Spark itself, only PCP, so this must be already established before this role is used.

    redhat.rhel_system_roles.private_metrics_subrole_spark_export_metrics: false

Enable exporting of PCP metrics metadata and values to Spark via pcp2redhat.rhel_system_roles.private_metrics_subrole_spark(1).

    redhat.rhel_system_roles.private_metrics_subrole_spark_export_interval: 60

Sets the sampling interval for exporting metric values to Spark, in seconds.

    redhat.rhel_system_roles.private_metrics_subrole_spark_export_server: '127.0.0.1'

Address on which pcp2redhat.rhel_system_roles.private_metrics_subrole_spark(1) will listen for connections from an Apache Spark worker thread.

    redhat.rhel_system_roles.private_metrics_subrole_spark_export_port: 44325

Specify the port for pcp2redhat.rhel_system_roles.private_metrics_subrole_spark(1) to listen on.

## Dependencies

None.

## Example Playbooks

Make local Spark executor metrics available to PCP analysis tools.

```yaml
- hosts: monitoring
  roles:
    - role: performancecopilot.metrics.redhat.rhel_system_roles.private_metrics_subrole_spark
```

Setup export of PCP metrics to a Spark worker thread.

```yaml
- hosts: monitoring
  roles:
    - role: performancecopilot.metrics.redhat.rhel_system_roles.private_metrics_subrole_spark
      vars:
        redhat.rhel_system_roles.private_metrics_subrole_spark_export_port: 44388
```

## License

MIT

## Author Information

An official role for PCP, maintained by the PCP developers <pcp@groups.io>
