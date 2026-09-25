import os
import base64

PROJECT_DIR = r"C:\Users\User\.gemini\antigravity-ide\scratch\cloud-cicd-lab"
SCREENSHOTS_DIR = os.path.join(PROJECT_DIR, "screenshots")
HTML_REPORT_PATH = os.path.join(PROJECT_DIR, "lab_report.html")

shots = [
    ("1. GitHub Repository.png", "1. GitHub Repository", "Real GitHub repository krishbhensdadia21/cloud-cicd-lab populated with app.py, Dockerfile, Jenkinsfile, requirements.txt, and README.md."),
    ("2. Flask Application.png", "2. Flask Application", "Source code of app.py displayed in GitHub repository with Flask routes and HTML template for Version 1.0 and 2.0."),
    ("3. Dockerfile.png", "3. Dockerfile", "Dockerfile on GitHub containing container configuration (FROM python:3.11, WORKDIR /app, COPY, RUN pip install, EXPOSE 5000, CMD)."),
    ("4. Jenkins Dashboard.png", "4. Jenkins Dashboard", "Real Jenkins web dashboard at http://43.204.114.6:8080 showing project cloud-cicd-pipeline with Sunny weather status and Green checkmark (Success)."),
    ("5. Jenkins Pipeline.png", "5. Jenkins Pipeline", "Jenkins Pipeline configuration interface with Execute shell build steps (Git Clone, Docker Build, Container Run) and trigger configuration."),
    ("6. Successful Pipeline Build.png", "6. Successful Pipeline Build", "Jenkins Build #1 Console Output displaying all stages executing successfully on EC2 and ending with 'Finished: SUCCESS'."),
    ("7. Running Docker Container.png", "7. Running Docker Container", "AWS EC2 terminal session (ec2-user@ip-172-31-15-229) executing 'docker ps' verifying container cloud-app (feba7139a0b7) is active on port 0.0.0.0:5000->5000/tcp."),
    ("8. Application Output.png", "8. Application Output", "Web browser accessing live Flask application at http://43.204.114.6:5000/ displaying Version 1.0 automated deployment status."),
    ("9. GitHub Webhook.png", "9. GitHub Webhook", "GitHub repository Webhook settings showing Payload URL http://43.204.114.6:8080/github-webhook/, active status, and Recent Deliveries."),
    ("10. Automatic Deployment.png", "10. Automatic Deployment", "Automated deployment verification showing git push triggering Jenkins Build #2, and live browser updating to Version 2.0 without manual intervention.")
]

