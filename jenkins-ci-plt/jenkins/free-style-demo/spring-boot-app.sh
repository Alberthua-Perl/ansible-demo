#!/bin/bash

echo -e "\n---> Create build env..."
mkdir build/
shopt -s extglob
mv !(build) build/ && mv .[a-zA-Z]* build/

echo -e "\n---> Install mvn modules..."
cd build/
export PATH=$PATH:/usr/local/apache-maven-3.9.9/bin
mvn clean install -DskipTest

echo -e "\n---> Test spring app..."
mvn test

echo -e "\n---> Generate Containerfile..."
cd ../
cat > Containerfile <<EOF
FROM nexus3.lab.example.com:8882/openjdk:17-jdk-alpine
MAINTAINER hualongfeiyyy@163.com

RUN mkdir /app
ADD ./build/target/spring-boot-helloworld-0.9.6-SNAPSHOT.jar /app

WORKDIR /app

EXPOSE 8080

ENTRYPOINT ["sh", "-c", "/opt/openjdk-17/bin/java -jar spring-boot-helloworld-0.9.6-SNAPSHOT.jar --server.port=80"]
EOF

echo -e "\n---> Login and pull base image..."
podman login --tls-verify=false --username devuser0 --password 1qazZSE$ nexus3.lab.example.com:8882
podman pull --tls-verify=false nexus3.lab.example.com:8882/openjdk:17-jdk-alpine

echo -e "\n---> Build spring app image..."
podman build -t spring-boot-app:v1.0 --format=docker .
if [[ $? -eq 0 ]]; then
  podman tag localhost/spring-boot-app:v1.0 nexus3.lab.example.com:8882/spring-boot-app:v1.0
  echo -e "\n---> Push spring app image..."
  podman push --tls-verify=false nexus3.lab.example.com:8882/spring-boot-app:v1.0
  if [[ $? -eq 0 ]]; then
    echo -e "\n--> Remove local builded image..."
    podman rmi localhost/spring-boot-app:v1.0 nexus3.lab.example.com:8882/spring-boot-app:v1.0
  fi
else
  echo -e "\n---> [ERROR] Build failure..."
fi
