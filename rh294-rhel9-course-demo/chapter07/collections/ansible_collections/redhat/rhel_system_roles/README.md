Red Hat Enterprise Linux System Roles Ansible Collection
=====================================

Red Hat Enterprise Linux System Roles is a set of roles for managing Red Hat Enterprise Linux system components.

## Dependencies

If installing from RPM, the dependencies will be installed with the package.
Otherwise, the dependencies are listed in `requirements.txt` and/or `bindep.txt`.

## Installation

There are currently two ways to use the Red Hat Enterprise Linux System Roles Collection in your setup.

### Installation from Automation Hub

You can install the collection from Automation Hub by running:
```
ansible-galaxy collection install redhat.rhel_system_roles
```

After the installation, the roles are available as `redhat.rhel_system_roles.<role_name>`.

Please see the [Using Ansible collections documentation](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for further details.

### Installation via RPM

You can install the collection with the software package management tool `dnf` by running:
```
dnf install rhel-system-roles
```

## Documentation
The official RHEL System Roles documentation can be found in the [Product Documentation section of the Red Hat Customer Portal](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/administration_and_configuration_tasks_using_system_roles_in_rhel/index).

## Support

### Supported Ansible Versions

The supported Ansible versions are aligned with currently maintained Ansible versions that support Collections (Ansible 2.9 and later). You can find the list of maintained Ansible versions [here](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#release-status).

### Modules and Plugins

The modules and other plugins in this collection are private, used only internally to the collection, unless otherwise noted.


### Supported Roles

<!--ts-->
  * postfix
  * selinux
  * timesync
  * kdump
  * network
  * storage
  * metrics
  * tlog
  * kernel_settings
  * logging
  * nbde_server
  * nbde_client
  * certificate
  * crypto_policies
  * sshd
  * ha_cluster
  * vpn
  * firewall
  * cockpit
  * podman
  * ad_integration
  * rhc
  * journald
<!--te-->

### Private Roles

<!--ts-->
  * private_metrics_subrole_elasticsearch
  * private_metrics_subrole_spark
  * private_metrics_subrole_grafana
  * private_metrics_subrole_repository
  * private_metrics_subrole_redis
  * private_metrics_subrole_postfix
  * private_metrics_subrole_pcp
  * private_metrics_subrole_mssql
  * private_metrics_subrole_bpftrace
  * private_logging_subrole_rsyslog
<!--te-->
