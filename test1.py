from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
import time

USERNAME = "fitctuoauth"

class TestOctoPrintOAuth2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/hany/Downloads/chromedriver")
        self.driver.implicitly_wait(10)

    def test_login(self):
        driver = self.driver

        driver.get("http://0.0.0.0:5000/")
        driver.find_element_by_id("navbar_plugin_oauth2").click()
        driver.find_element_by_id("loginForm").click()

        self.assertIn("github", driver.current_url)
        driver.find_element_by_id("login_field").send_keys(USERNAME)
        driver.find_element_by_id("password").send_keys("FITtest1234")
        driver.find_element_by_name("commit").click()
        time.sleep(3)

        #give information to application
        if "github" in driver.current_url:
            driver.find_element_by_id("js-oauth-authorize-btn").click()

        # print (driver.find_elements_by_xpath("//text()[contains(.,'fitctuoauth')]/ancestor::a[1]"))
        # // text()[contains(., 'Hanyman8')] / ancestor::a[1]
        list = driver.find_elements_by_xpath("// text()[contains(., '"+ USERNAME +"')] / ancestor::a[1]")
        print(list.__len__())
        self.assertEqual(list.__len__(), 1)

# assert "fitctuoauth" in get_text_excluding_children(driver,"ui-pnotify-text")


if __name__ == '__main__':
    unittest.main()