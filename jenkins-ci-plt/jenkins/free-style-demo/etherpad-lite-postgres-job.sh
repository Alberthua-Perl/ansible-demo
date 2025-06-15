#!/bin/bash

# 说明：
#   Jenkins 的作业存储于 /var/lib/jenkins/workspace/<job_name>/ 目录中，因此，拉取的源代码目录中的内容直接保存于此目录中。
#   因此，当前作业目录中直接保存了所有源代码文件。
echo -e "\n---> Create app build env..."
mkdir build/  #创建新目录
shopt -s extglob  #设置 shell 通配符扩展，如果不设置，那么下一步命令无法执行。
mv !(build) build/ && mv .[a-zA-Z]* build/
#将源代码文件及隐藏文件全部移入 build/ 目录中，方便之后在当前目录中创建 Containerfile 用于构建应用镜像。

echo -e "\n---> Show local dir structure..."
tree -L 2 .  #查看当前目录结构

echo -e "\n---> Test etherpad-lite-postgres app..."
cd build/
pnpm install --no-frozen-lockfile --force  #强制安装应用依赖模块，不使用 --force 选项将停滞在是否安装模块选项中。
pnpm run build:etherpad  #构建应用
[[ $? -eq 0 ]] || exit 10  #构建成功继续执行，否则错误退出。

echo -e "\n---> Generate app Containerfile..."
cd ../  #切换至源码目录外
cat > Containerfile <<EOF
FROM nexus3.lab.example.com:8882/node-pnpm:10.11.0  #此基础镜像需提前上传至 Nexus3 中
MAINTAINER hualongfeiyyy@163.com

RUN mkdir /app
ADD ./build /app  #将源码文件全部拷贝至容器镜像中
WORKDIR /app
RUN pnpm install --no-frozen-lockfile --force && \
    pnpm run build:etherpad

EXPOSE 9001  #暴露 9001 端口
ENTRYPOINT ["pnpm", "run", "prod"]  #运行应用
EOF

echo -e "\n---> Login and pull base image..."
podman login --tls-verify=false --username devuser0 --password 1qazZSE$ nexus3.lab.example.com:8882
podman pull --tls-verify=false nexus3.lab.example.com:8882/node-pnpm:10.11.0
#提前拉取镜像，如果构建时自动拉取镜像，会由于连接 Nexus3 镜像仓库的证书认证失败而导致拉取失败！
podman build -t etherpad-lite-postgres:v1.0 --format=docker .  #指定构建镜像格式执行构建
if [[ $? -eq 0 ]]; then
  podman tag localhost/etherpad-lite-postgres:v1.0 nexus3.lab.example.com:8882/etherpad-lite-postgres:v1.0
  echo -e "\n---> Push etherpad-lite-postgres app image..."
  podman push --tls-verify=false nexus3.lab.example.com:8882/etherpad-lite-postgres:v1.0
  if [[ $? -eq 0 ]]; then
		podman rmi localhost/etherpad-lite-postgres:v1.0 nexus3.lab.example.com:8882/etherpad-lite-postgres:v1.0
  fi
else
  echo -e "\n---> [ERROR] Build failure..."
  exit 10
fi
#如果构建成功，那么推送镜像，反之退出作业流程。