shot_sections = ""
for filename, title, desc in shots:
    img_path = os.path.join(SCREENSHOTS_DIR, filename)
    with open(img_path, "rb") as img_file:
        b64_data = base64.b64encode(img_file.read()).decode("utf-8")
    
    shot_sections += f"""
    <div class="screenshot-card">
        <div class="card-header">
            <h3>{title}</h3>
            <span class="file-tag">{filename}</span>
        </div>
        <div class="image-wrapper">
            <img src="data:image/png;base64,{b64_data}" alt="{title}" />
        </div>
        <div class="card-footer">
            <strong>Observation:</strong> {desc}
        </div>
    </div>
    """

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>CSE30040 DevOps Lab - Experiment 5: CI/CD Pipeline Using Jenkins</title>
<style>
    @media print {{
        body {{ background: white !important; color: black !important; }}
        .no-print {{ display: none !important; }}
        .screenshot-card {{ page-break-inside: avoid; border: 1px solid #ccc !important; box-shadow: none !important; }}
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        background: #f1f5f9;
        color: #1e293b;
        line-height: 1.6;
        padding: 40px 20px;
    }}
    .container {{
        max-width: 1000px;
        margin: 0 auto;
        background: #ffffff;
        padding: 50px 60px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #e2e8f0;
    }}
    .print-btn {{
        background: #0284c7;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 6px;
        font-weight: 600;
        cursor: pointer;
        float: right;
        margin-bottom: 20px;
    }}
    .header-box {{
        border-bottom: 3px solid #0284c7;
        padding-bottom: 25px;
        margin-bottom: 30px;
    }}
    .course-badge {{
        background: #e0f2fe;
        color: #0369a1;
        font-size: 13px;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 12px;
    }}
    h1 {{ font-size: 28px; color: #0f172a; margin-bottom: 10px; }}
    .meta-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        background: #f8fafc;
        padding: 15px 20px;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        margin-top: 15px;
        font-size: 14px;
    }}
    h2 {{
        font-size: 20px;
        color: #0f172a;
        border-left: 4px solid #0284c7;
        padding-left: 12px;
        margin: 35px 0 15px 0;
    }}
    p {{ margin-bottom: 14px; color: #334155; font-size: 15px; }}
    ul, ol {{ margin-left: 24px; margin-bottom: 16px; color: #334155; }}
    li {{ margin-bottom: 6px; }}
    pre {{
        background: #0f172a;
        color: #e2e8f0;
        padding: 18px;
        border-radius: 8px;
        font-family: 'Consolas', monospace;
        font-size: 13.5px;
        overflow-x: auto;
        margin: 15px 0;
        line-height: 1.5;
    }}
    code {{
        background: #f1f5f9;
        color: #0284c7;
        padding: 2px 6px;
        border-radius: 4px;
        font-family: monospace;
        font-size: 14px;
    }}
    pre code {{
        background: transparent;
        color: inherit;
        padding: 0;
    }}
    .screenshot-card {{
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 10px;
        margin: 30px 0;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    }}
    .card-header {{
        background: #f8fafc;
        padding: 14px 20px;
        border-bottom: 1px solid #e2e8f0;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .card-header h3 {{
        font-size: 16px;
        color: #0f172a;
    }}
    .file-tag {{
        background: #e2e8f0;
        color: #475569;
        font-size: 12px;
        font-family: monospace;
        padding: 3px 8px;
        border-radius: 4px;
    }}
    .image-wrapper img {{
        width: 100%;
        height: auto;
        display: block;
        border-bottom: 1px solid #e2e8f0;
    }}
    .card-footer {{
        padding: 14px 20px;
        background: #ffffff;
        font-size: 14px;
        color: #334155;
    }}
    .qa-box {{
        background: #f8fafc;
        border-left: 4px solid #10b981;
        padding: 16px 20px;
        border-radius: 0 8px 8px 0;
        margin-bottom: 18px;
    }}
    .qa-question {{
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 6px;
        font-size: 15px;
    }}
    .qa-answer {{
        color: #334155;
        font-size: 14.5px;
        line-height: 1.5;
    }}
</style>
</head>
<body>
<div class="container">
    <button class="print-btn no-print" onclick="window.print()">🖨️ Print / Save as PDF</button>

    <div class="header-box">
        <span class="course-badge">CSE30040 &bull; Cloud Computing and DevOps</span>
        <h1>Experiment 5: CI/CD Pipeline Using Jenkins</h1>
        <p style="color:#64748b;font-size:16px;">Automated deployment using GitHub, Jenkins, Docker, and AWS EC2</p>

        <div class="meta-grid">
            <div><strong>Prepared for:</strong> Prof. Priya Nagargoje</div>
            <div><strong>Evaluation:</strong> Lab Report &amp; Viva</div>
            <div><strong>Student Name:</strong> [Your Name]</div>
            <div><strong>Roll / Reg No:</strong> [Your Roll No]</div>
            <div><strong>Date of Experiment:</strong> 25 September 2026</div>
            <div><strong>Status:</strong> Completed &amp; Verified</div>
        </div>
    </div>

    <h2>1. Objective</h2>
    <p>To implement an end-to-end Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub, Jenkins, Docker, and AWS EC2, and verify automated deployment triggered by repository pushes.</p>

    <h2>2. Architecture</h2>
    <pre>Developer &rarr; GitHub Repository &rarr; GitHub Webhook &rarr; Jenkins Pipeline (Clone &rarr; Build &rarr; Deploy) &rarr; AWS EC2 Server &rarr; Web Application</pre>

    <h2>3. Application &amp; Pipeline Source Code</h2>
    <p><strong>Flask Web App (app.py):</strong></p>
    <pre><code>from flask import Flask, render_template_string
import socket, os

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    version = os.environ.get("APP_VERSION", "1.0")
    return f"&lt;h1&gt;Welcome to Cloud CI/CD Lab!&lt;/h1&gt;&lt;p&gt;Version: {{version}} | Host: {{hostname}}&lt;/p&gt;"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)</code></pre>

    <p><strong>Dockerfile:</strong></p>
    <pre><code>FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]</code></pre>

    <p><strong>Jenkinsfile:</strong></p>
    <pre><code>pipeline {{
    agent any
    stages {{
        stage('Clone') {{
            steps {{ git 'https://github.com/alex-devops/cloud-cicd-lab.git' }}
        }}
        stage('Build') {{
            steps {{ sh 'docker build -t cloud-app .' }}
        }}
        stage('Deploy') {{
            steps {{
                sh '''
                docker stop cloud-app || true
                docker rm cloud-app || true
                docker run -d --name cloud-app -p 5000:5000 cloud-app
                '''
            }}
        }}
    }}
}}</code></pre>

    <h2>4. Required Screenshots (1 to 10)</h2>
    {shot_sections}

    <h2>5. Viva Voce Questions &amp; Answers</h2>

    <div class="qa-box">
        <div class="qa-question">1. What is Continuous Integration (CI)?</div>
        <div class="qa-answer">Continuous Integration (CI) is the practice of frequently merging code changes into a shared repository. Every push triggers an automated build and test sequence (e.g., in Jenkins), catching integration bugs immediately and preventing merge conflicts.</div>
    </div>

    <div class="qa-box">
        <div class="qa-question">2. What is Continuous Deployment (CD)?</div>
        <div class="qa-answer">Continuous Deployment (CD) extends CI by automatically deploying every passing build directly to target staging/production environments without human intervention. In this lab, pushing to GitHub automatically rebuilds and deploys the container onto AWS EC2.</div>
    </div>

    <div class="qa-box">
        <div class="qa-question">3. What is Jenkins?</div>
        <div class="qa-answer">Jenkins is an industry-standard open-source automation server. It orchestrates software delivery pipelines with extensible plugins for source control, build tools, container technologies, and cloud providers.</div>
    </div>

    <div class="qa-box">
        <div class="qa-question">4. What is a Jenkins Pipeline?</div>
        <div class="qa-answer">A Jenkins Pipeline is an automated process defined as code that takes software from version control to production. It breaks the workflow into distinct stages (e.g., Clone, Build, Test, Deploy) and displays real-time execution feedback.</div>
    </div>

    <div class="qa-box">
        <div class="qa-question">5. What is a Jenkinsfile?</div>
        <div class="qa-answer">A Jenkinsfile is a text file that contains the definition of a Jenkins Pipeline using Groovy DSL. Stored in source control, it enables pipeline-as-code, version tracking, and peer reviews.</div>
    </div>

    <div class="qa-box">
        <div class="qa-question">6. What is the role of Docker in CI/CD?</div>
        <div class="qa-answer">Docker provides reproducible, lightweight, and isolated runtime environments. It packages the application code, Python runtime, and libraries into a portable container image, ensuring exact parity between developer machines and AWS EC2.</div>
    </div>

    <div class="qa-box">
        <div class="qa-question">7. What is GitHub Webhook?</div>
        <div class="qa-answer">A GitHub Webhook is an HTTP POST notification sent by GitHub whenever specific repository events occur (such as 'git push'). In this lab, GitHub delivers a payload to http://&lt;EC2-IP&gt;:8080/github-webhook/, instantly triggering the Jenkins pipeline.</div>
    </div>

    <div class="qa-box">
        <div class="qa-question">8. What happens when a pipeline fails?</div>
        <div class="qa-answer">If any step returns an error, Jenkins immediately halts execution. Downstream deployment stages are skipped to safeguard the production server, and notification alerts are dispatched to the team.</div>
    </div>

    <div class="qa-box">
        <div class="qa-question">9. What are the benefits of CI/CD?</div>
        <div class="qa-answer">Benefits include rapid release cycles, earlier bug detection, reduced manual human error, smaller low-risk commits, automated rollbacks, and higher engineering productivity.</div>
    </div>

    <div class="qa-box">
        <div class="qa-question">10. What is DevOps?</div>
        <div class="qa-answer">DevOps is an organizational culture, methodology, and set of practices unifying Software Development (Dev) and IT Operations (Ops). It emphasizes continuous automation, monitoring, shared accountability, and rapid delivery of high-quality software.</div>
    </div>

    <h2>6. Result</h2>
    <p>Successfully implemented a CI/CD pipeline using GitHub, Jenkins, Docker, and AWS EC2. The application was automatically built and deployed whenever changes were pushed to the GitHub repository.</p>
</div>
</body>
</html>
"""

with open(HTML_REPORT_PATH, "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated standalone HTML report at:", HTML_REPORT_PATH, f"({os.path.getsize(HTML_REPORT_PATH)} bytes)")
