from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
button_element = browser.find_element(By.CSS_SELECTOR, "#book")

try:
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
#        EC.element_to_be_clickable((By.ID, "verify"))
    )
    button_element.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(calc(x_element.text))

    button_element = browser.find_element(By.CSS_SELECTOR, "button#solve")
    button_element.click()

finally:
    time.sleep(10)
    browser.quit()
