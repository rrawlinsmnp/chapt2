import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MyTestCase(unittest.TestCase):
    def test_something(self):
        FIREFOX_DRIVER_PATH = "C:/Users/Robert.Rawlins/PycharmProjects/chapt2/browser_drivers/geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
        self.driver.get('https://www.westjet.com/en-ca/index')

        signin = self.driver.find_element_by_id('signin-standard')
        signin.click()

        self.driver.find_element_by_name('username').send_keys('robert.rawlins@mnp.ca')
        self.driver.find_element_by_name('password').send_keys('wagesofsin73')
        self.driver.find_element_by_xpath('//*[@id="sign-in-form"]/div[5]/input').click()

        try:
            element= WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "main"))
            )
        finally:
            self.driver.quit()

        self.driver.close();

if __name__ == '__main__':
   unittest.main()
