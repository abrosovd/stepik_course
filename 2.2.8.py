import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"][required]')
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"][required]')
    last_name.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, '[name="email"][required]')
    email.send_keys("petrov@example.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    file_element = browser.find_element(By.CSS_SELECTOR, '#file')
    file_element.send_keys(file_path)
    button_element = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button_element.click()

finally:
    time.sleep(10)
    browser.quit()
