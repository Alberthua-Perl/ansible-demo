Changelog
=========

[1.21.1] - 2023-03-16
----------------------------

### New Features

- [rhc - New Role - Red Hat subscription management, insights management](https://bugzilla.redhat.com/show_bug.cgi?id=2141330)

### Bug Fixes

- none

[1.21.0] - 2023-02-20
----------------------------

### New Features

- [ad_integration - New role - manage AD integration, join to AD domain](https://bugzilla.redhat.com/show_bug.cgi?id=2140795)
- [cockpit - convert cockpit role to use firewall, selinux role, and certificate role](https://bugzilla.redhat.com/show_bug.cgi?id=2137663)
- [ha_cluster - Allow quorum device configuration](https://bugzilla.redhat.com/show_bug.cgi?id=2140804)
- [ha_cluster - convert ha_cluster role to use firewall, selinux and certificate role](https://bugzilla.redhat.com/show_bug.cgi?id=2130010)
- [journald - New role - manage systemd-journald](https://bugzilla.redhat.com/show_bug.cgi?id=2165175)
- [logging - convert logging role to use firewall, selinux role, and certificate role](https://bugzilla.redhat.com/show_bug.cgi?id=2130357)
- [metrics - convert metrics role to use firewall and selinux role](https://bugzilla.redhat.com/show_bug.cgi?id=2133528)
- [nbde_server - convert nbde_server role to use firewall and selinux role](https://bugzilla.redhat.com/show_bug.cgi?id=2133930)
- [network - Support cloned MAC address](https://bugzilla.redhat.com/show_bug.cgi?id=2143768)
- [network - Support setting the metric of the default route for initscripts provider](https://bugzilla.redhat.com/show_bug.cgi?id=2134202)
- [network - Support the DNS priority](https://bugzilla.redhat.com/show_bug.cgi?id=2133858)
- [network - Support looking up named route table in routing rule](https://bugzilla.redhat.com/show_bug.cgi?id=2131293)
- [podman - New role - manage podman containers and systemd](https://bugzilla.redhat.com/show_bug.cgi?id=2143427)
- [postfix - convert postfix role to use firewall and selinux role](https://bugzilla.redhat.com/show_bug.cgi?id=2130329)
- [selinux - add support for the 'local' parameter](https://bugzilla.redhat.com/show_bug.cgi?id=2128843)
- [vpn - Add parameters shared_key_content, ike, esp, type, leftid, rightid](https://bugzilla.redhat.com/show_bug.cgi?id=2119102)
- [vpn - convert vpn role to use firewall and selinux role](https://bugzilla.redhat.com/show_bug.cgi?id=2130344)

### Bug Fixes

- [ha_cluster - use no_log in tasks looping over pot. secret parameters](https://bugzilla.redhat.com/show_bug.cgi?id=2143816)
- [ha_cluster - Allow enabled SBD on disabled cluster](https://bugzilla.redhat.com/show_bug.cgi?id=2153030)
- [ha_cluster - Fix stonith watchdog timeout](https://bugzilla.redhat.com/show_bug.cgi?id=2167528)
- [nbde_client - must handle clevis-luks-askpass and clevis-luks-askpass@ systemd unit names](https://bugzilla.redhat.com/show_bug.cgi?id=2126959)
- [nbde_client - nbde_client_clevis fails with a traceback and prints sensitive data](https://bugzilla.redhat.com/show_bug.cgi?id=2162782)
- [network - should route traffic via correct bond](https://bugzilla.redhat.com/show_bug.cgi?id=2168735)
- [selinux - managing modules is not idempotent](https://bugzilla.redhat.com/show_bug.cgi?id=2160152)
- [sshd,ssh,timesync - Unexpected templating type error - expected str instance, int found](https://bugzilla.redhat.com/show_bug.cgi?id=2129401)
- [tlog - Unconditionally enable the files provider](https://bugzilla.redhat.com/show_bug.cgi?id=2153043)

[1.20.1] - 2022-09-27
----------------------------

### New Features

- [ssh,sshd - Sync on final OpenSSH option name RequiredRSASize in ssh and sshd roles](https://bugzilla.redhat.com/show_bug.cgi?id=2129873)

### Bug Fixes

- none

[1.20.0] - 2022-08-05
----------------------------

### New Features

- [cockpit - Add customization of port](https://bugzilla.redhat.com/show_bug.cgi?id=2115152)
- [firewall - RFE: firewall-system-role: add ability to add interface to zone by PCI device ID](https://bugzilla.redhat.com/show_bug.cgi?id=2100942)
- [firewall - support for firewall_config - gather firewall facts](https://bugzilla.redhat.com/show_bug.cgi?id=2115154)
- [logging - [RFE] Support startmsg.regex and endmsg.regex in the files inputs](https://bugzilla.redhat.com/show_bug.cgi?id=2112145)
- [selinux - Added setting of seuser and selevel for completeness](https://bugzilla.redhat.com/show_bug.cgi?id=2115157)

### Bug Fixes

- [nbde_client - Sets proper spacing for parameter rd.neednet=1](https://bugzilla.redhat.com/show_bug.cgi?id=2115156)
- [network - fix IPRouteUtils.get_route_tables_mapping() to accept any whitespace sequence](https://bugzilla.redhat.com/show_bug.cgi?id=2115886)
- [ssh sshd - ssh, sshd: RSAMinSize parameter definition is missing](https://bugzilla.redhat.com/show_bug.cgi?id=2109998)
- [storage - [RHEL9] [WARNING]: The loop variable 'storage_test_volume' is already in use. You should set the `loop_var` value in the `loop_control` option for the task to something else to avoid variable collisions and unexpected behavior.](https://bugzilla.redhat.com/show_bug.cgi?id=2082736)

[1.19.3] - 2022-07-01
----------------------------

### New Features

- [firewall - support add/modify/delete services](https://bugzilla.redhat.com/show_bug.cgi?id=2100292)
- [network - [RFE] [network] Support managing the network through nmstate schema](https://bugzilla.redhat.com/show_bug.cgi?id=2072385)
- [storage - support for adding/removing disks to/from storage pools](https://bugzilla.redhat.com/show_bug.cgi?id=2072742)
- [storage - support for attaching cache volumes to existing volumes](https://bugzilla.redhat.com/show_bug.cgi?id=2072746)

### Bug Fixes

- [firewall - forward_port should accept list of string or list of dict](https://bugzilla.redhat.com/show_bug.cgi?id=2100605)
- [metrics - document minimum supported redis version required by rhel-system-roles](https://bugzilla.redhat.com/show_bug.cgi?id=2100286)
- [metrics - restart pmie, pmlogger if changed, do not wait for handler](https://bugzilla.redhat.com/show_bug.cgi?id=2100294)
- [storage - [RHEL9] _storage_test_pool_pvs get wrong data type in  test-verify-pool-members.yml](https://bugzilla.redhat.com/show_bug.cgi?id=2044119)

[1.19.2] - 2022-06-15
----------------------------

### New Features

- [sshd - system role should be able to optionally manage /etc/ssh/sshd_config on RHEL 9](https://bugzilla.redhat.com/show_bug.cgi?id=2052086)

### Bug Fixes

- none

[1.19.1] - 2022-06-13
----------------------------

### New Features

- [storage - support for creating and managing LVM thin pools/LVs](https://bugzilla.redhat.com/show_bug.cgi?id=2072745)
- [All roles should support running with gather_facts: false](https://bugzilla.redhat.com/show_bug.cgi?id=2078989)

### Bug Fixes

- none

[1.19.0] - 2022-06-06
----------------------------

### New Features

- [storage - support for creating and managing LVM thin pools/LVs](https://bugzilla.redhat.com/show_bug.cgi?id=2072745)
- [firewall - state no longer required for masquerade and ICMP block inversion](https://bugzilla.redhat.com/show_bug.cgi?id=2093423)

### Bug Fixes

- [storage - role raid_level "striped" is not supported](https://bugzilla.redhat.com/show_bug.cgi?id=2083410)

[1.18.0] - 2022-05-02
----------------------------

### New Features

- [firewall - [Improvement] Allow System Role to reset to default Firewalld Settings](https://bugzilla.redhat.com/show_bug.cgi?id=2043010)
- [metrics - [RFE] add an option to the metrics role to enable postfix metric collection](https://bugzilla.redhat.com/show_bug.cgi?id=2051737)
- [network - Rework the infiniband support](https://bugzilla.redhat.com/show_bug.cgi?id=2086965)
- [sshd - system role should not assume that RHEL 9 /etc/ssh/sshd_config has "Include > /etc/ssh/sshd_config.d/*.conf"](https://bugzilla.redhat.com/show_bug.cgi?id=2052081)
- [sshd - system role should be able to optionally manage /etc/ssh/sshd_config on RHEL 9](https://bugzilla.redhat.com/show_bug.cgi?id=2052086)

### Bug Fixes

- [storage - role cannot set mount_options for volumes](https://bugzilla.redhat.com/show_bug.cgi?id=2083376)

[1.17.0] - 2022-04-25
----------------------------

### New Features

- [All roles should support running with gather_facts: false](https://bugzilla.redhat.com/show_bug.cgi?id=2078989)
- [ha_cluster - support advanced corosync configuration](https://bugzilla.redhat.com/show_bug.cgi?id=2065337)
- [ha_cluster - support SBD fencing](https://bugzilla.redhat.com/show_bug.cgi?id=2079626)
- [ha_cluster - add support for configuring bundle resources](https://bugzilla.redhat.com/show_bug.cgi?id=2073519)
- [logging - Logging - RFE - support template, severity and facility options](https://bugzilla.redhat.com/show_bug.cgi?id=2075119)
- [metrics - consistently use ansible_managed in configuration files managed by role [rhel-9.1.0]](https://bugzilla.redhat.com/show_bug.cgi?id=2065392)
- [metrics - [RFE] add an option to the metrics role to enable postfix metric collection](https://bugzilla.redhat.com/show_bug.cgi?id=2051737)
- [network - [RFE] Extend rhel-system-roles.network feature set to support routing rules](https://bugzilla.redhat.com/show_bug.cgi?id=2079622)
- [postfix - Postfix RHEL System Role should provide the ability to replace config and reset configuration back to default [rhel-9.1.0]](https://bugzilla.redhat.com/show_bug.cgi?id=2065383)
- [storage - RFE storage Less verbosity by default](https://bugzilla.redhat.com/show_bug.cgi?id=2079627)

### Bug Fixes

- [firewall - Firewall system role Ansible deprecation warning related to "include"](https://bugzilla.redhat.com/show_bug.cgi?id=2061511)
- [kernel_settings - error configobj not found on RHEL 8.6 managed hosts](https://bugzilla.redhat.com/show_bug.cgi?id=2060525)
- [logging - tests fail during cleanup if no cloud-init on system](https://bugzilla.redhat.com/show_bug.cgi?id=2058799)
- [metrics - Metrics role, with "metrics_from_mssql" option does not configure /var/lib/pcp/pmdas/mssql/mssql.conf on first run](https://bugzilla.redhat.com/show_bug.cgi?id=2060523)
- [nbde_client - NBDE client system role does not support servers with static IP addresses [rhel-9.1.0]](https://bugzilla.redhat.com/show_bug.cgi?id=2070462)
- [network - bond: fix typo in supporting the infiniband ports in active-backup mode [rhel-9.1.0]](https://bugzilla.redhat.com/show_bug.cgi?id=2065394)
- [network - consistently use ansible_managed in configuration files managed by role [rhel-9.1.0]](https://bugzilla.redhat.com/show_bug.cgi?id=2065382)
- [postfix - consistently use ansible_managed in configuration files managed by role [rhel-9.1.0]](https://bugzilla.redhat.com/show_bug.cgi?id=2065393)
- [sshd - FIPS mode detection in SSHD role is wrong](https://bugzilla.redhat.com/show_bug.cgi?id=2073605)
- [tlog - Tlog role - Enabling session recording configuration does not work due to RHEL9 SSSD files provider default](https://bugzilla.redhat.com/show_bug.cgi?id=2071804)

[1.16.3] - 2022-04-07
----------------------------

### New Features

- none

### Bug Fixes

- [tlog - Tlog role - Enabling session recording configuration does not work due to RHEL9 SSSD files provider default](https://bugzilla.redhat.com/show_bug.cgi?id=2072749)

[1.16.2] - 2022-04-06
----------------------------

### New Features

- [nbde_client - NBDE client system role does not support servers with static IP addresses](https://bugzilla.redhat.com/show_bug.cgi?id=1985022)

### Bug Fixes

- none

[1.16.1] - 2022-03-29
----------------------------

### New Features

- [nbde_client - NBDE client system role does not support servers with static IP addresses](https://bugzilla.redhat.com/show_bug.cgi?id=1985022)

### Bug Fixes

- none

[1.16.0] - 2022-03-22
----------------------------

### New Features

- [network - consistently use ansible_managed in configuration files managed by role](https://bugzilla.redhat.com/show_bug.cgi?id=2057656)
- [metrics - consistently use ansible_managed in configuration files managed by role](https://bugzilla.redhat.com/show_bug.cgi?id=2057645)
- [postfix - consistently use ansible_managed in configuration files managed by role](https://bugzilla.redhat.com/show_bug.cgi?id=2057661)
- [postfix - Postfix RHEL System Role should provide the ability to replace config and reset configuration back to default](https://bugzilla.redhat.com/show_bug.cgi?id=2044657)

### Bug Fixes

- [network - bond: fix typo in supporting the infiniband ports in active-backup mode](https://bugzilla.redhat.com/show_bug.cgi?id=2064388)

[1.15.1] - 2022-03-03
----------------------------

### New Features

- none

### Bug Fixes

- [kernel_settings - error configobj not found on RHEL 8.6 managed hosts](https://bugzilla.redhat.com/show_bug.cgi?id=2058772)
- [timesync - timesync: basic-smoke test failure in timesync/tests_ntp.yml](https://bugzilla.redhat.com/show_bug.cgi?id=2058645)

[1.15.0] - 2022-03-01
----------------------------

### New Features

- [firewall - [RFE] - Firewall RHEL System Role should be able to set default zone](https://bugzilla.redhat.com/show_bug.cgi?id=2022458)

### Bug Fixes

- [metrics - Metrics role, with "metrics_from_mssql" option does not configure /var/lib/pcp/pmdas/mssql/mssql.conf on first run](https://bugzilla.redhat.com/show_bug.cgi?id=2058655)
- [firewall - ensure target changes take effect immediately](https://bugzilla.redhat.com/show_bug.cgi?id=2057172)

[1.14.0] - 2022-02-21
----------------------------

### New Features

- [network - [RFE] Add more bonding options to rhel-system-roles.network](https://bugzilla.redhat.com/show_bug.cgi?id=2008931)
- [certificate - should consistently use ansible_managed in hook scripts](https://bugzilla.redhat.com/show_bug.cgi?id=2054364)
- [tlog - consistently use ansible_managed in configuration files managed by role](https://bugzilla.redhat.com/show_bug.cgi?id=2054363)
- [vpn - consistently use ansible_managed in configuration files managed by role](https://bugzilla.redhat.com/show_bug.cgi?id=2054365)

### Bug Fixes

- [ha_cluster - set permissions for haclient group](https://bugzilla.redhat.com/show_bug.cgi?id=2049747)

[1.13.0] - 2022-02-14
----------------------------

### New Features

- [storage - RFE: Add support for RAID volumes (lvm-only)](https://bugzilla.redhat.com/show_bug.cgi?id=2016514)
- [storage - RFE: Add support for cached volumes (lvm-only)](https://bugzilla.redhat.com/show_bug.cgi?id=2016511)
- [nbde_client - NBDE client system role does not support servers with static IP addresses](https://bugzilla.redhat.com/show_bug.cgi?id=1985022)
- [ha_cluster - [RFE] ha_cluster - Support for creating resource constraints (Location, Ordering, etc.)](https://bugzilla.redhat.com/show_bug.cgi?id=2041635)
- [network - RFE: Support Routing Tables in static routes in Network Role](https://bugzilla.redhat.com/show_bug.cgi?id=2031521)

### Bug Fixes

- [metrics - role can't be re-run if the Grafana admin password has been changed](https://bugzilla.redhat.com/show_bug.cgi?id=1967321)
- [network - Failure to activate connection: nm-manager-error-quark: No suitable device found for this connection](https://bugzilla.redhat.com/show_bug.cgi?id=2034908)
- [network - Set DNS search setting only for enabled IP protocols](https://bugzilla.redhat.com/show_bug.cgi?id=2041627)

[1.12.1] - 2022-02-08
----------------------------

### New Features

- none

### Bug Fixes

- [vpn - vpn: template error while templating string: no filter named 'vpn_ipaddr'](https://bugzilla.redhat.com/show_bug.cgi?id=2050341)
- [kdump - kdump: Unable to start service kdump: Job for kdump.service failed because the control process exited with error code.](https://bugzilla.redhat.com/show_bug.cgi?id=2052105)

[1.12.0] - 2022-02-03
----------------------------

### New Features

- [Support ansible-core 2.11+](https://bugzilla.redhat.com/show_bug.cgi?id=2012316)

### Bug Fixes

- [logging - Logging role "logging_purge_confs" option not properly working](https://bugzilla.redhat.com/show_bug.cgi?id=2040812)
- [kernel_settings - role should use ansible_managed in its configuration file](https://bugzilla.redhat.com/show_bug.cgi?id=2047504)

[1.11.0] - 2022-01-20
----------------------------

### New Features

- [Support ansible-core 2.11+](https://bugzilla.redhat.com/show_bug.cgi?id=2012316)
- [cockpit - Please include "cockpit" role](https://bugzilla.redhat.com/show_bug.cgi?id=2021661)
- [ssh - ssh/tests_all_options.yml: "assertion": "'StdinNull yes' in config.content | b64decode ", failure](https://bugzilla.redhat.com/show_bug.cgi?id=2029614)

### Bug Fixes

- [timesync - timesync: Failure related to missing ntp/ntpd package/service on RHEL-9 host](https://bugzilla.redhat.com/show_bug.cgi?id=2029463)
- [logging - role missing quotes for immark module interval value](https://bugzilla.redhat.com/show_bug.cgi?id=2021678)
- [kdump - kdump: support reboot required and reboot ok](https://bugzilla.redhat.com/show_bug.cgi?id=2029605)
- [sshd - should detect FIPS mode and handle tasks correctly in FIPS mode](https://bugzilla.redhat.com/show_bug.cgi?id=1979714)

[1.10.0] - 2021-11-08
----------------------------

### New Features

- [cockpit - Please include "cockpit" role](https://bugzilla.redhat.com/show_bug.cgi?id=2021661)
- [firewall - Ansible Roles for RHEL Firewall](https://bugzilla.redhat.com/show_bug.cgi?id=1854988)
- [firewall - RFE: firewall-system-role: add ability to add-source](https://bugzilla.redhat.com/show_bug.cgi?id=1932678)
- [firewall - RFE: firewall-system-role: allow user defined zones](https://bugzilla.redhat.com/show_bug.cgi?id=1850768)
- [firewall - RFE: firewall-system-role: allow specifying the zone](https://bugzilla.redhat.com/show_bug.cgi?id=1850753)
- [Support ansible-core 2.11+](https://bugzilla.redhat.com/show_bug.cgi?id=2012316)
- [network - role: Allow to specify PCI address to configure profiles](https://bugzilla.redhat.com/show_bug.cgi?id=1695634)
- [network - [RFE] support wifi Enhanced Open (OWE)](https://bugzilla.redhat.com/show_bug.cgi?id=1993379)
- [network - [RFE] support WPA3 Simultaneous Authentication of Equals(SAE)](https://bugzilla.redhat.com/show_bug.cgi?id=1993311)
- [network - [Network] RFE: Support ignoring default gateway retrieved by DHCP/IPv6-RA](https://bugzilla.redhat.com/show_bug.cgi?id=1897565)
- [logging - [RFE]  logging - Add user and password](https://bugzilla.redhat.com/show_bug.cgi?id=2010327)

### Bug Fixes

- [Replace `# {{ ansible_managed }}` with `{{ ansible_managed | comment }}`](https://bugzilla.redhat.com/show_bug.cgi?id=2006230)
- [logging - role missing quotes for immark module interval value](https://bugzilla.redhat.com/show_bug.cgi?id=2021678)
- [logging - Logging - Performance improvement](https://bugzilla.redhat.com/show_bug.cgi?id=2005727)
- [nbde_client - add regenerate-all to the dracut command](https://bugzilla.redhat.com/show_bug.cgi?id=2021682)
- [certificate - certificates: "group" option keeps certificates inaccessible to the group](https://bugzilla.redhat.com/show_bug.cgi?id=2021683)

[1.9.0] - 2021-10-26
----------------------------

### New Features

- [logging - [RFE]  logging - Add user and password](https://bugzilla.redhat.com/show_bug.cgi?id=1990490)

### Bug Fixes

- [Replace `# {{ ansible_managed }}` with `{{ ansible_managed | comment }}`](https://bugzilla.redhat.com/show_bug.cgi?id=2006230)

[1.8.3] - 2021-08-26
----------------------------

### New Features

- [storage - RFE: Request that VDO be added to the Ansible (redhat-system-roles)](https://bugzilla.redhat.com/show_bug.cgi?id=1978488)

### Bug Fixes

- none

[1.8.2] - 2021-08-24
----------------------------

### New Features

- none

### Bug Fixes

- [logging - Update the certificates copy tasks](https://bugzilla.redhat.com/show_bug.cgi?id=1996777)

[1.8.1] - 2021-08-16
----------------------------

### New Features

- none

### Bug Fixes

- [metrics - role: the bpftrace role does not properly configure bpftrace agent](https://bugzilla.redhat.com/show_bug.cgi?id=1994180)

[1.8.0] - 2021-08-12
----------------------------

### New Features

- [drop support for Ansible 2.8](https://bugzilla.redhat.com/show_bug.cgi?id=1989197)

### Bug Fixes

- [sshd - sshd: failed to validate: error:Missing Match criteria for all Bad Match condition](https://bugzilla.redhat.com/show_bug.cgi?id=1991598)

[1.7.5] - 2021-08-10
----------------------------

### New Features

- [logging - [RFE] logging - Add a support for list value to server_host in the elasticsearch output](https://bugzilla.redhat.com/show_bug.cgi?id=1986460)

### Bug Fixes

- none

[1.7.4] - 2021-08-06
----------------------------

### New Features

- none

### Bug Fixes

- [metrics - role: Grafana dashboard not working after metrics role run unless services manually restarted](https://bugzilla.redhat.com/show_bug.cgi?id=1984150)

[1.7.0] - 2021-07-28
----------------------------

### New Features

- [logging - [RFE] logging - Add a support for list value to server_host in the elasticsearch output](https://bugzilla.redhat.com/show_bug.cgi?id=1986460)
- [storage - [RFE] storage: support volume sizes as a percentage of pool](https://bugzilla.redhat.com/show_bug.cgi?id=1984583)

### Bug Fixes

- none

[1.6.0] - 2021-07-15
----------------------------

### New Features

- [ha_cluster - RFE: ha_cluster - add pacemaker cluster properties configuration](https://bugzilla.redhat.com/show_bug.cgi?id=1982913)

### Bug Fixes

- none

[1.5.0] - 2021-07-15
----------------------------

### New Features

- [crypto_policies - rename 'policy modules' to 'subpolicies'](https://bugzilla.redhat.com/show_bug.cgi?id=1982896)

### Bug Fixes

- none

[1.4.2] - 2021-07-15
----------------------------

### New Features

- [storage - storage: relabel doesn't support](https://bugzilla.redhat.com/show_bug.cgi?id=1876315)

### Bug Fixes

- none

[1.4.1] - 2021-07-09
----------------------------

### New Features

- none

### Bug Fixes

- [network - Re-running the network system role results in "changed: true" when nothing has actually changed](https://bugzilla.redhat.com/show_bug.cgi?id=1980871)

[1.4.0] - 2021-07-08
----------------------------

### New Features

- [storage - RFE: Request that VDO be added to the Ansible (redhat-system-roles)](https://bugzilla.redhat.com/show_bug.cgi?id=1882475)

### Bug Fixes

- none

[1.3.0] - 2021-06-23
----------------------------

### New Features

- [storage - RFE: Request that VDO be added to the Ansible (redhat-system-roles)](https://bugzilla.redhat.com/show_bug.cgi?id=1978488)
- [sshd - RFE: sshd - support for appending a snippet to configuration file](https://bugzilla.redhat.com/show_bug.cgi?id=1978752)
- [timesync - RFE: timesync support for Network Time Security (NTS)](https://bugzilla.redhat.com/show_bug.cgi?id=1978753)

### Bug Fixes

- [postfix - Postfix RHEL system role README.md missing variables under the "Role Variables" section](https://bugzilla.redhat.com/show_bug.cgi?id=1978734)
- [postfix - the postfix role is not idempotent](https://bugzilla.redhat.com/show_bug.cgi?id=1978760)
- [selinux - task for semanage says Fedora in name but also runs on RHEL/CentOS 8](https://bugzilla.redhat.com/show_bug.cgi?id=1978740)
- [metrics - role task to enable logging for targeted hosts not working](https://bugzilla.redhat.com/show_bug.cgi?id=1978746)
- [sshd ssh - Unable to set sshd_hostkey_group and sshd_hostkey_mode](https://bugzilla.redhat.com/show_bug.cgi?id=1978745)

[1.2.3] - 2021-06-17
----------------------------

### New Features

- [main.yml: Add EL 9 support for all roles](https://bugzilla.redhat.com/show_bug.cgi?id=1952887)

### Bug Fixes

- none

[1.2.2] - 2021-06-15
----------------------------

### New Features

- none

### Bug Fixes

- [Internal links in README.md are broken](https://bugzilla.redhat.com/show_bug.cgi?id=1962976)

[1.2.1] - 2021-05-21
----------------------------

### New Features

- none

### Bug Fixes

- [Internal links in README.md are broken](https://bugzilla.redhat.com/show_bug.cgi?id=1962976)

[1.2.0] - 2021-05-21
----------------------------

### New Features

- [network - role: Support ethtool -G|--set-ring options](https://bugzilla.redhat.com/show_bug.cgi?id=1959649)

### Bug Fixes

- [postfix - the postfix role is not idempotent](https://bugzilla.redhat.com/show_bug.cgi?id=1960375)
- [postfix - postfix: Use FQRN in README](https://bugzilla.redhat.com/show_bug.cgi?id=1958963)
- [postfix - Documentation error in rhel-system-roles postfix readme file](https://bugzilla.redhat.com/show_bug.cgi?id=1866544)
- [storage - storage: calltrace observed when set type: partition for storage_pools](https://bugzilla.redhat.com/show_bug.cgi?id=1854187)
- [ha_cluster - cannot read preshared key in binary format](https://bugzilla.redhat.com/show_bug.cgi?id=1952620)

[1.1.0] - 2021-05-13
----------------------------

### New Features

- [timesync - [RFE] support for free form configuration for chrony](https://bugzilla.redhat.com/show_bug.cgi?id=1938023)
- [timesync - [RFE] support for timesync_max_distance to configure maxdistance/maxdist parameter](https://bugzilla.redhat.com/show_bug.cgi?id=1938016)
- [timesync - [RFE] support for ntp xleave, filter, and hw timestamping](https://bugzilla.redhat.com/show_bug.cgi?id=1938020)
- [selinux - [RFE] Ability to install custom SELinux module via Ansible](https://bugzilla.redhat.com/show_bug.cgi?id=1848683)
- [network - support for ipv6_disabled to disable ipv6 for address](https://bugzilla.redhat.com/show_bug.cgi?id=1939711)
- [vpn - [RFE] Release Ansible role for vpn in rhel-system-roles](https://bugzilla.redhat.com/show_bug.cgi?id=1943679)

### Bug Fixes

- [Bug fixes for Collection/Automation Hub](https://bugzilla.redhat.com/show_bug.cgi?id=1954747)
- [timesync - do not use ignore_errors in timesync role](https://bugzilla.redhat.com/show_bug.cgi?id=1938014)
- [selinux - rhel-system-roles should not reload the SELinux policy if its not changed](https://bugzilla.redhat.com/show_bug.cgi?id=1757869)

[0.6] - 2018-05-11
----------------------------

### New Features

- [RFE: Ansible rhel-system-roles.network: add ETHTOOL_OPTS, LINKDELAY, IPV4_FAILURE_FATAL](https://bugzilla.redhat.com/show_bug.cgi?id=1478576)

### Bug Fixes

- none
