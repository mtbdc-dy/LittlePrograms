from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.keys import Keys
# The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.


class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigate to %s" % url)

    def after_navigate_to(self, url, driver):
        print("After navigate to %s" % url)


profile = webdriver.FirefoxProfile('6wg635ft.default')
profile.accept_untrusted_certs = True
driver = Firefox(firefox_profile=profile)
driver.get("https://39.134.87.216:31943/itpaas/login.action")
# print(driver.page_source)
usr = driver.find_element_by_xpath("//*[@id=\"username\"]")
usr.send_keys("admin")
pw = driver.find_element_by_xpath("//*[@id=\"password\"]")
pw.send_keys("HuaWei12#$")
captcha = driver.find_element_by_xpath("//*[@id=\"validate\"]")
vc = input('输入网页上的验证码')
captcha.send_keys(vc)
captcha.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
