#!/bin/bash

echo -e "\n---> Copy motd file for ssh login..."
sudo cp ../files/jenkins-ci-plt /etc/motd.d/

echo -e "\n---> Prepare scm and artifact node..."
ansible-navigator run ./deploy-prep.yml
