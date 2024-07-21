from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.makeappointment = (By.ID,'btn-make-appointment')

    def click_appointment(self):
        self.driver.find_element(*self.makeappointment).click()


    