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

    def login_octoprint(self):
        self.driver.find_element_by_id("navbar_plugin_oauth2").click()
        self.driver.find_element_by_id("loginForm").click()

    def login_server(self):
        self.assertIn("github", self.driver.current_url)
        self.driver.find_element_by_id("login_field").send_keys(USERNAME)
        self.driver.find_element_by_id("password").send_keys("FITtest1234")
        self.driver.find_element_by_name("commit").click()

    def test_login_OK(self):

        self.driver.get("http://0.0.0.0:5000/")

        self.login_octoprint()
        self.login_server()
        time.sleep(3)

        #give information to application
        if "github" in self.driver.current_url:
            self.driver.find_element_by_id("js-oauth-authorize-btn").click()

        list = self.driver.find_elements_by_xpath("// text()[contains(., '"+ USERNAME +"')] / ancestor::a[1]")
        self.assertEqual(list.__len__(), 1)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()