from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    button_element = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_element.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(calc(x_element.text))

    button_element = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_element.click()

finally:
    time.sleep(10)
    browser.quit()
