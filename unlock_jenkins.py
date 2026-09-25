import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument('--headless')
opts.add_argument('--window-size=1366,880')

driver = webdriver.Edge(options=opts)

unlock_url = "http://43.204.114.6:8080"
driver.get(unlock_url)
time.sleep(2)

print("Title:", driver.title)
try:
    pass_input = driver.find_element(By.ID, "security-token")
    pass_input.clear()
    pass_input.send_keys("2760c00a9ef640479354723e8f614d61")
    time.sleep(1)
    
    # Click Continue button
    continue_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]")
    continue_btn.click()
    print("Clicked Continue!")
    time.sleep(6)
    
    print("New URL:", driver.current_url)
    print("New Title:", driver.title)
    driver.save_screenshot("jenkins_unlocked_step2.png")
except Exception as e:
    print("Error:", e)
    driver.save_screenshot("unlock_error.png")

driver.quit()
