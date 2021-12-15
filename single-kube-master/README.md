## Rapid install Kubernetes v1.22.1 by Ansible

##### Content:

- Purpose

- Environment

- Files to be changed

- Issues

- Usage

- References

##### Purpose:

- To rapid install Kubernetes cluster with single master node.
- To use `containerd` run-time and `Calico` CNI on Kubernetes cluster.

##### Environment:

- OS version: `CentOS Linux release 7.9.2009` (Core)

- Prepare one node as ansible control node and install `ansible`, `rhel-system-roles` rpm packages.

- Download the project directory and store it by regular user like `godev` user in vars/all.yml.

##### Files to be changed:

- Change arguements in following files according to your environment:
  
  - `./ansible.cfg` (Ansible config file):
    
    - remote_user
  
  - `./files/kubeadm-conf.yml` (kubeadm config file):
    
    - localAPIEndpoint.advertiseAddress
    
    - nodeRegistration.criSocket
    
    - nodeRegistration.taints
    
    - kube-proxy mode
    
    - imageRepository
    
    - KubernetesVersion
    
    - networking.podSubnet
    
    - cgroupDriver
  
  - `./kubecluster` (Ansible inventory file):
    
    - change group name and short hostname
  
  - `./vars/all.yml` (variables file):
    
    - gateway
    
    - nic
    
    - operator_user
    
    > 👉 operator_user same as remote_user of ansible.cfg
    
    - kube_master_node
    
    > 👉 Must change the arguement with the same as the master node short hostname in your inventory.

##### Issues:

- Reported errors during deploy kubernetes cluster like followings:
  
  kubeamd init master node failure, and report node not found. Because all `pause` infra images haven't been tagged `k8s.io/pause:3.5`, `kubelet` on master node can't create `sanbox`.
  
  ![](https://github.com/Alberthua-Perl/tech-docs/blob/master/images/kubeadm-init-master-error-1.jpg)
  
  ![](https://github.com/Alberthua-Perl/tech-docs/blob/master/images/kubeadm-init-master-error-2.jpg)

- `register` variable in playbook can't be use between different plays.
  
  ![](https://github.com/Alberthua-Perl/tech-docs/blob/master/images/register-var-used-between-two-plays-error.jpg)

##### Usage:

- After change all files, you can use following commands to deploy:

```bash
$ cd single-kube-master
$ chmod +x ./kani
$ ./kani
```

- project directory structure:
  
  ![](https://github.com/Alberthua-Perl/tech-docs/blob/master/images/kani-structure.jpg)
  
> Because of GitHub uploading limit, cri-containerd-cni-1.5.5-linux-amd64.tar.gz can be downloaded use [link](https://pan.baidu.com/s/1ytxDjSN0u5Tewy5rcEGWNQ), password is apdl

- Kubernetes cluster status in the project as following:
  
  ![](https://github.com/Alberthua-Perl/tech-docs/blob/master/images/kubernetes-cluster-status.jpg)
  
- Destroy Kubernetes cluster and re-install cluster, so you can run following command:
  
  ```bash
  $ ansible-playbook destroy-kube-cluster.yml
  ```  

##### References:

- [Kubernetes Docs - Bootstrapping clusters with kubeadm](https://v1-22.docs.kubernetes.io/docs/setup/production-environment/tools/kubeadm/)

- [Install Calico](https://projectcalico.docs.tigera.io/getting-started/kubernetes/self-managed-onprem/onpremises)
