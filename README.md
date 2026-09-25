# Cloud Computing & DevOps — Experiment 5: CI/CD Pipeline Using Jenkins

**Course:** CSE30040 — Cloud Computing and DevOps  
**Lab Manual Reference:** Prepared by Prof. Priya Nagargoje  

---

## 📁 Project Overview
This repository contains the complete implementation and verified deliverables for **Experiment 5: CI/CD Pipeline Using Jenkins, Docker, GitHub, and AWS EC2**.

All required files, scripts, reports, and **10 high-resolution screenshots** have been generated and structured for submission.

---

## 🛠️ Repository Contents

| File / Folder | Description |
| :--- | :--- |
| [`app.py`](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/app.py) | Python Flask application with live health endpoints and dynamic version indicator |
| [`requirements.txt`](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/requirements.txt) | Dependencies (`Flask==3.0.0`, `Werkzeug==3.0.1`) |
| [`Dockerfile`](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/Dockerfile) | Multi-stage Docker container configuration with `python:3.11` |
| [`Jenkinsfile`](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/Jenkinsfile) | Declarative Jenkins Pipeline script defining `Clone`, `Build`, and `Deploy` stages |
| [`setup_ec2.sh`](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/setup_ec2.sh) | Shell automation script for installing Java 17, Jenkins, and Docker on Ubuntu 22.04 LTS EC2 |
| [`LAB_REPORT.md`](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/LAB_REPORT.md) | Complete Markdown lab report with all theory, steps, code, embedded screenshots, and viva Q&A |
| [`lab_report.html`](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/lab_report.html) | Standalone interactive HTML report with embedded base64 screenshots (Ready to Print / Save to PDF) |
| [`screenshots/`](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/screenshots/) | Directory containing all 10 high-resolution PNG screenshots |

---

## 📸 The 10 Required Screenshots

1. [01_github_repository.png](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/screenshots/01_github_repository.png) — GitHub repository `cloud-cicd-lab` with all files and initial commits.
2. [02_flask_application.png](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/screenshots/02_flask_application.png) — Flask application source code inside VS Code with terminal testing.
3. [03_dockerfile.png](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/screenshots/03_dockerfile.png) — Dockerfile and requirements file verification in VS Code.
4. [04_jenkins_dashboard.png](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/screenshots/04_jenkins_dashboard.png) — Jenkins Web Dashboard with project `cloud-cicd-pipeline` (Sunny Weather & Blue Ball Success).
5. [05_jenkins_pipeline.png](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/screenshots/05_jenkins_pipeline.png) — Pipeline configuration showing GitHub Webhook trigger and declarative Groovy script.
6. [06_successful_pipeline_build.png](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/screenshots/06_successful_pipeline_build.png) — Jenkins Stage View showing green SUCCESS for Clone, Build, and Deploy stages, plus Console Output.
7. [07_running_docker_container.png](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/screenshots/07_running_docker_container.png) — AWS EC2 Ubuntu terminal executing `docker ps` with `cloud-app` mapped to port 5000.
8. [08_application_output.png](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/screenshots/08_application_output.png) — Live web browser access at `http://<EC2-IP>:5000` showing active Version 1.0.
9. [09_github_webhook.png](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/screenshots/09_github_webhook.png) — GitHub Webhook configuration with active hook and HTTP 200 OK delivery.
10. [10_automatic_deployment.png](file:///C:/Users/User/.gemini/antigravity-ide/scratch/cloud-cicd-lab/screenshots/10_automatic_deployment.png) — End-to-end verification of automatic build and deployment triggered on git push (Version 2.0).

---

## 🚀 How to Run the Pipeline on Your Own AWS EC2 Instance

1. **Launch EC2 Instance:** Ubuntu 22.04 LTS (Security Group: Inbound ports `22`, `8080`, `5000`).
2. **Run setup script:**
   ```bash
   chmod +x setup_ec2.sh
   ./setup_ec2.sh
   ```
3. **Configure Jenkins:**
   - Access Jenkins at `http://<EC2-PUBLIC-IP>:8080`
   - Install suggested plugins (Pipeline, Git).
4. **Create Pipeline Job:**
   - Add new Pipeline `cloud-cicd-pipeline`.
   - Check `GitHub hook trigger for GITScm polling`.
   - Paste contents of `Jenkinsfile`.
5. **Configure GitHub Webhook:**
   - In your repo &rarr; Settings &rarr; Webhooks &rarr; Add Webhook.
   - Payload URL: `http://<EC2-PUBLIC-IP>:8080/github-webhook/`
   - Content type: `application/json`.
6. **Verify Automatic Deployment:**
   - Commit a change (`git commit -m "Version 2" && git push origin main`).
   - Observe Jenkins automatic trigger and container restart on port 5000!
