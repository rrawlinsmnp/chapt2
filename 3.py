import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class MyTestCase(unittest.TestCase):
    def test_something(self):
        FIREFOX_DRIVER_PATH = "C:/Users/Robert.Rawlins/PycharmProjects/chapt2/browser_drivers/geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
        self.driver.get("http://python.org")
        search = self.driver.find_element_by_name('q')
        search.clear();
        search.send_keys("pycon");
        search.send_keys(Keys.RETURN);
        time.sleep(4)
        self.driver.close()

if __name__ == '__main__':
   unittest.main()
