#!/bin/bash
# ==============================================================================
# CSE30040 - Cloud Computing and DevOps - Experiment 5
# EC2 Provisioning & Tool Setup Script
# Installs Java 17, Jenkins, and Docker on Ubuntu 22.04 LTS
# ==============================================================================

set -e

echo ">>> [1/5] Updating package index..."
sudo apt update -y && sudo apt upgrade -y

echo ">>> [2/5] Installing OpenJDK 17..."
sudo apt install fontconfig openjdk-17-jdk -y

echo ">>> [3/5] Adding Jenkins repository and installing Jenkins..."
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update -y
sudo apt install jenkins -y
sudo systemctl start jenkins
sudo systemctl enable jenkins

echo ">>> [4/5] Installing Docker..."
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker

echo ">>> [5/5] Granting Jenkins and Ubuntu user Docker permissions..."
sudo usermod -aG docker jenkins
sudo usermod -aG docker ubuntu
sudo systemctl restart jenkins

echo "=============================================================================="
echo "Setup Complete!"
echo "Jenkins Initial Admin Password:"
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
echo "=============================================================================="
echo "Access Jenkins at: http://<EC2-PUBLIC-IP>:8080"
echo "=============================================================================="
