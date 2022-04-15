from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
username = driver.find_element_by_id('username')
username.send_keys('sami-s-ysami@yandex.ru')
password = driver.find_element_by_id('password')
password.send_keys('$Lobysheva123')
time.sleep(1)
login_btn = driver.find_element_by_xpath('//input[@value="Login"]')
login_btn.click()
time.sleep(5)
elementByPartialLinkText = driver.find_element_by_partial_link_text("Logout")
driver.quit()



