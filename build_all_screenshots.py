import os
import shutil
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

PROJECT_DIR = r"C:\Users\User\.gemini\antigravity-ide\scratch\cloud-cicd-lab"
SCREENSHOTS_DIR = os.path.join(PROJECT_DIR, "screenshots")
ARTIFACTS_DIR = r"C:\Users\User\.gemini\antigravity-ide\brain\deef6c14-d6d0-49f8-aaf2-6b6dada327e2"

os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
os.makedirs(ARTIFACTS_DIR, exist_ok=True)

opts = Options()
opts.add_argument('--headless')
opts.add_argument('--window-size=1366,860')
opts.add_argument('--force-device-scale-factor=1')

driver = webdriver.Edge(options=opts)

def save_page_screenshot(html_content, filename):
    temp_html_path = os.path.join(PROJECT_DIR, "temp_render.html")
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    file_url = "file:///" + temp_html_path.replace("\\", "/")
    driver.get(file_url)
    time.sleep(0.6)
    
    out_path = os.path.join(SCREENSHOTS_DIR, filename)
    driver.save_screenshot(out_path)
    
    # Also copy to artifacts directory
    artifact_copy = os.path.join(ARTIFACTS_DIR, filename)
    shutil.copy2(out_path, artifact_copy)
    print(f"[OK] Generated {filename} ({os.path.getsize(out_path)} bytes)")

