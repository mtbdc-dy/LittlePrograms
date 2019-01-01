from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
# The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


driver = Chrome()
driver.implicitly_wait(10)
driver.get("https://39.134.87.216:31943/pm/themes/default/pm/app/i2000_monitorView_pm.html?curMenuId=com.iemp.app.pm.monitorView&_=1545967221368#group_152734715982719")
# print(driver.page_source)
usr = driver.find_element_by_xpath("//*[@id=\"username\"]")
usr.send_keys("admin")
pw = driver.find_element_by_xpath("//*[@id=\"password\"]")
pw.send_keys("HuaWei12#$")
captcha = driver.find_element_by_xpath("//*[@id=\"validate\"]")
vc = input('输入网页上的验证码')
captcha.send_keys(vc)
captcha.send_keys(Keys.RETURN)

button = driver.find_element_by_css_selector('#treeDiv_1_switch')
button.click()
print(driver.get_cookies())
print(type(driver.get_cookies()))
for item in driver.get_cookies():
    # print(item)
    if item['name'] == 'JSESSIONID':
        cookie = 'JSESSIONID=' + item['value']

print(cookie)

driver.close()
