from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'txt-username')
        self.password_input = (By.ID, 'txt-password')
        self.login_button = (By.ID, 'btn-login')
        self.error_label = (By.XPATH,"//p[@class='lead text-danger']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error(self):
        error_text = self.driver.find_element(*self.error_label).text
        return error_text

    
