## ♾ Demo: Deploy and manage GitLab-CE and Jenkins CI platform by Ansible

- Note: The demo is JUST a lab practice, if you want to use in your environment, please change and test it!

- Environment required:
  - Access external internet network
  - Locate ansible-cicd-plt.tgz in `devops@foundation0.ilt.example.com:~` after creating devops user

- Project directory shownd as follow:
  ```bash
  $ tree -L 3 .
  .
  ├── 10-provision-gitlab-ce.yml
  ├── 20-provision-container-image.yml
  ├── 30-provision-tomcat-jenkins.yml
  ├── ansible.cfg
  ├── ansible-gitlab-jenkins-cicd-platform-demo.png
  ├── ansible-navigator.log
  ├── ansible-navigator.yml
  ├── collections
  │   ├── ansible_collections
  │   │   ├── community
  │   │   ├── community.general-8.5.0.info
  │   │   ├── containers
  │   │   └── containers.podman-1.15.3.info
  │   └── requirement.yml
  ├── example-pics
  │   ├── 01-automation-hub-tomcat-image.png
  │   ├── 02-gitlab-ce-devops-project.png
  │   ├── 03-jenkins-pipeline-build-deploy-container-1.png
  │   ├── 03-jenkins-pipeline-build-deploy-container-2.png
  │   ├── 03-jenkins-pipeline-build-deploy-container-3.png
  │   ├── 03-jenkins-pipeline-build-deploy-container-4.png
  │   └── 04-simpleserver-demo.png
  ├── files
  │   ├── Containerfile
  │   ├── gitlab_gitlab-ce.repo
  │   ├── gitlab.rb
  │   └── index.jsp
  ├── inventory
  ├── Jenkinsfile
  ├── packages
  │   ├── apache-tomcat-9.0.30.tar.gz
  │   ├── gitlab-ce-17.2.0-ce.0.el9.x86_64.rpm
  │   ├── harbor-offline-installer-v1.8.1.tgz
  │   ├── jdk-8u191-linux-x64.tar.gz
  │   ├── jenkins-2.204.2.war
  │   └── jenkins-plugins.tgz
  ├── README.md
  ├── secrets
  │   ├── gitlab_auth.yml
  │   └── hub_auth.yml
  └── tomcat-v1.0.0.tar

  10 directories, 31 files
  ```

- Topology for lab:

  ![ansible-gitlab-jenkins-cicd-platform-demo](ansible-gitlab-jenkins-cicd-platform-demo.png)

- Prepare devops user account and ssh authorized:
  ```bash
  @foundation0:
  ## create devops user on foundation0 node
  (kiosk) $ su - root  # type password 'Asimov'
  (root)  # useradd devops
  (root)  # echo redhat | passwd --stdin devops
  (root)  # exit
  ```
- Prepare demo material and install ansible-navigator:
  ```bash
  @foundation0:
  (kiosk) $ su - devops  # type password 'redhat'
  (devops)$ tar -zxf ansible-cicd-plt.tgz
  (devops)$ ssh-keygen
  (devops)$ ssh-copy-id devops@foundation0.ilt.example.com	# type password 'redhat'
  (devops)$ ssh-copy-id devops@servera.lab.example.com	# type password 'redhat'
  (devops)$ mkdir ~/.pip
  (devops)$ cat > ~/.pip/pip.conf <<EOF
  > [global]
  > index-url=http://mirrors.aliyun.com/pypi/simple/
  > [install]
  > trusted-host=mirrors.aliyun.com
  > EOF
  # change pip3 source index to accelerate installation
  (devops)$ pip3 install ansible-navigator --user  # JUST install in user env
  ```
  
- Prepare execution environment image:
  ```bash
  @foundation0:
  (devops)$ podman login -u admin -p redhat utility.lab.example.com --tls-verify=false
  (devops)$ podman pull utility.lab.example.com/ansible-automation-platform-22/ee-supported-rhel8:latest --tls-verify=false
  ```
- Install collections in collections directory:
  - community.general and containers.podman collection installed in collections directory
  - If previous collections is not existing, run following commands:
    ```bash
    @foundation0:
    (devops)$ cd ~/ansible-cicd-plt
    (devops)$ ansible-galaxy collection install -r collections/requirement.yml -p collections
    (devops)$ ansible-galaxy collection list
    ```
    
