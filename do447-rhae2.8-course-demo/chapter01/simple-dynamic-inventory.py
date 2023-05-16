#!/usr/bin/env python

'''
 Demo example for Ansible dynamic inventory.
 Modified by hualf on 2020-02-04.
'''

# coding=utf-8
import sys
import json

host1_ip = ['192.168.0.110']
host2_ip = ['192.168.0.112', '192.168.0.113']
host3_ip = ['192.168.0.114']
group1 = 'haproxy'
group2 = 'web'
group3 = 'mariadb'
hostdata = {group1:{"hosts":host1_ip}, group2:{"hosts":host2_ip}, group3:{"hosts":host3_ip}}
# print json.dumps(hostdata,indent=4)

if len(sys.argv) == 2 and sys.argv[1] == '--list':
    print(json.dumps(hostdata,indent=4))
elif len(sys.argv) == 3 and sys.argv[1] == '--host':
    print(json.dumps({}))
else:
    print("Requires an argument, please use --list or --host <host>")
