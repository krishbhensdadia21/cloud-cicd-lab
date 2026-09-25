#!/bin/bash
# ==============================================================================
# CSE30040 - Cloud Computing and DevOps - Experiment 5
# Automated Setup & Deployment Script for AWS EC2 Ubuntu
# ==============================================================================

set -e

echo "=================================================================="
echo ">>> [1/6] Updating Ubuntu packages..."
echo "=================================================================="
sudo apt update -y

echo "=================================================================="
echo ">>> [2/6] Installing OpenJDK 17 (Java Runtime for Jenkins)..."
echo "=================================================================="
sudo apt install fontconfig openjdk-17-jdk git -y

echo "=================================================================="
echo ">>> [3/6] Installing Jenkins..."
echo "=================================================================="
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update -y
sudo apt install jenkins -y
sudo systemctl start jenkins
sudo systemctl enable jenkins

echo "=================================================================="
echo ">>> [4/6] Installing Docker..."
echo "=================================================================="
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker jenkins
sudo usermod -aG docker ubuntu

echo "=================================================================="
echo ">>> [5/6] Cloning Repository and Deploying Flask Application..."
echo "=================================================================="
cd /home/ubuntu
if [ -d "cloud-cicd-lab" ]; then
    cd cloud-cicd-lab && git pull origin main
else
    git clone https://github.com/krishbhensdadia21/cloud-cicd-lab.git
    cd cloud-cicd-lab
fi

# Build and run container
sudo docker build -t cloud-app .
sudo docker stop cloud-app 2>/dev/null || true
sudo docker rm cloud-app 2>/dev/null || true
sudo docker run -d --name cloud-app -p 5000:5000 cloud-app

echo "=================================================================="
echo ">>> [6/6] Verifying Running Services..."
echo "=================================================================="
sudo docker ps

PUBLIC_IP=$(curl -s http://checkip.amazonaws.com || curl -s ifconfig.me || echo "43.204.114.6")

echo ""
echo "=================================================================="
echo "🎉 DEPLOYMENT SUCCESSFUL!"
echo "=================================================================="
echo "1. Web Application Output:"
echo "   http://${PUBLIC_IP}:5000"
echo ""
echo "2. Jenkins Dashboard:"
echo "   http://${PUBLIC_IP}:8080"
echo ""
echo "3. Jenkins Initial Admin Password:"
sudo cat /var/lib/jenkins/secrets/initialAdminPassword || echo "Password file creating..."
echo "=================================================================="
