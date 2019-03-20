import unittest
from selenium import webdriver
import time
from selenium.webdriver import ActionChains

class MyTestCase(unittest.TestCase):
    def test_something(self):
        FIREFOX_DRIVER_PATH = "C:/Users/Robert.Rawlins/PycharmProjects/chapt2/browser_drivers/geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
        self.driver.get('http://jqueryui.com/droppable')
        self.driver.switch_to.frame(0)

        action_chains= ActionChains (driver)

        source= self.driver.find_element_by_id('draggable')
        target= self.driver.find_element_by_id('droppable')
        action_chains.drag_and_drop_by_offset(source, 100, 100).perform()
        time.sleep(2)
        action_chains.drag_and_drop(source, target).perform()
        time.sleep(2)


        self.driver.close()

if __name__ == '__main__':
   unittest.main()
