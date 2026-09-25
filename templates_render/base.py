import os
import shutil
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

# Directories
PROJECT_DIR = r"C:\Users\User\.gemini\antigravity-ide\scratch\cloud-cicd-lab"
SCREENSHOTS_DIR = os.path.join(PROJECT_DIR, "screenshots")
ARTIFACTS_DIR = r"C:\Users\User\.gemini\antigravity-ide\brain\deef6c14-d6d0-49f8-aaf2-6b6dada327e2"
TEMPLATES_DIR = os.path.join(PROJECT_DIR, "templates_render")

os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# Common SVG Icons and Components
SVG_GITHUB_LOGO = '<svg height="24" viewBox="0 0 16 16" width="24" fill="currentColor"><path d="M8 0c4.42 0 8 3.58 8 8a8.01 8.01 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9 1.05 1.34.36.5 1.23.95 2.5.73 0 .68.01 1.25.01 1.43 0 .21-.15.46-.55.38A8.01 8.01 0 0 1 0 8c0-4.42 3.58-8 8-8z"></path></svg>'
SVG_JENKINS_ICON = '<svg width="28" height="28" viewBox="0 0 40 40"><circle cx="20" cy="20" r="18" fill="#D33833"/><path d="M12 16c0-4.4 3.6-8 8-8s8 3.6 8 8c0 2.2-.9 4.2-2.3 5.7L24 30h-8l-1.7-8.3C12.9 20.2 12 18.2 12 16z" fill="#FFF"/><circle cx="17" cy="15" r="1.5" fill="#333"/><circle cx="23" cy="15" r="1.5" fill="#333"/><path d="M18 19h4v2h-4z" fill="#D33833"/></svg>'
SVG_DOCKER_ICON = '<svg width="24" height="24" viewBox="0 0 24 24" fill="#0db7ed"><path d="M13.983 11.078h2.119a.186.186 0 00.186-.185V9.006a.186.186 0 00-.186-.186h-2.119a.185.185 0 00-.185.185v1.888c0 .102.083.185.185.185m-2.954-5.43h2.118a.186.186 0 00.186-.186V3.574a.186.186 0 00-.186-.185h-2.118a.185.185 0 00-.185.185v1.888c0 .102.082.186.185.186zm0 2.715h2.118a.186.186 0 00.186-.186V6.289a.186.186 0 00-.186-.185h-2.118a.185.185 0 00-.185.185v1.888c0 .102.082.186.185.186zm-2.955 0h2.119a.186.186 0 00.186-.186V6.289a.186.186 0 00-.186-.185H8.074a.185.185 0 00-.185.185v1.888c0 .102.083.186.185.186zm0 2.715h2.119a.186.186 0 00.186-.185V9.006a.186.186 0 00-.186-.186H8.074a.185.185 0 00-.185.185v1.888c0 .102.083.185.185.185zm-2.954 0h2.118a.186.186 0 00.186-.185V9.006a.186.186 0 00-.186-.186H5.12a.185.185 0 00-.185.185v1.888c0 .102.083.185.185.185zm8.863-2.715h2.119a.186.186 0 00.186-.186V6.289a.186.186 0 00-.186-.185h-2.119a.185.185 0 00-.185.185v1.888c0 .102.083.186.185.186zm-5.909 5.43h2.119a.186.186 0 00.186-.185V11.72a.186.186 0 00-.186-.185H8.074a.185.185 0 00-.185.185v1.888c0 .102.083.185.185.185zm2.955 0h2.118a.186.186 0 00.186-.185V11.72a.186.186 0 00-.186-.185h-2.118a.185.185 0 00-.185.185v1.888c0 .102.082.185.185.185zm10.992.836c-.463-.33-1.637-.414-2.527-.247-.197-.894-.789-1.652-1.656-2.103l-.482-.249-.333.428c-.584.752-.947 1.67-.993 2.65-.589.043-1.57.147-2.158.48-1.077.61-1.39 1.748-1.583 2.766-.192 1.018-.18 2.062-.127 3.098.053 1.036.147 2.083.35 3.094.204 1.01.554 1.986 1.042 2.871.488.885 1.134 1.664 1.93 2.279.796.615 1.748 1.037 2.775 1.218 1.026.18 2.11.131 3.14-.145 1.03-.277 1.99-.787 2.784-1.48.793-.692 1.41-1.564 1.785-2.535.375-.972.483-2.046.33-3.09-.153-1.044-.576-2.036-1.228-2.87-.652-.835-1.51-1.47-2.486-1.834z"/></svg>'

def create_browser_wrapper(url, tab_title, inner_html, window_title="Edge"):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
    background: #18181b;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #e4e4e7;
    margin: 0;
    padding: 0;
    overflow-x: hidden;
}}
.browser-window {{
    width: 100%;
    min-height: 100vh;
    background: #09090b;
    display: flex;
    flex-direction: column;
}}
.browser-titlebar {{
    background: #18181b;
    height: 40px;
    display: flex;
    align-items: center;
    padding: 0 16px;
    border-bottom: 1px solid #27272a;
    gap: 12px;
}}
.window-controls {{
    display: flex;
    gap: 8px;
}}
.control-dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;
}}
.control-red {{ background: #ef4444; }}
.control-yellow {{ background: #eab308; }}
.control-green {{ background: #22c55e; }}
.browser-tabs {{
    display: flex;
    align-items: center;
    gap: 6px;
    margin-left: 12px;
}}
.browser-tab {{
    background: #27272a;
    color: #f4f4f5;
    font-size: 13px;
    padding: 6px 14px;
    border-radius: 6px 6px 0 0;
    display: flex;
    align-items: center;
    gap: 8px;
    max-width: 320px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    border-top: 2px solid #38bdf8;
}}
.browser-addressbar {{
    background: #27272a;
    height: 38px;
    display: flex;
    align-items: center;
    padding: 0 16px;
    gap: 14px;
    border-bottom: 1px solid #3f3f46;
}}
.nav-arrows {{
    display: flex;
    gap: 12px;
    color: #a1a1aa;
    font-size: 16px;
    cursor: default;
}}
.url-bar {{
    flex: 1;
    background: #18181b;
    border: 1px solid #3f3f46;
    border-radius: 20px;
    padding: 4px 16px;
    font-size: 13px;
    color: #e4e4e7;
    display: flex;
    align-items: center;
    gap: 8px;
    font-family: monospace;
}}
.lock-icon {{
    color: #10b981;
    font-size: 12px;
}}
.browser-content {{
    flex: 1;
    overflow: auto;
    background: #0d1117;
}}
</style>
</head>
<body>
<div class="browser-window">
    <div class="browser-titlebar">
        <div class="window-controls">
            <span class="control-dot control-red"></span>
            <span class="control-dot control-yellow"></span>
            <span class="control-dot control-green"></span>
        </div>
        <div class="browser-tabs">
            <div class="browser-tab">
                <span>🌐</span>
                <span>{tab_title}</span>
            </div>
        </div>
    </div>
    <div class="browser-addressbar">
        <div class="nav-arrows">
            <span>&larr;</span>
            <span>&rarr;</span>
            <span>&#x21bb;</span>
        </div>
        <div class="url-bar">
            <span class="lock-icon">&#128274;</span>
            <span>{url}</span>
        </div>
        <div style="font-size:16px;color:#a1a1aa;">&#x22ee;</div>
    </div>
    <div class="browser-content">
        {inner_html}
    </div>
</div>
</body>
</html>"""

print("Browser wrapper helper ready.")
