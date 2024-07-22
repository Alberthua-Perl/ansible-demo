# **RH294 for RHEL9 Course Demo** #

- Demo ansible configuration file and playbooks for RH294 course of RHEL 9.x.

- Course includes elements as followings:

  - Ansible Core 2.13.3

  - Ansible Navigator 3.2.0

  - Podman 4.0.2

  - `registry.redhat.io/ansible-automation-platform-22/ee-supported-rhel8:latest` container image

- Userful collections and roles url:

  - [Red Hat Certified Ansible Content Collections from the Red Hat hosted automation hub](https://console.redhat.com/)

  - [Community from Ansible Galaxy](https://galaxy.ansible.com)

- Use following command to run most playbooks:

  ```bash
  $ cd rh294-rhel9-course-demo/
  $ ansible-navigator run -m stdout chapterXX/playbook-name.yml
  # run playbook in rh294-rhel9-course-demo directory if current directory doesn't exist ansible.cfg
  ```

- References:

  - [Ansible Navigator Documentation](https://ansible.readthedocs.io/projects/navigator/)
 
  - [Running Ansible with the community EE image](https://ansible.readthedocs.io/en/latest/getting_started_ee/run_community_ee_image/)
 
  - [Ansible Community EE container image](https://github.com/orgs/ansible-community/packages)
 
  - [Running a local container registry for Execution Environments](https://forum.ansible.com/t/running-a-local-container-registry-for-execution-environments/206)
