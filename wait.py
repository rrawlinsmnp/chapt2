import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyTestCase(unittest.TestCase):
    def test_something(self):
        FIREFOX_DRIVER_PATH = "C:/Users/Robert.Rawlins/PycharmProjects/chapt2/browser_drivers/geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
        self.driver.get('http://www.python.org')

        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "start-shell"))
            )
        finally:
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
