from flask import Flask, render_template_string
import socket
import os

app = Flask(__name__)

# HTML Template for Web Application
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cloud DevOps Lab - Flask Application</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: #f8fafc;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: rgba(30, 41, 59, 0.95);
            border: 1px solid #334155;
            border-radius: 16px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
            max-width: 650px;
            width: 100%;
            padding: 40px;
            text-align: center;
        }
        .header-tag {
            background: rgba(56, 189, 248, 0.15);
            color: #38bdf8;
            font-size: 13px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            padding: 6px 14px;
            border-radius: 20px;
            display: inline-block;
            margin-bottom: 20px;
            border: 1px solid rgba(56, 189, 248, 0.3);
        }
        h1 {
            font-size: 28px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 12px;
        }
        p.subtitle {
            font-size: 16px;
            color: #94a3b8;
            margin-bottom: 25px;
            line-height: 1.5;
        }
        .version-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #10b981;
            color: #ffffff;
            padding: 8px 20px;
            border-radius: 30px;
            font-weight: 600;
            font-size: 15px;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
            margin-bottom: 30px;
        }
        .version-pulse {
            width: 10px;
            height: 10px;
            background: #ffffff;
            border-radius: 50%;
            display: inline-block;
        }
        .grid-info {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            text-align: left;
            margin-bottom: 30px;
        }
        .info-card {
            background: #0f172a;
            border: 1px solid #1e293b;
            padding: 15px;
            border-radius: 10px;
        }
        .info-card .label {
            font-size: 11px;
            text-transform: uppercase;
            color: #64748b;
            font-weight: 600;
            letter-spacing: 0.5px;
            margin-bottom: 4px;
        }
        .info-card .value {
            font-size: 14px;
            color: #e2e8f0;
            font-weight: 500;
            font-family: monospace;
        }
        .pipeline-flow {
            background: #0f172a;
            border: 1px dashed #334155;
            border-radius: 10px;
            padding: 15px;
            display: flex;
            justify-content: space-around;
            align-items: center;
            font-size: 13px;
            color: #cbd5e1;
        }
        .flow-step {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
        }
        .flow-step span.icon { font-size: 20px; }
        .flow-arrow { color: #64748b; font-size: 16px; font-weight: bold; }
        footer {
            margin-top: 25px;
            font-size: 12px;
            color: #64748b;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header-tag">CSE30040 DevOps Lab &bull; Exp 5</div>
        <h1>🚀 Welcome to Cloud CI/CD Lab!</h1>
        <p class="subtitle">Continuous Integration & Continuous Deployment Pipeline using GitHub, Jenkins, Docker, and AWS EC2.</p>
        
        <div class="version-badge">
            <span class="version-pulse"></span>
            Version {{ version }} - Automated Deployment Active
        </div>

        <div class="grid-info">
            <div class="info-card">
                <div class="label">Container Hostname</div>
                <div class="value">{{ hostname }}</div>
            </div>
            <div class="info-card">
                <div class="label">Target Port</div>
                <div class="value">0.0.0.0:5000</div>
            </div>
            <div class="info-card">
                <div class="label">Cloud Server</div>
                <div class="value">AWS EC2 Ubuntu 22.04</div>
            </div>
            <div class="info-card">
                <div class="label">Build Orchestrator</div>
                <div class="value">Jenkins Automation</div>
            </div>
        </div>

        <div class="pipeline-flow">
            <div class="flow-step"><span class="icon">🐙</span><span>GitHub Push</span></div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step"><span class="icon">🔔</span><span>Webhook</span></div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step"><span class="icon">⚙️</span><span>Jenkins</span></div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step"><span class="icon">🐳</span><span>Docker Container</span></div>
        </div>

        <footer>
            Prepared for Cloud Computing and DevOps Lab Evaluation
        </footer>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    hostname = socket.gethostname()
    version = os.environ.get("APP_VERSION", "1.0")
    return render_template_string(HTML_TEMPLATE, hostname=hostname, version=version)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
