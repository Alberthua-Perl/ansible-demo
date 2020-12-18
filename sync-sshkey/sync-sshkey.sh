#!/bin/bash
#
# Function: implement to add remote user authorized key
# Author: hualongfeiyyy@163.com
# Modified date: 2020-12-18
# Files: ansible.cfg, inventory, sync-sshkey.yml, sync-sshkey.sh
# 
# Please according to your environment to change inventory
# and variables in playbook.
#
#   Usage: 
#     1. all previous files in the same directory, 
#        e.g /home/hualf
#			2. $ chmod +x sync-sshkey.sh && ./sync-sshkey.sh
#

TARGET=$HOME/sync-sshkey
CONFIG=$HOME/ansible.cfg
HOSTS=$HOME/inventory
PLAYS=$HOME/sync-sshkey.yml

mkdir ${TARGET}
if [[ -f ${CONFIG} || -f ${HOSTS} || -f ${PLAYS} ]]; then
	mv ${CONFIG} ${HOSTS} ${PLAYS} ${TARGET} 2> /dev/null
fi

# set env variable not to check host key
export ANSIBLE_HOST_KEY_CHECKING=False

# add user ssh public key to authorized_key file
cd ${TARGET}
ansible-playbook sync-sshkey.yml

