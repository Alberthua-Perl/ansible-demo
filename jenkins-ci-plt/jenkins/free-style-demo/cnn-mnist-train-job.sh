#!/bin/bash

echo -e "\n---> Create build env..."
mkdir build/
shopt -s extglob
mv !(build) build/

echo -e "\n---> Train MNIST and generate module..."
cd build/
python ./train_mnist_model_tf.py
tree .

echo -e "\n---> Generate Containerfile..."
cd ../
cat > Containerfile <<EOF
FROM nexus3.lab.example.com:8882/tf-flask:2.18.0

ADD build/ /app
WORKDIR /app
EXPOSE 5000

ENTRYPOINT ["python", "app.py"]
EOF

echo -e "\n---> Login and pull tf-flask image..."
podman login --tls-verify=false --username devuser0 --password 1qazZSE$ nexus3.lab.example.com:8882
podman pull --tls-verify=false nexus3.lab.example.com:8882/tf-flask:2.18.0

echo -e "\n---> Build app-tf-flask app image..."
podman build -t app-tf-flask:v1.0 --format=docker .
if [[ $? -eq 0 ]]; then
  podman tag localhost/app-tf-flask:v1.0 nexus3.lab.example.com:8882/app-tf-flask:v1.0
  podman push --tls-verify=false nexus3.lab.example.com:8882/app-tf-flask:v1.0
  if [[ $? -eq 0 ]]; then
    echo -e "\n--> Remove local builded image..."
    podman rmi localhost/app-tf-flask:v1.0 nexus3.lab.example.com:8882/app-tf-flask:v1.0
  fi
else
  echo -e "\n---> [ERROR] Build failure..."
  exit 10
fi