- GitLab CE deploy and manage:
  ```bash
  @foundation0:
  (devops)$ cd ~/ansible-cicd-plt
  (devops)$ ansible-navigator run -m stdout 10-provision-gitlab-ce.yml --list-tags  # optional: verify all tags
  (devops)$ ansible-navigator run -m stdout 10-provision-gitlab-ce.yml
  (devops)$ ansible-navigator run -m stdout 10-provision-gitlab-ce.yml --tag create_user  # optional: if create_user ERROR
  (devops)$ ansible-navigator run -m stdout 10-provision-gitlab-ce.yml --tag create_project  # optional: if create_project ERROR
  ```
  Open firefox and use devops account and password to login `http://foundation0.ilt.example.com:7000`, and you will find the project is in it.

- Tomcat container image synchronize into automation hub:
  ```bash
  @foundation0:
  (devops)$ cd ~/ansible-cicd-plt
  (devops)$ ansible-navigator run -m stdout 20-provision-container-image.yml	
  ```
  Open firefox and use admin/redhat to login automation hub, and verify tomcat image in Execution Environment.

- JDK, Tomcat and Jenkins deploy and set environment:
  ```bash
  @foundation0:
  (devops)$ cd ~/ansible-cicd-plt
  (devops)$ ansible-navigator run -m stdout 30-provision-tomcat-jenkins.yml --skip-tag config_plugins
  (devops)$ ssh devops@servera
  
  @servera:
  (devops)$ source /etc/profile && /home/devops/tomcat-jenkins/bin/startup.sh
  Using CATALINA_BASE:   /home/devops/tomcat-jenkins
  Using CATALINA_HOME:   /home/devops/tomcat-jenkins
  Using CATALINA_TMPDIR: /home/devops/tomcat-jenkins/temp
  Using JRE_HOME:        /usr/local/jdk1.8.0_191/jre
  Using CLASSPATH:       /home/devops/tomcat-jenkins/bin/bootstrap.jar:/home/devops/tomcat-jenkins/bin/tomcat-juli.jar
  Tomcat started.
  ```
  Open firefox and access `http://servera.lab.example.com:8080/jenkins` to init jenkins.

- Jenkins plugins install:
  ```bash
  @servera:
  (devops)$ /home/devops/tomcat-jenkins/bin/shutdown.sh
  
  @foundation0:
  (devops)$ cd ~/ansible-cicd-plt
  (devops)$ ansible-navigator run -m stdout 30-provision-tomcat-jenkins.yml --tag config_plugins
  
  @servera:
  (devops)$ /home/devops/tomcat-jenkins/bin/startup.sh
  ```
  Login jenkins again to verify installed plugins.

- Update code to gitlab-ce:
  ```bash
  @foundation0:
  (devops)$ cd ~/ansible-cicd-plt
  (devops)$ git clone http://foundation0.ilt.example.com:7000/devops/tomcat-jenkins-demo.git
  (devops)$ cp files/{Containerfile,index.jsp} tomcat-jenkins-demo/
  (devops)$ cd tomcat-jenkins-demo/
  (devops)$ git config --global user.email devops@lab.example.com
  (devops)$ git config --global user.name devops
  (devops)$ git add .
  (devops)$ git commit -m "First update project"
  (devops)$ git push	# user: devops, password: 1qazZSE$
  ```

- Jenkins pipeline create and start:
  - Open firefox and login jenkins.
  - Create pipeline, add scm credential, generate pipeline and so on. Follow the images in example-pics directory.		

    ![](example-pics/03-jenkins-pipeline-build-deploy-container-1.png)
    
    ![](example-pics/03-jenkins-pipeline-build-deploy-container-2.png)

    ![](example-pics/03-jenkins-pipeline-build-deploy-container-3.png)

    ![](example-pics/03-jenkins-pipeline-build-deploy-container-4.png)

  - Build pipeline to view the progress.

- Access webapp:
  - Access `http://servera.lab.example.com:8880/simpleServer/`

- References:
  - [Ansible Doc - Community.General](https://docs.ansible.com/ansible/latest/collections/community/general/index.html)
  - [Install GitLab CE on RHEL 9 | CentOS 9](https://infotechys.com/install-gitlab-ce-on-rhel-9/)
