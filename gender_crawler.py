# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def getGender(driver, id):
    driver.get("https://www.facebook.com/"+id)
    about_url = driver.find_element_by_xpath('//a[@data-tab-key="about"]').get_attribute("href")
    driver.get(about_url)
    time.sleep(2)
    gender_text = driver.find_element_by_xpath('(//li[@class="_47_-"])[3]').get_attribute("title")
    print('User {} : {}'.format( id, gender_dict[gender_text[0].encode('utf-8')]))


gender_dict = {'他': 'male', '她': 'female'}

search_id_list = ['100000185072960','100002605871033']

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")

# Login
email = driver.find_element_by_name("email")
passwd = driver.find_element_by_name("pass")
email.clear()
email.send_keys("YOUR_FB_EMAIL")
passwd.clear()
passwd.send_keys("YOUR_FB_PASSWD")
passwd.send_keys(Keys.RETURN)
time.sleep(2)


# Go through user
for id in search_id_list:
    getGender(driver, id)

driver.close()
