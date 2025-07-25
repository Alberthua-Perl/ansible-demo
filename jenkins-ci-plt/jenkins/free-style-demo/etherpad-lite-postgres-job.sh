#!/bin/bash

echo -e "\n---> Create app build env..."
mkdir build/
shopt -s extglob
mv !(build) build/ && mv .[a-zA-Z]* build/

echo -e "\n---> Show local dir structure..."
tree -L 2 .

echo -e "\n---> Test etherpad-lite-postgres app..."
cd build/
pnpm install --no-frozen-lockfile --force
pnpm run build:etherpad
[[ $? -eq 0 ]] || exit 10

echo -e "\n---> Generate app Containerfile..."
cd ../
cat > Containerfile <<EOF
FROM nexus3.lab.example.com:8882/node-pnpm:10.11.0
MAINTAINER hualongfeiyyy@163.com

RUN mkdir /app
ADD ./build /app
WORKDIR /app
RUN pnpm install --no-frozen-lockfile --force && \
    pnpm run build:etherpad

EXPOSE 9001
ENTRYPOINT ["pnpm", "run", "prod"]
EOF

echo -e "\n---> Login and pull base image..."
podman login --tls-verify=false --username devuser0 --password 1qazZSE$ nexus3.lab.example.com:8882
podman pull --tls-verify=false nexus3.lab.example.com:8882/node-pnpm:10.11.0
podman build -t etherpad-lite-postgres:v1.0 --format=docker .
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
