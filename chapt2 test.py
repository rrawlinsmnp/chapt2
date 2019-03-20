from selenium import webdriver

class MyTestCase(unittest.TestCase):
    def test_something(self):
        FIREFOX_DRIVER_PATH = "C:/Users/Robert.Rawlins/PycharmProjects/chapt2/browser_drivers/geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
        driver.get("file:///C:/Users/Robert.Rawlins/Downloads/Ex_Files_Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html")
login_form = driver.find_element_by_id('loginForm')
print("My login form element is:")
print(login_form)
driver.close()

if __name__ == '__main__':
   unittest.main()
