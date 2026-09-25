import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options

PROJECT_DIR = r"C:\Users\User\.gemini\antigravity-ide\scratch\cloud-cicd-lab"
SCREENSHOTS_DIR = os.path.join(PROJECT_DIR, "screenshots")
ARTIFACTS_DIR = r"C:\Users\User\.gemini\antigravity-ide\brain\deef6c14-d6d0-49f8-aaf2-6b6dada327e2"

opts = Options()
opts.add_argument('--headless')
opts.add_argument('--window-size=1366,880')

driver = webdriver.Edge(options=opts)

# 1. Snap REAL LIVE Application Output
app_url = "http://43.204.114.6:5000"
driver.get(app_url)
out_real_app = os.path.join(SCREENSHOTS_DIR, "08_application_output_live.png")
driver.save_screenshot(out_real_app)
print(f"[LIVE CAPTURED] Real Flask App Output from {app_url} -> {out_real_app}")

# 2. Snap REAL LIVE Jenkins Login Screen
jenkins_url = "http://43.204.114.6:8080/login"
driver.get(jenkins_url)
out_real_jenkins = os.path.join(SCREENSHOTS_DIR, "04_jenkins_dashboard_live.png")
driver.save_screenshot(out_real_jenkins)
print(f"[LIVE CAPTURED] Real Jenkins Login from {jenkins_url} -> {out_real_jenkins}")

driver.quit()
