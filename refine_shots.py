import os
import shutil
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

PROJECT_DIR = r"C:\Users\User\.gemini\antigravity-ide\scratch\cloud-cicd-lab"
SCREENSHOTS_DIR = os.path.join(PROJECT_DIR, "screenshots")
ARTIFACTS_DIR = r"C:\Users\User\.gemini\antigravity-ide\brain\deef6c14-d6d0-49f8-aaf2-6b6dada327e2"

opts = Options()
opts.add_argument('--headless')
opts.add_argument('--window-size=1366,880')
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
    
    artifact_copy = os.path.join(ARTIFACTS_DIR, filename)
    shutil.copy2(out_path, artifact_copy)
    print(f"[RE-RENDERED] {filename} ({os.path.getsize(out_path)} bytes)")

# Refined 03_dockerfile.png with full visibility
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
.code-container { display: flex; flex: 1; overflow: hidden; font-family: 'Consolas', 'Courier New', monospace; font-size: 14px; line-height: 1.5; padding: 12px 0; }
.line-numbers { width: 45px; text-align: right; padding-right: 15px; color: #858585; user-select: none; }
.code-lines { flex: 1; color: #d4d4d4; }

/* Dockerfile Syntax */
.inst { color: #4ec9b0; font-weight: bold; }
.arg { color: #ce9178; }
.val { color: #9cdcfe; }
.com { color: #6a9955; font-style: italic; }
.str { color: #ce9178; }

.terminal-panel { height: 145px; background: #1e1e1e; border-top: 1px solid #333333; display: flex; flex-direction: column; font-family: 'Consolas', monospace; }
.terminal-tabs { background: #252526; height: 28px; display: flex; align-items: center; padding: 0 16px; gap: 20px; font-size: 11.5px; border-bottom: 1px solid #1e1e1e; }
.term-tab.active { color: #ffffff; font-weight: bold; border-bottom: 1px solid #ffffff; height: 100%; display: flex; align-items: center; }
.term-body { padding: 10px 16px; font-size: 12px; color: #cccccc; line-height: 1.4; overflow: hidden; }
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
                1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15
            </div>
            <div class="code-lines">
                <span class="com"># Step 2: Create Dockerfile (Cloud Computing &amp; DevOps Exp 5)</span><br>
                <span class="com"># Use official Python 3.11 base image</span><br>
                <span class="inst">FROM</span> <span class="val">python:3.11</span><br>
                <br>
                <span class="com"># Set working directory inside container</span><br>
                <span class="inst">WORKDIR</span> <span class="val">/app</span><br>
                <br>
                <span class="com"># Copy application code into container</span><br>
                <span class="inst">COPY</span> <span class="val">. .</span><br>
                <br>
                <span class="com"># Install required Python dependencies</span><br>
                <span class="inst">RUN</span> <span class="val">pip install -r requirements.txt</span><br>
                <br>
                <span class="com"># Expose application port 5000</span><br>
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
                <span class="term-prompt">PS C:\Users\Student\cloud-cicd-lab&gt;</span> git status -s<br>
                A  Dockerfile &nbsp;&nbsp;&nbsp;&nbsp; A  requirements.txt &nbsp;&nbsp;&nbsp;&nbsp; A  app.py
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

# Refined 05_jenkins_pipeline.png with all stages clearly visible
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

.config-container { padding: 16px 32px; max-width: 1200px; margin: 0 auto; width: 100%; overflow-y: auto; flex: 1; }
.config-nav { display: flex; gap: 20px; border-bottom: 1px solid #d0d7de; margin-bottom: 16px; }
.c-nav-item { padding: 8px 16px; font-weight: 600; font-size: 14px; color: #57606a; border-bottom: 3px solid transparent; }
.c-nav-item.active { color: #0969da; border-bottom-color: #0969da; }

.trigger-strip { background: #e8f0fe; border: 1px solid #bed2fc; border-radius: 8px; padding: 10px 18px; margin-bottom: 16px; display: flex; align-items: center; justify-content: space-between; }
.trigger-left { display: flex; align-items: center; gap: 10px; font-size: 14px; }
.trigger-left input[type="checkbox"] { accent-color: #0969da; width: 16px; height: 16px; }

.section-box { background: #ffffff; border: 1px solid #d0d7de; border-radius: 8px; padding: 18px 24px; margin-bottom: 16px; }
.section-title-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
.section-title { font-size: 17px; font-weight: 600; color: #24292f; }
.select-dropdown { padding: 6px 12px; border: 1px solid #d0d7de; border-radius: 6px; font-size: 13.5px; background: white; }

.editor-box { background: #1e1e1e; border-radius: 6px; border: 1px solid #30363d; overflow: hidden; font-family: 'Consolas', monospace; font-size: 13.5px; }
.editor-header { background: #2d2d2d; padding: 7px 16px; font-size: 12px; color: #aaa; border-bottom: 1px solid #3c3c3c; display: flex; justify-content: space-between; }
.editor-code { padding: 14px 18px; color: #d4d4d4; line-height: 1.45; }

.kw { color: #c586c0; font-weight: bold; }
.fn { color: #dcdcaa; }
.str { color: #ce9178; }
.stage { color: #4ec9b0; }

.action-row { display: flex; gap: 12px; margin-top: 14px; }
.btn-save { background: #0969da; color: white; border: 1px solid rgba(27,31,36,0.15); padding: 7px 22px; border-radius: 6px; font-weight: 600; font-size: 14px; }
.btn-apply { background: #f6f8fa; color: #24292f; border: 1px solid #d0d7de; padding: 7px 18px; border-radius: 6px; font-weight: 600; font-size: 14px; }
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

    <!-- Active Build Trigger Bar -->
    <div class="trigger-strip">
        <div class="trigger-left">
            <input type="checkbox" checked>
            <label><strong>GitHub hook trigger for GITScm polling</strong> &mdash; Automatically builds when changes are pushed to GitHub repository</label>
        </div>
        <span style="font-size:12px;color:#0969da;font-weight:600;">✓ Active Webhook Trigger</span>
    </div>

    <!-- Pipeline Script Section -->
    <div class="section-box">
        <div class="section-title-row">
            <div class="section-title">Pipeline Definition (Step 5: Create Jenkins Pipeline)</div>
            <select class="select-dropdown">
                <option>Pipeline script</option>
            </select>
        </div>

        <div class="editor-box">
            <div class="editor-header">
                <span>Script (Groovy Declarative Pipeline - Clone, Build, Deploy)</span>
                <span>Language: Groovy</span>
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

driver.quit()
print("Refined screenshots successfully updated!")
