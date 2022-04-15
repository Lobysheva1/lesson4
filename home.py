from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
Selenium_Ruby = driver.find_element_by_css_selector("[alt='Selenium Ruby']")
Selenium_Ruby.click()
btn_REVIEWS = driver.find_element_by_class_name('reviews_tab')
btn_REVIEWS.click()
star5 = driver.find_element_by_class_name('star-5')
star5.click()
my_review = driver.find_element_by_id('comment')
my_review.send_keys('Nice book!')
name = driver.find_element_by_id('author')
name.send_keys('Irina')
email = driver.find_element_by_id('email')
email.send_keys('sami-s-ysami@yandex.ru')
submit_btn = driver.find_element_by_id('submit')
submit_btn.click
driver.quit()