import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class MyTestCase(unittest.TestCase):
    def test_something(self):
        FIREFOX_DRIVER_PATH = "C:/Users/Robert.Rawlins/PycharmProjects/chapt2/browser_drivers/geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
        self.driver.get('https://www.google.com/')
        signin = self.driver.find_element_by_id('signin-standard')
        signin.click();
               time.sleep(10)


        self.driver.close();

if __name__ == '__main__':
   unittest.main()
