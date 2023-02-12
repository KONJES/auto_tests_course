import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    secWindow = browser.window_handles[1]
    browser.switch_to.window(secWindow)

    x = browser.find_element(By.ID, "input_value").text
    res = calc(x)
    browser.find_element(By.ID, "answer").send_keys(res)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

except Exception as e:
    print(e)

finally:
    time.sleep(10)
    browser.quit()
