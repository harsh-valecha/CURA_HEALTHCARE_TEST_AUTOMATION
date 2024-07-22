from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.makeappointment = (By.ID,'btn-make-appointment')
        self.navigationbtn = (By.ID,"menu-toggle")
        self.homebtn = (By.XPATH,"//a[text()='Home']")
        self.loginbtn = (By.XPATH,"//a[text()='Login']")

    def click_appointment(self):
        self.driver.find_element(*self.makeappointment).click()

    def click_home(self):
        self.driver.find_element(*self.homebtn).click()

    def click_login(self):
        self.driver.find_element(*self.loginbtn).click()

    def click_navigation(self):
        self.driver.find_element(*self.navigationbtn).click()

    def home_is_active(self):
        if self.driver.find_element(*self.homebtn).is_displayed()!=0:
            return True
        else:
            return False
        
    def login_is_active(self):
        if self.driver.find_element(*self.loginbtn).is_displayed()!=0:
            return True
        else:
            return False
        
    

    