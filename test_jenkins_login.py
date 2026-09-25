import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument('--headless')
opts.add_argument('--window-size=1366,880')

driver = webdriver.Edge(options=opts)

# 1. Login to Jenkins
login_url = "http://43.204.114.6:8080/login"
driver.get(login_url)
time.sleep(2)

print("Title on login page:", driver.title)
try:
    user_input = driver.find_element(By.NAME, "j_username")
    pass_input = driver.find_element(By.NAME, "j_password")
    user_input.send_keys("admin")
    pass_input.send_keys("admin123")
    
    submit_btn = driver.find_element(By.NAME, "Submit")
    submit_btn.click()
    time.sleep(3)
    
    print("Logged in successfully! Current URL:", driver.current_url)
    print("Page Title:", driver.title)
    driver.save_screenshot("jenkins_logged_in.png")
except Exception as e:
    print("Login exception:", e)
    driver.save_screenshot("login_failed.png")

driver.quit()
