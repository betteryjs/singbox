

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(
   options=chrome_options
)




username="2024200572"
password="000000"

# 打开百度网页
driver.get("http://10.10.11.2")

time.sleep(5)

driver.find_element(By.ID,"username").send_keys(username)
driver.execute_script("""
document.getElementById('pwd').style.display='block';
document.getElementById('pwd').style.float='left';
document.getElementById('pwd').style.width='240px';
""")

driver.find_element(By.ID, "pwd").send_keys(password)
driver.find_element(By.ID, "loginLink_div").click()

time.sleep(20)

driver.close()