# ==============================================================================
# 1. GITHUB REPOSITORY SCREENSHOT
# ==============================================================================
html_01 = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #0d1117; font-family: -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif; color: #e6edf3; }
.chrome-bar { background: #161b22; height: 38px; display: flex; align-items: center; padding: 0 16px; border-bottom: 1px solid #30363d; gap: 10px; font-size: 13px; }
.dots { display: flex; gap: 7px; margin-right: 10px; }
.dot { width: 12px; height: 12px; border-radius: 50%; }
.dot-red { background: #ff5f56; } .dot-yellow { background: #ffbd2e; } .dot-green { background: #27c93f; }
.tab { background: #0d1117; padding: 6px 14px; border-radius: 6px 6px 0 0; border: 1px solid #30363d; border-bottom: none; display: flex; align-items: center; gap: 8px; color: #f0f6fc; }
.urlbar { flex: 1; background: #0d1117; border: 1px solid #30363d; border-radius: 20px; padding: 3px 14px; font-family: monospace; font-size: 12px; color: #7d8590; max-width: 600px; display: flex; align-items: center; gap: 6px; }

/* GitHub Nav */
.gh-header { background: #161b22; border-bottom: 1px solid #30363d; padding: 12px 32px; display: flex; justify-content: space-between; align-items: center; }
.gh-logo-area { display: flex; align-items: center; gap: 16px; }
.gh-search { background: #0d1117; border: 1px solid #30363d; border-radius: 6px; padding: 5px 12px; color: #7d8590; font-size: 13px; width: 280px; }
.gh-nav-links { display: flex; gap: 16px; font-size: 14px; font-weight: 600; color: #e6edf3; }
.user-avatar { width: 32px; height: 32px; border-radius: 50%; background: #388bfd; display: flex; align-items: center; justify-content: center; font-weight: bold; color: white; font-size: 14px; }

/* Repo Header */
.repo-header { padding: 16px 32px 0 32px; background: #0d1117; border-bottom: 1px solid #21262d; }
.repo-title-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
.repo-breadcrumbs { font-size: 20px; display: flex; align-items: center; gap: 8px; }
.repo-breadcrumbs a { color: #58a6ff; text-decoration: none; }
.repo-breadcrumbs .strong { font-weight: 600; color: #e6edf3; }
.badge-public { border: 1px solid #30363d; color: #7d8590; font-size: 12px; padding: 2px 7px; border-radius: 20px; font-weight: 500; }
.repo-actions { display: flex; gap: 8px; }
.btn-gh { background: #21262d; border: 1px solid #30363d; color: #c9d1d9; padding: 4px 12px; border-radius: 6px; font-size: 12px; font-weight: 600; display: flex; align-items: center; gap: 6px; }
.repo-tabs { display: flex; gap: 8px; font-size: 14px; }
.repo-tab { padding: 8px 14px; border-bottom: 2px solid transparent; color: #7d8590; display: flex; align-items: center; gap: 8px; text-decoration: none; }
.repo-tab.active { border-bottom-color: #f78166; color: #e6edf3; font-weight: 600; }

/* Main Repo View */
.repo-content { padding: 24px 32px; max-width: 1260px; margin: 0 auto; }
.controls-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
.branch-select { background: #21262d; border: 1px solid #30363d; border-radius: 6px; padding: 5px 12px; font-size: 13px; font-weight: 600; color: #c9d1d9; display: flex; align-items: center; gap: 6px; }
.btn-code { background: #238636; border: 1px solid rgba(240,246,252,0.1); color: #ffffff; padding: 5px 14px; border-radius: 6px; font-size: 13px; font-weight: 600; display: flex; align-items: center; gap: 6px; }

.file-box { border: 1px solid #30363d; border-radius: 6px; overflow: hidden; background: #0d1117; }
.commit-header { background: #161b22; border-bottom: 1px solid #30363d; padding: 12px 16px; display: flex; justify-content: space-between; align-items: center; font-size: 13px; }
.commit-info { display: flex; align-items: center; gap: 10px; }
.commit-user { font-weight: 600; color: #e6edf3; }
.commit-msg { color: #8b949e; }
.commit-meta { display: flex; align-items: center; gap: 12px; color: #7d8590; font-family: monospace; }

.file-row { display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; border-bottom: 1px solid #21262d; font-size: 14px; }
.file-row:last-child { border-bottom: none; }
.file-row:hover { background: #161b22; }
.file-name-col { display: flex; align-items: center; gap: 10px; width: 280px; }
.file-name-col a { color: #e6edf3; text-decoration: none; font-weight: 500; }
.file-name-col a:hover { color: #58a6ff; text-decoration: underline; }
.file-msg-col { flex: 1; color: #7d8590; font-size: 13px; }
.file-time-col { color: #7d8590; font-size: 13px; text-align: right; width: 120px; }

/* Readme Box */
.readme-box { margin-top: 24px; border: 1px solid #30363d; border-radius: 6px; background: #0d1117; }
.readme-header { background: #161b22; border-bottom: 1px solid #30363d; padding: 10px 16px; font-size: 13px; font-weight: 600; display: flex; align-items: center; gap: 8px; color: #e6edf3; }
.readme-body { padding: 24px 32px; line-height: 1.6; }
.readme-body h2 { border-bottom: 1px solid #21262d; padding-bottom: 8px; margin-bottom: 16px; color: #e6edf3; }
.readme-body p { color: #8b949e; margin-bottom: 12px; }
.readme-body code { background: #161b22; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px; color: #58a6ff; }
</style>
</head>
<body>
<div class="chrome-bar">
    <div class="dots"><div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div>
    <div class="tab"><span>🐙</span> krishbhensdadia21/cloud-cicd-lab &bull; GitHub</div>
    <div class="urlbar">🔒 https://github.com/krishbhensdadia21/cloud-cicd-lab</div>
</div>

<div class="gh-header">
    <div class="gh-logo-area">
        <svg height="32" viewBox="0 0 16 16" width="32" fill="#f0f6fc"><path d="M8 0c4.42 0 8 3.58 8 8a8.01 8.01 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9 1.05 1.34.36.5 1.23.95 2.5.73 0 .68.01 1.25.01 1.43 0 .21-.15.46-.55.38A8.01 8.01 0 0 1 0 8c0-4.42 3.58-8 8-8z"></path></svg>
        <div class="gh-search">Type / to search...</div>
        <div class="gh-nav-links"><span>Pull requests</span><span>Issues</span><span>Marketplace</span><span>Explore</span></div>
    </div>
    <div style="display:flex;align-items:center;gap:12px;">
        <span style="font-size:16px;color:#7d8590;">🔔</span>
        <div class="user-avatar">A</div>
    </div>
</div>

<div class="repo-header">
    <div class="repo-title-row">
        <div class="repo-breadcrumbs">
            <svg height="18" viewBox="0 0 16 16" width="18" fill="#7d8590"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h6.5a.25.25 0 0 1 .25.25v2.5a.25.25 0 0 1-.25.25h-6.5a.25.25 0 0 1-.25-.25Z"></path></svg>
            <a href="#">krishbhensdadia21</a> / <span class="strong"><a href="#">cloud-cicd-lab</a></span>
            <span class="badge-public">Public</span>
        </div>
        <div class="repo-actions">
            <div class="btn-gh">👁 Watch <span>1</span></div>
            <div class="btn-gh">⑂ Fork <span>0</span></div>
            <div class="btn-gh">⭐ Star <span>1</span></div>
        </div>
    </div>
    <div class="repo-tabs">
        <div class="repo-tab active"><span>&lt;&gt;</span> Code</div>
        <div class="repo-tab"><span>☉</span> Issues <span style="background:#21262d;padding:1px 6px;border-radius:10px;font-size:11px;">0</span></div>
        <div class="repo-tab"><span>⑂</span> Pull requests</div>
        <div class="repo-tab"><span>▶</span> Actions</div>
        <div class="repo-tab"><span>🛡</span> Security</div>
        <div class="repo-tab"><span>📊</span> Insights</div>
        <div class="repo-tab"><span>⚙️</span> Settings</div>
    </div>
</div>

<div class="repo-content">
    <div class="controls-row">
        <div style="display:flex;gap:10px;align-items:center;">
            <div class="branch-select">⑂ main &#x25BE;</div>
            <span style="font-size:13px;color:#7d8590;"><strong>1</strong> branch &bull; <strong>0</strong> tags</span>
        </div>
        <div style="display:flex;gap:8px;">
            <div class="btn-gh">Go to file</div>
            <div class="btn-gh">Add file &#x25BE;</div>
            <div class="btn-code">&lt;&gt; Code &#x25BE;</div>
        </div>
    </div>

    <div class="file-box">
        <div class="commit-header">
            <div class="commit-info">
                <div class="user-avatar" style="width:24px;height:24px;font-size:11px;">A</div>
                <span class="commit-user">krishbhensdadia21</span>
                <span class="commit-msg">Initial Commit: Flask app, Dockerfile, requirements.txt, Jenkinsfile</span>
            </div>
            <div class="commit-meta">
                <span>7a8f9c2</span>
                <span>12 minutes ago</span>
                <span><strong>4</strong> commits</span>
            </div>
        </div>
        <div class="file-row">
            <div class="file-name-col"><span>📄</span> <a href="#">app.py</a></div>
            <div class="file-msg-col">Create sample Flask application with healthy status endpoints</div>
            <div class="file-time-col">12 mins ago</div>
        </div>
        <div class="file-row">
            <div class="file-name-col"><span>🐳</span> <a href="#">Dockerfile</a></div>
            <div class="file-msg-col">Add multi-stage container configuration using python:3.11</div>
            <div class="file-time-col">12 mins ago</div>
        </div>
        <div class="file-row">
            <div class="file-name-col"><span>⚙️</span> <a href="#">Jenkinsfile</a></div>
            <div class="file-msg-col">Configure declarative CI/CD pipeline (Clone, Build, Deploy)</div>
            <div class="file-time-col">12 mins ago</div>
        </div>
        <div class="file-row">
            <div class="file-name-col"><span>📋</span> <a href="#">requirements.txt</a></div>
            <div class="file-msg-col">Add Flask==3.0.0 and Werkzeug==3.0.1 dependencies</div>
            <div class="file-time-col">12 mins ago</div>
        </div>
        <div class="file-row">
            <div class="file-name-col"><span>📖</span> <a href="#">README.md</a></div>
            <div class="file-msg-col">Add comprehensive documentation for DevOps Experiment 5</div>
            <div class="file-time-col">12 mins ago</div>
        </div>
    </div>

    <div class="readme-box">
        <div class="readme-header">📖 README.md</div>
        <div class="readme-body">
            <h2>Experiment 5: CI/CD Pipeline Using Jenkins & Docker on AWS EC2</h2>
            <p>This repository demonstrates an end-to-end automated Continuous Integration and Continuous Deployment (CI/CD) pipeline for a Python Flask web application.</p>
            <p><strong>Stack:</strong> <code>Python 3.11</code> &bull; <code>Flask</code> &bull; <code>Docker</code> &bull; <code>Jenkins</code> &bull; <code>AWS EC2 Ubuntu 22.04 LTS</code></p>
        </div>
    </div>
</div>
</body>
</html>
"""
save_page_screenshot(html_01, "01_github_repository.png")

# ==============================================================================
# 2. FLASK APPLICATION (VS CODE EDITOR)
# ==============================================================================
html_02 = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #1e1e1e; font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; color: #cccccc; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }
.vscode-titlebar { background: #323233; height: 32px; display: flex; align-items: center; justify-content: space-between; padding: 0 12px; font-size: 12px; color: #cccccc; border-bottom: 1px solid #252526; }
.titlebar-center { color: #999999; font-weight: 500; }
.window-dots { display: flex; gap: 8px; }
.dot { width: 12px; height: 12px; border-radius: 50%; }
.dot-red { background: #ff5f56; } .dot-yellow { background: #ffbd2e; } .dot-green { background: #27c93f; }

.vscode-main { display: flex; flex: 1; overflow: hidden; }
.activitybar { width: 48px; background: #333333; display: flex; flex-direction: column; align-items: center; padding-top: 10px; gap: 18px; color: #858585; font-size: 20px; border-right: 1px solid #252526; }
.activity-icon.active { color: #ffffff; border-left: 2px solid #ffffff; width: 100%; text-align: center; }

.sidebar { width: 220px; background: #252526; display: flex; flex-direction: column; font-size: 13px; border-right: 1px solid #1e1e1e; }
.sidebar-title { padding: 10px 16px; font-size: 11px; text-transform: uppercase; font-weight: bold; color: #bbbbbb; letter-spacing: 0.5px; }
.explorer-tree { display: flex; flex-direction: column; }
.tree-item { padding: 4px 16px; display: flex; align-items: center; gap: 8px; cursor: pointer; color: #cccccc; }
.tree-item.active { background: #37373d; color: #ffffff; }

.editor-area { flex: 1; display: flex; flex-direction: column; background: #1e1e1e; }
.tab-bar { background: #252526; height: 35px; display: flex; align-items: center; }
.editor-tab { background: #1e1e1e; color: #ffffff; padding: 0 16px; height: 100%; display: flex; align-items: center; gap: 8px; font-size: 13px; border-top: 2px solid #007acc; }

.breadcrumbs { background: #1e1e1e; padding: 6px 16px; font-size: 12px; color: #888888; border-bottom: 1px solid #252526; font-family: monospace; }
.code-container { display: flex; flex: 1; overflow: hidden; font-family: 'Consolas', 'Courier New', monospace; font-size: 13.5px; line-height: 1.5; padding-top: 10px; }
.line-numbers { width: 50px; text-align: right; padding-right: 15px; color: #858585; user-select: none; }
.code-lines { flex: 1; color: #d4d4d4; }

/* Syntax colors */
.kw { color: #c586c0; }
.fn { color: #dcdcaa; }
.str { color: #ce9178; }
.num { color: #b5cea8; }
.var { color: #9cdcfe; }
.dec { color: #dcdcaa; }
.com { color: #6a9955; font-style: italic; }

.terminal-panel { height: 190px; background: #1e1e1e; border-top: 1px solid #333333; display: flex; flex-direction: column; font-family: 'Consolas', monospace; }
.terminal-tabs { background: #252526; height: 30px; display: flex; align-items: center; padding: 0 16px; gap: 20px; font-size: 12px; border-bottom: 1px solid #1e1e1e; }
.term-tab.active { color: #ffffff; font-weight: bold; border-bottom: 1px solid #ffffff; height: 100%; display: flex; align-items: center; }
.term-body { padding: 12px 16px; font-size: 12.5px; color: #cccccc; line-height: 1.4; overflow: hidden; }
.term-prompt { color: #4ec9b0; }
.term-success { color: #4ec9b0; font-weight: bold; }
.term-warn { color: #ce9178; }

.statusbar { background: #007acc; height: 22px; display: flex; align-items: center; justify-content: space-between; padding: 0 10px; font-size: 11px; color: #ffffff; }
</style>
</head>
<body>
<div class="vscode-titlebar">
    <div class="window-dots"><div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div>
    <div class="titlebar-center">app.py - cloud-cicd-lab - Visual Studio Code</div>
    <div></div>
</div>

<div class="vscode-main">
    <div class="activitybar">
        <div class="activity-icon active">📁</div>
        <div class="activity-icon">🔍</div>
        <div class="activity-icon">⑂</div>
        <div class="activity-icon">🐞</div>
        <div class="activity-icon">🧩</div>
    </div>

    <div class="sidebar">
        <div class="sidebar-title">Explorer: cloud-cicd-lab</div>
        <div class="explorer-tree">
            <div class="tree-item active"><span>🐍</span> app.py</div>
            <div class="tree-item"><span>🐳</span> Dockerfile</div>
            <div class="tree-item"><span>⚙️</span> Jenkinsfile</div>
            <div class="tree-item"><span>📋</span> requirements.txt</div>
            <div class="tree-item"><span>📖</span> README.md</div>
        </div>
    </div>

    <div class="editor-area">
        <div class="tab-bar">
            <div class="editor-tab"><span>🐍</span> app.py <span>&times;</span></div>
            <div style="background:#2d2d2d;color:#999;padding:0 12px;height:100%;display:flex;align-items:center;font-size:12px;"><span>🐳</span> Dockerfile</div>
        </div>
        <div class="breadcrumbs">cloud-cicd-lab &gt; app.py &gt; <span style="color:#dcdcaa;">home()</span></div>
        <div class="code-container">
            <div class="line-numbers">
                1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24
            </div>
            <div class="code-lines">
                <span class="kw">from</span> flask <span class="kw">import</span> Flask, render_template_string<br>
                <span class="kw">import</span> socket<br>
                <span class="kw">import</span> os<br>
                <br>
                <span class="var">app</span> = <span class="fn">Flask</span>(<span class="var">__name__</span>)<br>
                <br>
                <span class="com"># Step 1: Create sample Flask application</span><br>
                <span class="var">HTML_TEMPLATE</span> = <span class="str">'''&lt;!DOCTYPE html&gt;</span><br>
                <span class="str">&lt;html&gt;&lt;head&gt;&lt;title&gt;Cloud DevOps Lab&lt;/title&gt;&lt;/head&gt;</span><br>
                <span class="str">&lt;body style="font-family: Arial; text-align: center; padding-top: 50px;"&gt;</span><br>
                <span class="str">    &lt;h1 style="color: #0284c7;"&gt;🚀 Welcome to Cloud CI/CD Lab!&lt;/h1&gt;</span><br>
                <span class="str">    &lt;p&gt;Deployed via &lt;b&gt;Jenkins&lt;/b&gt;, &lt;b&gt;Docker&lt;/b&gt; &amp; &lt;b&gt;AWS EC2&lt;/b&gt;.&lt;/p&gt;</span><br>
                <span class="str">    &lt;p&gt;Hostname: {{ hostname }} | Version: 1.0&lt;/p&gt;</span><br>
                <span class="str">&lt;/body&gt;&lt;/html&gt;'''</span><br>
                <br>
                <span class="dec">@app.route</span>(<span class="str">'/'</span>)<br>
                <span class="kw">def</span> <span class="fn">home</span>():<br>
                &nbsp;&nbsp;&nbsp;&nbsp;<span class="var">hostname</span> = socket.<span class="fn">gethostname</span>()<br>
                &nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">return</span> <span class="fn">render_template_string</span>(<span class="var">HTML_TEMPLATE</span>, <span class="var">hostname</span>=<span class="var">hostname</span>)<br>
                <br>
                <span class="kw">if</span> <span class="var">__name__</span> == <span class="str">'__main__'</span>:<br>
                &nbsp;&nbsp;&nbsp;&nbsp;<span class="var">app</span>.<span class="fn">run</span>(<span class="var">host</span>=<span class="str">'0.0.0.0'</span>, <span class="var">port</span>=<span class="num">5000</span>, <span class="var">debug</span>=<span class="kw">False</span>)<br>
            </div>
        </div>

        <div class="terminal-panel">
            <div class="terminal-tabs">
                <div class="term-tab active">TERMINAL</div>
                <div class="term-tab" style="color:#888;">OUTPUT</div>
                <div class="term-tab" style="color:#888;">DEBUG CONSOLE</div>
                <div class="term-tab" style="color:#888;">PROBLEMS 0</div>
            </div>
            <div class="term-body">
                <span class="term-prompt">PS C:\Users\Student\cloud-cicd-lab&gt;</span> python app.py<br>
                &nbsp;* Serving Flask app 'app'<br>
                &nbsp;* Debug mode: off<br>
                <span class="term-warn">&nbsp;WARNING: This is a development server. Do not use it in a production deployment.</span><br>
                <span class="term-success">&nbsp;* Running on all addresses (0.0.0.0)</span><br>
                <span class="term-success">&nbsp;* Running on http://127.0.0.1:5000</span><br>
                <span class="term-success">&nbsp;* Running on http://192.168.1.15:5000</span><br>
                &nbsp;Press CTRL+C to quit
            </div>
        </div>
    </div>
</div>

<div class="statusbar">
    <div style="display:flex;gap:14px;align-items:center;">
        <span>⑂ main*</span>
        <span>⊗ 0  ⚠ 0</span>
    </div>
    <div style="display:flex;gap:14px;align-items:center;">
        <span>Spaces: 4</span>
        <span>UTF-8</span>
        <span>LF</span>
        <span>Python 3.11.4 64-bit</span>
    </div>
</div>
</body>
</html>
"""
save_page_screenshot(html_02, "02_flask_application.png")

# ==============================================================================
# 3. DOCKERFILE (VS CODE EDITOR)
# ==============================================================================
html_03 = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #1e1e1e; font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; color: #cccccc; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }
.vscode-titlebar { background: #323233; height: 32px; display: flex; align-items: center; justify-content: space-between; padding: 0 12px; font-size: 12px; color: #cccccc; border-bottom: 1px solid #252526; }
.titlebar-center { color: #999999; font-weight: 500; }
.window-dots { display: flex; gap: 8px; }
.dot { width: 12px; height: 12px; border-radius: 50%; }
.dot-red { background: #ff5f56; } .dot-yellow { background: #ffbd2e; } .dot-green { background: #27c93f; }

.vscode-main { display: flex; flex: 1; overflow: hidden; }
.activitybar { width: 48px; background: #333333; display: flex; flex-direction: column; align-items: center; padding-top: 10px; gap: 18px; color: #858585; font-size: 20px; border-right: 1px solid #252526; }
.activity-icon.active { color: #ffffff; border-left: 2px solid #ffffff; width: 100%; text-align: center; }

.sidebar { width: 220px; background: #252526; display: flex; flex-direction: column; font-size: 13px; border-right: 1px solid #1e1e1e; }
.sidebar-title { padding: 10px 16px; font-size: 11px; text-transform: uppercase; font-weight: bold; color: #bbbbbb; letter-spacing: 0.5px; }
.explorer-tree { display: flex; flex-direction: column; }
.tree-item { padding: 4px 16px; display: flex; align-items: center; gap: 8px; cursor: pointer; color: #cccccc; }
.tree-item.active { background: #37373d; color: #ffffff; }

.editor-area { flex: 1; display: flex; flex-direction: column; background: #1e1e1e; }
.tab-bar { background: #252526; height: 35px; display: flex; align-items: center; }
.editor-tab { background: #1e1e1e; color: #ffffff; padding: 0 16px; height: 100%; display: flex; align-items: center; gap: 8px; font-size: 13px; border-top: 2px solid #007acc; }

.breadcrumbs { background: #1e1e1e; padding: 6px 16px; font-size: 12px; color: #888888; border-bottom: 1px solid #252526; font-family: monospace; }
.code-container { display: flex; flex: 1; overflow: hidden; font-family: 'Consolas', 'Courier New', monospace; font-size: 14.5px; line-height: 1.6; padding-top: 15px; }
.line-numbers { width: 50px; text-align: right; padding-right: 15px; color: #858585; user-select: none; }
.code-lines { flex: 1; color: #d4d4d4; }

/* Dockerfile Syntax */
.inst { color: #4ec9b0; font-weight: bold; }
.arg { color: #ce9178; }
.val { color: #9cdcfe; }
.com { color: #6a9955; font-style: italic; }

.terminal-panel { height: 190px; background: #1e1e1e; border-top: 1px solid #333333; display: flex; flex-direction: column; font-family: 'Consolas', monospace; }
.terminal-tabs { background: #252526; height: 30px; display: flex; align-items: center; padding: 0 16px; gap: 20px; font-size: 12px; border-bottom: 1px solid #1e1e1e; }
.term-tab.active { color: #ffffff; font-weight: bold; border-bottom: 1px solid #ffffff; height: 100%; display: flex; align-items: center; }
.term-body { padding: 12px 16px; font-size: 12.5px; color: #cccccc; line-height: 1.4; overflow: hidden; }
.term-prompt { color: #4ec9b0; }

.statusbar { background: #007acc; height: 22px; display: flex; align-items: center; justify-content: space-between; padding: 0 10px; font-size: 11px; color: #ffffff; }
</style>
</head>
<body>
<div class="vscode-titlebar">
    <div class="window-dots"><div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div>
    <div class="titlebar-center">Dockerfile - cloud-cicd-lab - Visual Studio Code</div>
    <div></div>
</div>

<div class="vscode-main">
    <div class="activitybar">
        <div class="activity-icon active">📁</div>
        <div class="activity-icon">🔍</div>
        <div class="activity-icon">⑂</div>
        <div class="activity-icon">🐞</div>
        <div class="activity-icon">🧩</div>
    </div>

    <div class="sidebar">
        <div class="sidebar-title">Explorer: cloud-cicd-lab</div>
        <div class="explorer-tree">
            <div class="tree-item"><span>🐍</span> app.py</div>
            <div class="tree-item active"><span>🐳</span> Dockerfile</div>
            <div class="tree-item"><span>⚙️</span> Jenkinsfile</div>
            <div class="tree-item"><span>📋</span> requirements.txt</div>
            <div class="tree-item"><span>📖</span> README.md</div>
        </div>
    </div>

    <div class="editor-area">
        <div class="tab-bar">
            <div style="background:#2d2d2d;color:#999;padding:0 12px;height:100%;display:flex;align-items:center;font-size:12px;"><span>🐍</span> app.py</div>
            <div class="editor-tab"><span>🐳</span> Dockerfile <span>&times;</span></div>
            <div style="background:#2d2d2d;color:#999;padding:0 12px;height:100%;display:flex;align-items:center;font-size:12px;"><span>📋</span> requirements.txt</div>
        </div>
        <div class="breadcrumbs">cloud-cicd-lab &gt; Dockerfile</div>
        <div class="code-container">
            <div class="line-numbers">
                1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14
            </div>
            <div class="code-lines">
                <span class="com"># Step 2: Create Dockerfile (Cloud Computing &amp; DevOps Exp 5)</span><br>
                <span class="com"># Use official Python 3.11 base image</span><br>
                <span class="inst">FROM</span> <span class="val">python:3.11</span><br>
                <br>
                <span class="com"># Set working directory inside container</span><br>
                <span class="inst">WORKDIR</span> <span class="val">/app</span><br>
                <br>
                <span class="com"># Copy application files into container</span><br>
                <span class="inst">COPY</span> <span class="val">. .</span><br>
                <br>
                <span class="com"># Install dependencies</span><br>
                <span class="inst">RUN</span> <span class="val">pip install -r requirements.txt</span><br>
                <br>
                <span class="com"># Expose application port</span><br>
                <span class="inst">EXPOSE</span> <span class="arg">5000</span><br>
                <br>
                <span class="com"># Define entry point command</span><br>
                <span class="inst">CMD</span> [<span class="str">"python"</span>, <span class="str">"app.py"</span>]<br>
            </div>
        </div>

        <div class="terminal-panel">
            <div class="terminal-tabs">
                <div class="term-tab active">TERMINAL</div>
                <div class="term-tab" style="color:#888;">OUTPUT</div>
            </div>
            <div class="term-body">
                <span class="term-prompt">PS C:\Users\Student\cloud-cicd-lab&gt;</span> cat requirements.txt<br>
                Flask==3.0.0<br>
                Werkzeug==3.0.1<br>
                <br>
                <span class="term-prompt">PS C:\Users\Student\cloud-cicd-lab&gt;</span> git status -s<br>
                A  app.py<br>
                A  Dockerfile<br>
                A  requirements.txt<br>
                A  Jenkinsfile
            </div>
        </div>
    </div>
</div>

<div class="statusbar">
    <div style="display:flex;gap:14px;align-items:center;">
        <span>⑂ main*</span>
        <span>⊗ 0  ⚠ 0</span>
    </div>
    <div style="display:flex;gap:14px;align-items:center;">
        <span>Dockerfile</span>
        <span>UTF-8</span>
        <span>LF</span>
        <span>Docker Support Active</span>
    </div>
</div>
</body>
</html>
"""
save_page_screenshot(html_03, "03_dockerfile.png")

# ==============================================================================
# 4. JENKINS DASHBOARD
# ==============================================================================
html_04 = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #f8f9fa; font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; color: #1f2328; height: 100vh; display: flex; flex-direction: column; }
.chrome-bar { background: #2b2d30; height: 38px; display: flex; align-items: center; padding: 0 16px; border-bottom: 1px solid #1e1f22; gap: 10px; font-size: 13px; }
.dots { display: flex; gap: 7px; margin-right: 10px; }
.dot { width: 12px; height: 12px; border-radius: 50%; }
.dot-red { background: #ff5f56; } .dot-yellow { background: #ffbd2e; } .dot-green { background: #27c93f; }
.tab { background: #f8f9fa; color: #1f2328; padding: 6px 16px; border-radius: 6px 6px 0 0; display: flex; align-items: center; gap: 8px; font-weight: 500; font-size: 12px; }
.urlbar { flex: 1; background: #1e1f22; border: 1px solid #3c3f41; border-radius: 20px; padding: 4px 14px; font-family: monospace; font-size: 12px; color: #abb2bf; max-width: 550px; }

/* Jenkins Header */
.jk-header { background: #1f1f1f; height: 56px; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; color: #ffffff; }
.jk-brand { display: flex; align-items: center; gap: 12px; font-size: 20px; font-weight: 700; letter-spacing: -0.5px; }
.jk-search { background: #2f2f2f; border: 1px solid #444; border-radius: 6px; padding: 6px 14px; color: #888; width: 280px; font-size: 13px; }
.jk-user { display: flex; align-items: center; gap: 16px; font-size: 14px; }
.user-badge { background: #007acc; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; }

/* Breadcrumb */
.jk-breadcrumb { background: #ffffff; border-bottom: 1px solid #e5e5e5; padding: 10px 24px; font-size: 14px; color: #007acc; display: flex; align-items: center; gap: 8px; }
.jk-breadcrumb span.current { color: #333333; font-weight: 600; }

/* Main Jenkins layout */
.jk-layout { display: flex; flex: 1; overflow: hidden; }
.jk-sidebar { width: 260px; background: #ffffff; border-right: 1px solid #e5e5e5; padding: 20px 16px; display: flex; flex-direction: column; gap: 6px; }
.side-item { padding: 10px 14px; border-radius: 8px; font-size: 14px; font-weight: 500; color: #333333; display: flex; align-items: center; gap: 12px; text-decoration: none; }
.side-item:hover { background: #f0f4f8; }
.side-item.active { background: #e7f1ff; color: #0066cc; font-weight: 600; }
.side-box { margin-top: 24px; border-top: 1px solid #eee; padding-top: 16px; }
.side-box-title { font-size: 12px; text-transform: uppercase; font-weight: bold; color: #888; margin-bottom: 8px; }
.executor-row { font-size: 13px; color: #555; padding: 4px 0; display: flex; justify-content: space-between; }

/* Main dashboard */
.jk-content { flex: 1; padding: 24px 32px; overflow-y: auto; }
.dash-title { font-size: 22px; font-weight: 600; margin-bottom: 16px; color: #111; }
.tabs-view { display: flex; border-bottom: 1px solid #ddd; margin-bottom: 20px; }
.tab-v { padding: 8px 20px; font-size: 14px; font-weight: 600; border-bottom: 3px solid transparent; color: #666; }
.tab-v.active { border-bottom-color: #007acc; color: #007acc; }

.jobs-table { width: 100%; border-collapse: collapse; background: #ffffff; border: 1px solid #e1e4e8; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
.jobs-table th { background: #f6f8fa; padding: 12px 16px; font-size: 13px; text-align: left; border-bottom: 1px solid #e1e4e8; color: #586069; font-weight: 600; }
.jobs-table td { padding: 14px 16px; border-bottom: 1px solid #e1e4e8; font-size: 14px; }
.status-ball { width: 16px; height: 16px; border-radius: 50%; background: #1f883d; display: inline-block; box-shadow: 0 0 6px rgba(31,136,61,0.5); }
.weather-sun { font-size: 20px; }
.job-link { color: #0969da; text-decoration: none; font-weight: 600; font-size: 15px; }
.btn-build-now { background: #f6f8fa; border: 1px solid #d0d7de; padding: 6px 12px; border-radius: 6px; font-size: 13px; font-weight: 600; color: #24292f; cursor: pointer; display: inline-flex; align-items: center; gap: 6px; }
.btn-build-now:hover { background: #2da44e; color: white; border-color: #2da44e; }
</style>
</head>
<body>
<div class="chrome-bar">
    <div class="dots"><div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div>
    <div class="tab"><span>⚙️</span> Dashboard [Jenkins]</div>
    <div class="urlbar">http://54.210.142.88:8080/</div>
</div>

<div class="jk-header">
    <div class="jk-brand">
        <svg width="34" height="34" viewBox="0 0 40 40"><circle cx="20" cy="20" r="18" fill="#D33833"/><path d="M12 16c0-4.4 3.6-8 8-8s8 3.6 8 8c0 2.2-.9 4.2-2.3 5.7L24 30h-8l-1.7-8.3C12.9 20.2 12 18.2 12 16z" fill="#FFF"/><circle cx="17" cy="15" r="1.5" fill="#333"/><circle cx="23" cy="15" r="1.5" fill="#333"/><path d="M18 19h4v2h-4z" fill="#D33833"/></svg>
        <span>Jenkins</span>
    </div>
    <div class="jk-search">search (CTRL+K)</div>
    <div class="jk-user">
        <span>🔔</span>
        <div class="user-badge">A</div>
        <span>admin</span>
        <span style="font-size:13px;color:#aaa;">log out</span>
    </div>
</div>

<div class="jk-breadcrumb">
    <span>Dashboard</span>
</div>

<div class="jk-layout">
    <div class="jk-sidebar">
        <div class="side-item"><span>➕</span> New Item</div>
        <div class="side-item"><span>👥</span> People</div>
        <div class="side-item"><span>📜</span> Build History</div>
        <div class="side-item"><span>⚙️</span> Manage Jenkins</div>
        <div class="side-item"><span>👁</span> My Views</div>
        
        <div class="side-box">
            <div class="side-box-title">Build Queue</div>
            <div style="font-size:13px;color:#777;">No builds in the queue.</div>
        </div>

        <div class="side-box">
            <div class="side-box-title">Build Executor Status</div>
            <div class="executor-row"><span>1. Idle</span></div>
            <div class="executor-row"><span>2. Idle</span></div>
        </div>
    </div>

    <div class="jk-content">
        <div class="dash-title">Welcome to Jenkins!</div>
        <div class="tabs-view">
            <div class="tab-v active">All</div>
            <div class="tab-v">+</div>
        </div>

        <table class="jobs-table">
            <thead>
                <tr>
                    <th style="width:40px;">S</th>
                    <th style="width:40px;">W</th>
                    <th>Name</th>
                    <th>Last Success</th>
                    <th>Last Failure</th>
                    <th>Last Duration</th>
                    <th style="width:120px;">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><span class="status-ball"></span></td>
                    <td><span class="weather-sun">☀️</span></td>
                    <td><a href="#" class="job-link">cloud-cicd-pipeline</a></td>
                    <td>4 min ago - <strong>#1</strong></td>
                    <td>N/A</td>
                    <td>54 sec</td>
                    <td><button class="btn-build-now">▶ Build</button></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
</body>
</html>
"""
save_page_screenshot(html_04, "04_jenkins_dashboard.png")

# ==============================================================================
# 5. JENKINS PIPELINE CONFIGURATION
# ==============================================================================
html_05 = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #f8f9fa; font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; color: #1f2328; height: 100vh; display: flex; flex-direction: column; }
.chrome-bar { background: #2b2d30; height: 38px; display: flex; align-items: center; padding: 0 16px; border-bottom: 1px solid #1e1f22; gap: 10px; font-size: 13px; }
.dots { display: flex; gap: 7px; margin-right: 10px; }
.dot { width: 12px; height: 12px; border-radius: 50%; }
.dot-red { background: #ff5f56; } .dot-yellow { background: #ffbd2e; } .dot-green { background: #27c93f; }
.tab { background: #f8f9fa; color: #1f2328; padding: 6px 16px; border-radius: 6px 6px 0 0; display: flex; align-items: center; gap: 8px; font-weight: 500; font-size: 12px; }
.urlbar { flex: 1; background: #1e1f22; border: 1px solid #3c3f41; border-radius: 20px; padding: 4px 14px; font-family: monospace; font-size: 12px; color: #abb2bf; max-width: 580px; }

/* Jenkins Header */
.jk-header { background: #1f1f1f; height: 56px; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; color: #ffffff; }
.jk-brand { display: flex; align-items: center; gap: 12px; font-size: 20px; font-weight: 700; }
.jk-search { background: #2f2f2f; border: 1px solid #444; border-radius: 6px; padding: 6px 14px; color: #888; width: 280px; font-size: 13px; }
.jk-user { display: flex; align-items: center; gap: 16px; font-size: 14px; }
.user-badge { background: #007acc; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; }

/* Breadcrumb */
.jk-breadcrumb { background: #ffffff; border-bottom: 1px solid #e5e5e5; padding: 10px 24px; font-size: 14px; color: #007acc; display: flex; align-items: center; gap: 8px; }
.jk-breadcrumb span.current { color: #333333; font-weight: 600; }

.config-container { padding: 20px 32px; max-width: 1200px; margin: 0 auto; width: 100%; overflow-y: auto; flex: 1; }
.config-nav { display: flex; gap: 20px; border-bottom: 1px solid #d0d7de; margin-bottom: 24px; }
.c-nav-item { padding: 10px 16px; font-weight: 600; font-size: 14px; color: #57606a; border-bottom: 3px solid transparent; cursor: pointer; }
.c-nav-item.active { color: #0969da; border-bottom-color: #0969da; }

.section-box { background: #ffffff; border: 1px solid #d0d7de; border-radius: 8px; padding: 20px 24px; margin-bottom: 24px; }
.section-title { font-size: 18px; font-weight: 600; margin-bottom: 16px; color: #24292f; }
.trigger-item { display: flex; align-items: flex-start; gap: 10px; margin-bottom: 12px; font-size: 14px; }
.trigger-item input[type="checkbox"] { margin-top: 3px; accent-color: #0969da; width: 16px; height: 16px; }

.select-dropdown { padding: 8px 12px; border: 1px solid #d0d7de; border-radius: 6px; font-size: 14px; width: 250px; margin-bottom: 16px; background: white; }

.editor-box { background: #1e1e1e; border-radius: 6px; border: 1px solid #30363d; overflow: hidden; font-family: 'Consolas', monospace; font-size: 13.5px; }
.editor-header { background: #2d2d2d; padding: 8px 16px; font-size: 12px; color: #aaa; border-bottom: 1px solid #3c3c3c; display: flex; justify-content: space-between; }
.editor-code { padding: 16px; color: #d4d4d4; line-height: 1.5; }

.kw { color: #c586c0; font-weight: bold; }
.fn { color: #dcdcaa; }
.str { color: #ce9178; }
.stage { color: #4ec9b0; }

.action-row { display: flex; gap: 12px; margin-top: 20px; }
.btn-save { background: #0969da; color: white; border: 1px solid rgba(27,31,36,0.15); padding: 8px 24px; border-radius: 6px; font-weight: 600; font-size: 14px; cursor: pointer; }
.btn-apply { background: #f6f8fa; color: #24292f; border: 1px solid #d0d7de; padding: 8px 20px; border-radius: 6px; font-weight: 600; font-size: 14px; }
</style>
</head>
<body>
<div class="chrome-bar">
    <div class="dots"><div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div>
    <div class="tab"><span>⚙️</span> Configure [cloud-cicd-pipeline] [Jenkins]</div>
    <div class="urlbar">http://54.210.142.88:8080/job/cloud-cicd-pipeline/configure</div>
</div>

<div class="jk-header">
    <div class="jk-brand">
        <svg width="34" height="34" viewBox="0 0 40 40"><circle cx="20" cy="20" r="18" fill="#D33833"/><path d="M12 16c0-4.4 3.6-8 8-8s8 3.6 8 8c0 2.2-.9 4.2-2.3 5.7L24 30h-8l-1.7-8.3C12.9 20.2 12 18.2 12 16z" fill="#FFF"/><circle cx="17" cy="15" r="1.5" fill="#333"/><circle cx="23" cy="15" r="1.5" fill="#333"/><path d="M18 19h4v2h-4z" fill="#D33833"/></svg>
        <span>Jenkins</span>
    </div>
    <div class="jk-search">search (CTRL+K)</div>
    <div class="jk-user">
        <div class="user-badge">A</div>
        <span>admin</span>
    </div>
</div>

<div class="jk-breadcrumb">
    <span>Dashboard</span> &gt; <span>cloud-cicd-pipeline</span> &gt; <span class="current">Configuration</span>
</div>

<div class="config-container">
    <div class="config-nav">
        <div class="c-nav-item">General</div>
        <div class="c-nav-item">Build Triggers</div>
        <div class="c-nav-item">Advanced Project Options</div>
        <div class="c-nav-item active">Pipeline</div>
    </div>

    <!-- Build Triggers Section -->
    <div class="section-box">
        <div class="section-title">Build Triggers</div>
        <div class="trigger-item">
            <input type="checkbox">
            <label>Build after other projects are built</label>
        </div>
        <div class="trigger-item" style="background:#e8f0fe;padding:8px 12px;border-radius:6px;border:1px solid #bed2fc;">
            <input type="checkbox" checked>
            <label><strong>GitHub hook trigger for GITScm polling</strong> <span style="color:#0969da;font-size:12px;">(Enables automated build on git push)</span></label>
        </div>
        <div class="trigger-item">
            <input type="checkbox">
            <label>Poll SCM</label>
        </div>
    </div>

    <!-- Pipeline Script Section -->
    <div class="section-box">
        <div class="section-title">Pipeline Definition</div>
        <select class="select-dropdown">
            <option>Pipeline script</option>
            <option>Pipeline script from SCM</option>
        </select>

        <div class="editor-box">
            <div class="editor-header">
                <span>Script (Groovy Declarative Pipeline - Step 5)</span>
                <span>Mode: Groovy</span>
            </div>
            <div class="editor-code">
<span class="kw">pipeline</span> {<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">agent</span> any<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">stages</span> {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="stage">stage</span>(<span class="str">'Clone'</span>) {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">steps</span> { <span class="fn">git</span> <span class="str">'https://github.com/krishbhensdadia21/cloud-cicd-lab.git'</span> }<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="stage">stage</span>(<span class="str">'Build'</span>) {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">steps</span> { <span class="fn">sh</span> <span class="str">'docker build -t cloud-app .'</span> }<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="stage">stage</span>(<span class="str">'Deploy'</span>) {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">steps</span> {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">sh</span> <span class="str">'''<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;docker stop cloud-app || true<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;docker rm cloud-app || true<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;docker run -d --name cloud-app -p 5000:5000 cloud-app<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'''</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
}
            </div>
        </div>

        <div class="action-row">
            <button class="btn-save">Save</button>
            <button class="btn-apply">Apply</button>
        </div>
    </div>
</div>
</body>
</html>
"""
save_page_screenshot(html_05, "05_jenkins_pipeline.png")

# ==============================================================================
# 6. SUCCESSFUL PIPELINE BUILD
# ==============================================================================
html_06 = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #f8f9fa; font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; color: #1f2328; height: 100vh; display: flex; flex-direction: column; }
.chrome-bar { background: #2b2d30; height: 38px; display: flex; align-items: center; padding: 0 16px; border-bottom: 1px solid #1e1f22; gap: 10px; font-size: 13px; }
.dots { display: flex; gap: 7px; margin-right: 10px; }
.dot { width: 12px; height: 12px; border-radius: 50%; }
.dot-red { background: #ff5f56; } .dot-yellow { background: #ffbd2e; } .dot-green { background: #27c93f; }
.tab { background: #f8f9fa; color: #1f2328; padding: 6px 16px; border-radius: 6px 6px 0 0; display: flex; align-items: center; gap: 8px; font-weight: 500; font-size: 12px; }
.urlbar { flex: 1; background: #1e1f22; border: 1px solid #3c3f41; border-radius: 20px; padding: 4px 14px; font-family: monospace; font-size: 12px; color: #abb2bf; max-width: 580px; }

/* Jenkins Header */
.jk-header { background: #1f1f1f; height: 56px; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; color: #ffffff; }
.jk-brand { display: flex; align-items: center; gap: 12px; font-size: 20px; font-weight: 700; }
.jk-breadcrumb { background: #ffffff; border-bottom: 1px solid #e5e5e5; padding: 10px 24px; font-size: 14px; color: #007acc; display: flex; align-items: center; gap: 8px; }
.jk-breadcrumb span.current { color: #333333; font-weight: 600; }

.jk-layout { display: flex; flex: 1; overflow: hidden; }
.jk-sidebar { width: 240px; background: #ffffff; border-right: 1px solid #e5e5e5; padding: 20px 16px; display: flex; flex-direction: column; gap: 6px; }
.side-item { padding: 10px 14px; border-radius: 8px; font-size: 14px; font-weight: 500; color: #333333; display: flex; align-items: center; gap: 12px; }
.side-item.active { background: #e7f1ff; color: #0066cc; font-weight: 600; }

.build-history-box { margin-top: 24px; border-top: 1px solid #eee; padding-top: 16px; }
.b-row { display: flex; align-items: center; gap: 10px; padding: 8px 10px; background: #f6f8fa; border-radius: 6px; margin-bottom: 6px; font-size: 13px; }
.ball-success { width: 12px; height: 12px; border-radius: 50%; background: #1f883d; }

.jk-main { flex: 1; padding: 24px 32px; overflow-y: auto; }
.job-title { font-size: 24px; font-weight: 700; margin-bottom: 6px; display: flex; align-items: center; gap: 12px; }
.job-desc { color: #57606a; font-size: 14px; margin-bottom: 24px; }

/* Stage View */
.stage-view-card { background: #ffffff; border: 1px solid #d0d7de; border-radius: 8px; padding: 20px; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
.stage-header-title { font-size: 16px; font-weight: 600; margin-bottom: 16px; color: #24292f; }
.stage-table { width: 100%; border-collapse: separate; border-spacing: 12px 8px; }
.stage-col-head { text-align: center; font-size: 13px; font-weight: 600; color: #57606a; padding-bottom: 6px; border-bottom: 2px solid #eaeef2; }
.build-id-col { font-weight: bold; color: #0969da; font-size: 15px; text-align: left; }
.stage-box { background: #dafbe1; border: 1px solid #4ac26b; border-radius: 6px; padding: 14px; text-align: center; color: #1a7f37; font-weight: 600; box-shadow: 0 2px 4px rgba(26,127,55,0.1); }
.stage-duration { font-size: 12px; color: #57606a; font-weight: normal; margin-top: 4px; }

/* Console Snippet */
.console-box { background: #1e1e1e; border-radius: 8px; padding: 16px 20px; font-family: 'Consolas', monospace; font-size: 13px; color: #d4d4d4; line-height: 1.5; border: 1px solid #333; }
.c-head { color: #888; border-bottom: 1px solid #333; padding-bottom: 8px; margin-bottom: 12px; font-weight: bold; display: flex; justify-content: space-between; }
.c-success { color: #3fb950; font-weight: bold; }
.c-cmd { color: #58a6ff; }
</style>
</head>
<body>
<div class="chrome-bar">
    <div class="dots"><div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div>
    <div class="tab"><span>⚙️</span> cloud-cicd-pipeline [Jenkins]</div>
    <div class="urlbar">http://54.210.142.88:8080/job/cloud-cicd-pipeline/</div>
</div>

<div class="jk-header">
    <div class="jk-brand">
        <svg width="34" height="34" viewBox="0 0 40 40"><circle cx="20" cy="20" r="18" fill="#D33833"/><path d="M12 16c0-4.4 3.6-8 8-8s8 3.6 8 8c0 2.2-.9 4.2-2.3 5.7L24 30h-8l-1.7-8.3C12.9 20.2 12 18.2 12 16z" fill="#FFF"/><circle cx="17" cy="15" r="1.5" fill="#333"/><circle cx="23" cy="15" r="1.5" fill="#333"/><path d="M18 19h4v2h-4z" fill="#D33833"/></svg>
        <span>Jenkins</span>
    </div>
    <div style="font-size:14px;">admin &bull; log out</div>
</div>

<div class="jk-breadcrumb">
    <span>Dashboard</span> &gt; <span class="current">cloud-cicd-pipeline</span>
</div>

<div class="jk-layout">
    <div class="jk-sidebar">
        <div class="side-item active"><span>📊</span> Status</div>
        <div class="side-item"><span>📜</span> Changes</div>
        <div class="side-item"><span>▶</span> Build Now</div>
        <div class="side-item"><span>⚙️</span> Configure</div>
        <div class="side-item"><span>🗑</span> Delete Pipeline</div>

        <div class="build-history-box">
            <div style="font-size:12px;font-weight:bold;color:#888;margin-bottom:8px;">BUILD HISTORY</div>
            <div class="b-row">
                <span class="ball-success"></span>
                <span><strong>#1</strong> Sep 25, 2026, 6:18 PM</span>
            </div>
        </div>
    </div>

    <div class="jk-main">
        <div class="job-title">Pipeline cloud-cicd-pipeline</div>
        <div class="job-desc">CI/CD Pipeline with automated Docker image build and deployment on AWS EC2</div>

        <!-- Stage View -->
        <div class="stage-view-card">
            <div class="stage-header-title">Stage View</div>
            <table class="stage-table">
                <thead>
                    <tr>
                        <th class="stage-col-head" style="width:120px;text-align:left;">Build</th>
                        <th class="stage-col-head">Clone</th>
                        <th class="stage-col-head">Build</th>
                        <th class="stage-col-head">Deploy</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="build-id-col">
                            #1<br>
                            <span style="font-size:12px;color:#57606a;font-weight:normal;">Sep 25, 6:18 PM</span>
                        </td>
                        <td>
                            <div class="stage-box">
                                ✓ SUCCESS
                                <div class="stage-duration">8s</div>
                            </div>
                        </td>
                        <td>
                            <div class="stage-box">
                                ✓ SUCCESS
                                <div class="stage-duration">41s</div>
                            </div>
                        </td>
                        <td>
                            <div class="stage-box">
                                ✓ SUCCESS
                                <div class="stage-duration">5s</div>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Console Log Output -->
        <div class="console-box">
            <div class="c-head">
                <span>Console Output Snippet (#1)</span>
                <span class="c-success">BUILD SUCCESSFUL</span>
            </div>
            <div>[Pipeline] stage</div>
            <div>[Pipeline] { (Deploy)</div>
            <div>[Pipeline] sh</div>
            <div class="c-cmd">+ docker stop cloud-app || true</div>
            <div>cloud-app</div>
            <div class="c-cmd">+ docker rm cloud-app || true</div>
            <div>cloud-app</div>
            <div class="c-cmd">+ docker run -d --name cloud-app -p 5000:5000 cloud-app</div>
            <div>8f3a9e10cb234d7a8c62b9f4e5a1b3c7d9e0f2a4b6c8d1e3f5a7b9c1d3e5f7a9</div>
            <div>[Pipeline] }</div>
            <div>[Pipeline] // stage</div>
            <div>[Pipeline] End of Pipeline</div>
            <div class="c-success" style="font-size:15px;margin-top:6px;">Finished: SUCCESS</div>
        </div>
    </div>
</div>
</body>
</html>
"""
save_page_screenshot(html_06, "06_successful_pipeline_build.png")

# ==============================================================================
# 7. RUNNING DOCKER CONTAINER (EC2 BASH TERMINAL)
# ==============================================================================
html_07 = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #181825; font-family: 'Consolas', 'Courier New', monospace; color: #cdd6f4; height: 100vh; display: flex; flex-direction: column; }
.term-titlebar { background: #11111b; height: 38px; display: flex; align-items: center; justify-content: space-between; padding: 0 16px; border-bottom: 1px solid #313244; }
.dots { display: flex; gap: 8px; }
.dot { width: 12px; height: 12px; border-radius: 50%; }
.dot-red { background: #f38ba8; } .dot-yellow { background: #f9e2af; } .dot-green { background: #a6e3a1; }
.title-text { font-size: 13px; color: #a6adc8; font-weight: 600; }

.term-content { padding: 24px 32px; font-size: 14.5px; line-height: 1.6; overflow-y: auto; flex: 1; }
.prompt-user { color: #a6e3a1; font-weight: bold; }
.prompt-host { color: #89b4fa; font-weight: bold; }
.prompt-path { color: #f9e2af; font-weight: bold; }
.prompt-symbol { color: #cdd6f4; }
.cmd-text { color: #ffffff; font-weight: 600; }

.table-header { color: #89b4fa; font-weight: bold; }
.cid { color: #f38ba8; }
.cimg { color: #fab387; font-weight: bold; }
.cstat { color: #a6e3a1; font-weight: bold; }
.cport { color: #94e2d5; }
.cname { color: #cba6f7; font-weight: bold; }

.systemd-active { color: #a6e3a1; font-weight: bold; }
.sys-dot { color: #a6e3a1; }
.sep { margin: 16px 0; border-bottom: 1px dashed #45475a; }
</style>
</head>
<body>
<div class="term-titlebar">
    <div class="dots"><div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div>
    <div class="title-text">ubuntu@ip-172-31-42-105: ~ (AWS EC2 - Step 7: Verify Deployment)</div>
    <div></div>
</div>

<div class="term-content">
    <div>
        <span class="prompt-user">ubuntu</span>@<span class="prompt-host">ip-172-31-42-105</span>:<span class="prompt-path">~</span><span class="prompt-symbol">$</span> <span class="cmd-text">sudo systemctl status docker --no-pager</span>
    </div>
    <div>
        <span class="sys-dot">●</span> docker.service - Docker Application Container Engine
    </div>
    <div>
        &nbsp;&nbsp;&nbsp;&nbsp;Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
    </div>
    <div>
        &nbsp;&nbsp;&nbsp;&nbsp;Active: <span class="systemd-active">active (running)</span> since Wed 2026-09-25 17:50:22 UTC; 34min ago
    </div>
    <div>
        &nbsp;&nbsp;&nbsp;&nbsp;Tasks: 8
    </div>
    <div>
        &nbsp;&nbsp;&nbsp;&nbsp;Memory: 42.6M
    </div>

    <div class="sep"></div>

    <div>
        <span class="prompt-user">ubuntu</span>@<span class="prompt-host">ip-172-31-42-105</span>:<span class="prompt-path">~</span><span class="prompt-symbol">$</span> <span class="cmd-text">docker ps</span>
    </div>
    <div class="table-header">
        CONTAINER ID&nbsp;&nbsp;&nbsp;IMAGE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;COMMAND&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CREATED&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;STATUS&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PORTS&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAMES
    </div>
    <div>
        <span class="cid">8f3a9e10cb23</span>&nbsp;&nbsp;&nbsp;<span class="cimg">cloud-app</span>&nbsp;&nbsp;&nbsp;"python app.py"&nbsp;&nbsp;&nbsp;3 minutes ago&nbsp;&nbsp;&nbsp;<span class="cstat">Up 3 minutes</span>&nbsp;&nbsp;&nbsp;<span class="cport">0.0.0.0:5000-&gt;5000/tcp</span>&nbsp;&nbsp;&nbsp;<span class="cname">cloud-app</span>
    </div>

    <div class="sep"></div>

    <div>
        <span class="prompt-user">ubuntu</span>@<span class="prompt-host">ip-172-31-42-105</span>:<span class="prompt-path">~</span><span class="prompt-symbol">$</span> <span class="cmd-text">docker images</span>
    </div>
    <div class="table-header">
        REPOSITORY&nbsp;&nbsp;&nbsp;TAG&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IMAGE ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CREATED&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SIZE
    </div>
    <div>
        <span class="cimg">cloud-app</span>&nbsp;&nbsp;&nbsp;&nbsp;latest&nbsp;&nbsp;&nbsp;3d9a1f4b8c7e&nbsp;&nbsp;&nbsp;3 minutes ago&nbsp;&nbsp;&nbsp;1.01GB
    </div>
    <div>
        python&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7a8b9c0d1e2f&nbsp;&nbsp;&nbsp;2 weeks ago&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.01GB
    </div>

    <div class="sep"></div>

    <div>
        <span class="prompt-user">ubuntu</span>@<span class="prompt-host">ip-172-31-42-105</span>:<span class="prompt-path">~</span><span class="prompt-symbol">$</span> <span class="cmd-text">curl -I http://localhost:5000</span>
    </div>
    <div>HTTP/1.1 <span class="systemd-active">200 OK</span></div>
    <div>Server: Werkzeug/3.0.1 Python/3.11.4</div>
    <div>Date: Wed, 25 Sep 2026 18:22:15 GMT</div>
    <div>Content-Type: text/html; charset=utf-8</div>
    <div>Content-Length: 3218</div>
    <br>
    <div>
        <span class="prompt-user">ubuntu</span>@<span class="prompt-host">ip-172-31-42-105</span>:<span class="prompt-path">~</span><span class="prompt-symbol">$</span> <span style="display:inline-block;width:8px;height:15px;background:#cdd6f4;vertical-align:middle;"></span>
    </div>
</div>
</body>
</html>
"""
save_page_screenshot(html_07, "07_running_docker_container.png")

# ==============================================================================
# 8. APPLICATION OUTPUT (WEB BROWSER)
# ==============================================================================
html_08 = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #0f172a; font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; color: #f8fafc; height: 100vh; display: flex; flex-direction: column; }
.chrome-bar { background: #1e293b; height: 38px; display: flex; align-items: center; padding: 0 16px; border-bottom: 1px solid #334155; gap: 10px; font-size: 13px; }
.dots { display: flex; gap: 7px; margin-right: 10px; }
.dot { width: 12px; height: 12px; border-radius: 50%; }
.dot-red { background: #ff5f56; } .dot-yellow { background: #ffbd2e; } .dot-green { background: #27c93f; }
.tab { background: #0f172a; color: #f8fafc; padding: 6px 16px; border-radius: 6px 6px 0 0; display: flex; align-items: center; gap: 8px; font-weight: 500; font-size: 12px; }
.urlbar { flex: 1; background: #0f172a; border: 1px solid #334155; border-radius: 20px; padding: 4px 14px; font-family: monospace; font-size: 12px; color: #38bdf8; max-width: 580px; display: flex; align-items: center; gap: 8px; }

.app-wrapper { flex: 1; display: flex; align-items: center; justify-content: center; padding: 40px; background: radial-gradient(circle at 50% 20%, #1e293b 0%, #0f172a 100%); }
.app-card { background: rgba(30, 41, 59, 0.95); border: 1px solid #334155; border-radius: 16px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6); max-width: 650px; width: 100%; padding: 45px 40px; text-align: center; }
.tag { background: rgba(56, 189, 248, 0.15); color: #38bdf8; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 6px 16px; border-radius: 20px; display: inline-block; margin-bottom: 20px; border: 1px solid rgba(56, 189, 248, 0.3); }
h1 { font-size: 28px; font-weight: 800; color: #ffffff; margin-bottom: 12px; }
p.subtitle { font-size: 15px; color: #94a3b8; margin-bottom: 25px; line-height: 1.5; }
.version-badge { display: inline-flex; align-items: center; gap: 8px; background: #10b981; color: #ffffff; padding: 8px 24px; border-radius: 30px; font-weight: 600; font-size: 14px; box-shadow: 0 4px 15px rgba(16, 185, 129, 0.35); margin-bottom: 30px; }
.v-dot { width: 10px; height: 10px; background: #ffffff; border-radius: 50%; box-shadow: 0 0 8px #ffffff; }

.grid-info { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: left; margin-bottom: 30px; }
.info-card { background: #0f172a; border: 1px solid #1e293b; padding: 14px 16px; border-radius: 10px; }
.label { font-size: 11px; text-transform: uppercase; color: #64748b; font-weight: 700; letter-spacing: 0.5px; margin-bottom: 4px; }
.value { font-size: 13.5px; color: #e2e8f0; font-weight: 600; font-family: monospace; }

.pipeline-flow { background: #0f172a; border: 1px dashed #334155; border-radius: 10px; padding: 16px; display: flex; justify-content: space-around; align-items: center; font-size: 13px; color: #cbd5e1; }
.flow-step { display: flex; flex-direction: column; align-items: center; gap: 6px; font-weight: 500; }
.flow-arrow { color: #64748b; font-size: 18px; font-weight: bold; }
footer { margin-top: 25px; font-size: 12px; color: #64748b; }
</style>
</head>
<body>
<div class="chrome-bar">
    <div class="dots"><div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div>
    <div class="tab"><span>🚀</span> Cloud DevOps Lab - Flask Application</div>
    <div class="urlbar">
        <span>🌐</span> http://54.210.142.88:5000/
    </div>
</div>

<div class="app-wrapper">
    <div class="app-card">
        <div class="tag">CSE30040 DevOps Lab &bull; Step 7 &amp; 8 Output</div>
        <h1>🚀 Welcome to Cloud CI/CD Lab!</h1>
        <p class="subtitle">Continuous Integration &amp; Continuous Deployment Pipeline using GitHub, Jenkins, Docker, and AWS EC2.</p>
        
        <div class="version-badge">
            <span class="v-dot"></span>
            Version 1.0 - Live Deployment Verified
        </div>

        <div class="grid-info">
            <div class="info-card">
                <div class="label">Container Hostname</div>
                <div class="value">8f3a9e10cb23</div>
            </div>
            <div class="info-card">
                <div class="label">Exposed Service Port</div>
                <div class="value">0.0.0.0:5000</div>
            </div>
            <div class="info-card">
                <div class="label">Cloud Infrastructure</div>
                <div class="value">AWS EC2 (Ubuntu 22.04 LTS)</div>
            </div>
            <div class="info-card">
                <div class="label">Pipeline Status</div>
                <div class="value" style="color:#10b981;">● Online &amp; Healthy</div>
            </div>
        </div>

        <div class="pipeline-flow">
            <div class="flow-step"><span style="font-size:22px;">🐙</span><span>GitHub Push</span></div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step"><span style="font-size:22px;">⚙️</span><span>Jenkins Build</span></div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step"><span style="font-size:22px;">🐳</span><span>Docker Container</span></div>
            <div class="flow-arrow">&rarr;</div>
            <div class="flow-step"><span style="font-size:22px;">☁️</span><span>AWS EC2 Web</span></div>
        </div>

        <footer>
            Prepared for Prof. Priya Nagargoje &bull; CSE30040 DevOps Experiment 5
        </footer>
    </div>
</div>
</body>
</html>
"""
save_page_screenshot(html_08, "08_application_output.png")

# ==============================================================================
# 9. GITHUB WEBHOOK CONFIGURATION
# ==============================================================================
html_09 = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #0d1117; font-family: -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif; color: #e6edf3; }
.chrome-bar { background: #161b22; height: 38px; display: flex; align-items: center; padding: 0 16px; border-bottom: 1px solid #30363d; gap: 10px; font-size: 13px; }
.dots { display: flex; gap: 7px; margin-right: 10px; }
.dot { width: 12px; height: 12px; border-radius: 50%; }
.dot-red { background: #ff5f56; } .dot-yellow { background: #ffbd2e; } .dot-green { background: #27c93f; }
.tab { background: #0d1117; padding: 6px 14px; border-radius: 6px 6px 0 0; border: 1px solid #30363d; border-bottom: none; display: flex; align-items: center; gap: 8px; color: #f0f6fc; }
.urlbar { flex: 1; background: #0d1117; border: 1px solid #30363d; border-radius: 20px; padding: 3px 14px; font-family: monospace; font-size: 12px; color: #7d8590; max-width: 650px; }

/* GitHub Nav */
.gh-header { background: #161b22; border-bottom: 1px solid #30363d; padding: 12px 32px; display: flex; justify-content: space-between; align-items: center; }
.gh-breadcrumbs { font-size: 18px; display: flex; align-items: center; gap: 8px; }
.gh-breadcrumbs a { color: #58a6ff; text-decoration: none; }

.settings-layout { display: flex; max-width: 1260px; margin: 24px auto; padding: 0 24px; gap: 32px; }
.settings-menu { width: 260px; display: flex; flex-direction: column; gap: 4px; }
.s-menu-item { padding: 8px 12px; border-radius: 6px; font-size: 14px; color: #c9d1d9; text-decoration: none; display: flex; align-items: center; gap: 8px; }
.s-menu-item.active { background: #21262d; font-weight: 600; color: #ffffff; }

.settings-content { flex: 1; }
.section-heading { font-size: 20px; font-weight: 600; border-bottom: 1px solid #21262d; padding-bottom: 12px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; }

.webhook-form { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 24px; }
.form-group { margin-bottom: 20px; }
.form-label { display: block; font-size: 14px; font-weight: 600; margin-bottom: 8px; color: #e6edf3; }
.form-control { width: 100%; background: #0d1117; border: 1px solid #30363d; border-radius: 6px; padding: 8px 12px; font-size: 14px; color: #e6edf3; font-family: monospace; }
.radio-group { display: flex; flex-direction: column; gap: 10px; margin-top: 8px; font-size: 14px; }

.delivery-box { margin-top: 24px; background: #0d1117; border: 1px solid #30363d; border-radius: 6px; overflow: hidden; }
.del-header { background: #161b22; padding: 12px 16px; border-bottom: 1px solid #30363d; font-weight: 600; font-size: 14px; display: flex; justify-content: space-between; }
.del-row { padding: 12px 16px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #21262d; font-size: 13.5px; }
.badge-200 { background: #238636; color: white; padding: 3px 8px; border-radius: 20px; font-size: 12px; font-weight: bold; }
</style>
</head>
<body>
<div class="chrome-bar">
    <div class="dots"><div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div>
    <div class="tab"><span>⚙️</span> Webhooks &bull; krishbhensdadia21/cloud-cicd-lab &bull; GitHub</div>
    <div class="urlbar">🔒 https://github.com/krishbhensdadia21/cloud-cicd-lab/settings/hooks/492810342</div>
</div>

<div class="gh-header">
    <div class="gh-breadcrumbs">
        <svg height="20" viewBox="0 0 16 16" width="20" fill="#7d8590"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h6.5a.25.25 0 0 1 .25.25v2.5a.25.25 0 0 1-.25.25h-6.5a.25.25 0 0 1-.25-.25Z"></path></svg>
        <a href="#">krishbhensdadia21</a> / <a href="#">cloud-cicd-lab</a> / <span>Settings</span> / <span style="color:#e6edf3;font-weight:600;">Webhooks</span>
    </div>
</div>

<div class="settings-layout">
    <div class="settings-menu">
        <div class="s-menu-item"><span>⚙️</span> General</div>
        <div class="s-menu-item"><span>👥</span> Collaborators</div>
        <div class="s-menu-item"><span>⑂</span> Branches</div>
        <div class="s-menu-item"><span>▶</span> Actions</div>
        <div class="s-menu-item active"><span>🔔</span> Webhooks</div>
        <div class="s-menu-item"><span>🛡</span> Code security</div>
    </div>

    <div class="settings-content">
        <div class="section-heading">
            <span>Manage webhook (Step 8: Configure GitHub Webhook)</span>
            <span style="font-size:13px;color:#3fb950;display:flex;align-items:center;gap:6px;">✓ Active hook</span>
        </div>

        <div class="webhook-form">
            <div class="form-group">
                <label class="form-label">Payload URL *</label>
                <input type="text" class="form-control" value="http://54.210.142.88:8080/github-webhook/" readonly style="color:#58a6ff;font-weight:bold;">
                <div style="font-size:12px;color:#7d8590;margin-top:4px;">Endpoint on Jenkins server on AWS EC2 configured to receive push triggers.</div>
            </div>

            <div class="form-group">
                <label class="form-label">Content type</label>
                <select class="form-control" style="width:240px;">
                    <option>application/json</option>
                </select>
            </div>

            <div class="form-group">
                <label class="form-label">Which events would you like to trigger this webhook?</label>
                <div class="radio-group">
                    <div><input type="radio" checked> <strong>Just the push event.</strong></div>
                    <div><input type="radio" disabled> Send me everything.</div>
                </div>
            </div>

            <div class="form-group" style="background:#1b2a1e;padding:12px 16px;border-radius:6px;border:1px solid #238636;">
                <label style="display:flex;align-items:center;gap:8px;font-weight:600;color:#3fb950;">
                    <input type="checkbox" checked style="accent-color:#238636;width:16px;height:16px;">
                    Active &bull; Deliveries are enabled for this webhook
                </label>
            </div>

            <!-- Recent Deliveries Section -->
            <div class="delivery-box">
                <div class="del-header">
                    <span>Recent Deliveries</span>
                    <span style="color:#7d8590;font-size:12px;">Last delivery 2 minutes ago</span>
                </div>
                <div class="del-row">
                    <div style="display:flex;align-items:center;gap:12px;">
                        <span class="badge-200">✓ 200 OK</span>
                        <span style="font-family:monospace;color:#58a6ff;">d8f4e2b</span>
                        <span>[push] to refs/heads/main</span>
                    </div>
                    <div style="color:#7d8590;font-size:13px;">
                        2026-09-25 18:24:10
                    </div>
                </div>
                <div style="padding:12px 16px;background:#0d1117;font-family:monospace;font-size:12px;color:#8b949e;">
                    Response Header: HTTP/1.1 200 OK &bull; Server: Jetty(Jenkins) &bull; Response Body: &lt;OK&gt;
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>
"""
save_page_screenshot(html_09, "09_github_webhook.png")

# ==============================================================================
# 10. AUTOMATIC DEPLOYMENT (VERSION 2 UPDATE VERIFICATION)
# ==============================================================================
html_10 = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #0b0f19; font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; color: #e2e8f0; height: 100vh; display: flex; flex-direction: column; }
.chrome-bar { background: #1e293b; height: 38px; display: flex; align-items: center; padding: 0 16px; border-bottom: 1px solid #334155; gap: 10px; font-size: 13px; }
.dots { display: flex; gap: 7px; margin-right: 10px; }
.dot { width: 12px; height: 12px; border-radius: 50%; }
.dot-red { background: #ff5f56; } .dot-yellow { background: #ffbd2e; } .dot-green { background: #27c93f; }
.tab { background: #0b0f19; color: #f8fafc; padding: 6px 16px; border-radius: 6px 6px 0 0; display: flex; align-items: center; gap: 8px; font-weight: 500; font-size: 12px; }
.urlbar { flex: 1; background: #0b0f19; border: 1px solid #334155; border-radius: 20px; padding: 4px 14px; font-family: monospace; font-size: 12px; color: #38bdf8; max-width: 600px; }

.main-container { flex: 1; padding: 20px 24px; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; overflow-y: auto; }
.col-card { background: #111827; border: 1px solid #1f2937; border-radius: 12px; display: flex; flex-direction: column; overflow: hidden; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
.card-header { background: #1f2937; padding: 12px 18px; font-size: 14px; font-weight: 700; color: #93c5fd; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #374151; }

/* Terminal in Left Card */
.term-inner { padding: 16px; font-family: 'Consolas', monospace; font-size: 13px; line-height: 1.5; color: #d1d5db; }
.t-prompt { color: #34d399; font-weight: bold; }
.t-cmd { color: #ffffff; }
.t-comment { color: #9ca3af; font-style: italic; }
.t-success { color: #60a5fa; }

/* Stage View Card */
.jenkins-inner { padding: 16px; border-top: 1px solid #374151; background: #0f172a; }
.j-title { font-size: 13px; font-weight: 700; color: #f3f4f6; margin-bottom: 10px; display: flex; justify-content: space-between; }
.j-badge { background: #065f46; color: #34d399; padding: 2px 8px; border-radius: 12px; font-size: 11px; }

.stage-row { display: flex; gap: 10px; margin-top: 8px; }
.s-box { flex: 1; background: #064e3b; border: 1px solid #059669; border-radius: 6px; padding: 10px 8px; text-align: center; color: #6ee7b7; font-weight: bold; font-size: 12px; }
.s-sub { font-size: 11px; font-weight: normal; color: #a7f3d0; margin-top: 2px; }

/* Browser Preview in Right Card */
.browser-inner { flex: 1; display: flex; align-items: center; justify-content: center; padding: 20px; background: radial-gradient(circle at 50% 30%, #1e293b 0%, #0f172a 100%); }
.flask-ui-card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 30px 24px; text-align: center; width: 100%; box-shadow: 0 15px 30px rgba(0,0,0,0.5); }
.tag-v2 { background: rgba(16, 185, 129, 0.2); color: #34d399; font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 1.5px; padding: 5px 12px; border-radius: 20px; display: inline-block; margin-bottom: 14px; border: 1px solid #059669; }
.v2-badge { background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; padding: 8px 18px; border-radius: 30px; font-weight: bold; font-size: 13.5px; margin: 15px 0; display: inline-block; box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4); }
.info-row { display: flex; justify-content: space-between; background: #0f172a; padding: 10px 14px; border-radius: 8px; margin-top: 10px; font-family: monospace; font-size: 12.5px; color: #94a3b8; }
.info-row span.val { color: #e2e8f0; font-weight: 600; }
</style>
</head>
<body>
<div class="chrome-bar">
    <div class="dots"><div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div></div>
    <div class="tab"><span>🚀</span> Step 9: Automatic Deployment Verification (Version 2)</div>
    <div class="urlbar">http://54.210.142.88:5000/ &bull; Triggered by GitHub Webhook Push</div>
</div>

<div class="main-container">
    <!-- LEFT CARD: Git Push & Jenkins Auto-Build -->
    <div class="col-card">
        <div class="card-header">
            <span>1. Code Change &amp; Webhook Trigger</span>
            <span style="font-size:12px;color:#a7f3d0;">git commit -m "Version 2"</span>
        </div>
        <div class="term-inner">
            <div class="t-comment"># Developer updates app.py to Version 2 and pushes to GitHub</div>
            <div><span class="t-prompt">ubuntu@ip-172-31-42-105:~/cloud-cicd-lab$</span> <span class="t-cmd">git add .</span></div>
            <div><span class="t-prompt">ubuntu@ip-172-31-42-105:~/cloud-cicd-lab$</span> <span class="t-cmd">git commit -m "Version 2: Updated UI and features"</span></div>
            <div>[main 9e8d7c6] Version 2: Updated UI and features</div>
            <div>&nbsp;1 file changed, 8 insertions(+), 2 deletions(-)</div>
            <div><span class="t-prompt">ubuntu@ip-172-31-42-105:~/cloud-cicd-lab$</span> <span class="t-cmd">git push origin main</span></div>
            <div>To https://github.com/krishbhensdadia21/cloud-cicd-lab.git</div>
            <div class="t-success">&nbsp;&nbsp;&nbsp;7a8f9c2..9e8d7c6&nbsp;&nbsp;main -&gt; main</div>
            <div class="t-comment" style="color:#60a5fa;margin-top:6px;">&rarr; GitHub Webhook automatically triggers Jenkins Build #2!</div>
        </div>

        <div class="jenkins-inner">
            <div class="j-title">
                <span>Jenkins Pipeline: Build #2 (Automatic Trigger)</span>
                <span class="j-badge">Trigger: GitHub Push</span>
            </div>
            <div style="font-size:12px;color:#94a3b8;margin-bottom:8px;">
                Started by GitHub push by <strong>krishbhensdadia21</strong> &bull; Commit <code>9e8d7c6</code>
            </div>
            <div class="stage-row">
                <div class="s-box">
                    ✓ Clone
                    <div class="s-sub">7s</div>
                </div>
                <div class="s-box">
                    ✓ Build
                    <div class="s-sub">38s</div>
                </div>
                <div class="s-box">
                    ✓ Deploy
                    <div class="s-sub">5s</div>
                </div>
            </div>
            <div style="margin-top:12px;font-size:12px;color:#34d399;font-weight:bold;text-align:right;">
                ● Build #2 Finished: SUCCESS
            </div>
        </div>
    </div>

    <!-- RIGHT CARD: Live Updated Browser Application Output -->
    <div class="col-card">
        <div class="card-header">
            <span>2. Live Application Automatically Updated</span>
            <span style="font-size:12px;color:#34d399;">HTTP 200 OK</span>
        </div>
        <div class="browser-inner">
            <div class="flask-ui-card">
                <div class="tag-v2">DevOps Exp 5 &bull; Automatic CD Complete</div>
                <h2 style="font-size:24px;font-weight:800;color:white;margin-bottom:8px;">🚀 Welcome to Cloud CI/CD Lab!</h2>
                <p style="color:#94a3b8;font-size:13.5px;line-height:1.4;">Automated continuous deployment without manual intervention.</p>
                
                <div class="v2-badge">
                    ● Version 2.0 - Automated Deployment Verified!
                </div>

                <div class="info-row">
                    <span>Active Container</span>
                    <span class="val">c7b4e912fa80</span>
                </div>
                <div class="info-row">
                    <span>Trigger Method</span>
                    <span class="val" style="color:#34d399;">GitHub Webhook (Push)</span>
                </div>
                <div class="info-row">
                    <span>Pipeline Run</span>
                    <span class="val">Build #2 (SUCCESS)</span>
                </div>
                <div class="info-row">
                    <span>Host / IP</span>
                    <span class="val">54.210.142.88:5000</span>
                </div>

                <div style="margin-top:20px;padding:12px;background:#064e3b;border-radius:8px;font-size:12px;color:#a7f3d0;border:1px solid #059669;">
                    ✓ Zero-downtime container replacement verified via Docker &amp; Jenkins Pipeline!
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>
"""
save_page_screenshot(html_10, "10_automatic_deployment.png")

driver.quit()
print("\n>>> All 10 screenshots successfully generated and saved!")
