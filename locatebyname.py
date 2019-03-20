import unittest
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    def test_something(self):
        FIREFOX_DRIVER_PATH = "C:/Users/Robert.Rawlins/PycharmProjects/chapt2/browser_drivers/geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
        self.driver.get("http://seleniumhq.org")
        element_id = self.driver.find_element_by_id('q')
        print(element_id)

        element_name = self.driver.find_element_by_name('q')
        print(element_name)

        heading_xpath = self.driver.find_element_by_xpath("//*[@id='mainContent;]/h2[1]")
        print(heading_xpath)

        element_classname = driver.find_element_by_class_name('selenium-sponsors')
        print(element_classname)

        self.driver.close()

if __name__ == '__main__':
   unittest.main()
