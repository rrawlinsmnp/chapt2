import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

class MyTestCase(unittest.TestCase):
    def test_something(self):
        FIREFOX_DRIVER_PATH = "C:/Users/Robert.Rawlins/PycharmProjects/chapt2/browser_drivers/geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
        self.driver.get("file:///C:/Users/Robert.Rawlins/Downloads/Ex_Files_Python_Automation_Testing/Exercise%20Files/CH03/03_02/html_code_03_02.html")
        select = Select(self.driver.find_element_by_name('numReturnSelect'))
        select.select_by_index(4)
        time.sleep(4)
        select.select_by_visible_text("200")
        time.sleep(4)
        select.select_by_value("250")
        time.sleep(4)
        options = select.options
        print(options)
        submit_button = self.driver.find_element_by_name('continue')
        submit_button.submit();
        time.sleep(4)
        self.driver.close()

if __name__ == '__main__':
   unittest.main()
