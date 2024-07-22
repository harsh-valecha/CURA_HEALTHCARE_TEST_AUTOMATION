from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver,facility=None,program = None):
        self.driver = driver
        self.make_appointment_btn = (By.ID,'btn-make-appointment')
        self.navigation_btn = (By.ID,"menu-toggle")
        self.home_btn = (By.XPATH,"//a[text()='Home']")
        self.login_btn = (By.XPATH,"//a[text()='Login']")
        self.logout_btn = (By.XPATH,"//a[text()='Logout']")
        self.facility_dropdown = (By.ID,"combo_facility")
        self.facility_value = (By.XPATH,f"//option[@value='{facility}']")
        self.readmission_check = (By.ID,"chk_hospotal_readmission")
        self.program_radio = (By.ID,f"radio_program_{program}")
        self.visitdate_txt = (By.ID,"txt_visit_date")
        self.comment_txt = (By.ID,"txt_comment")
        self.bookappointment_btn = (By.ID,"btn-book-appointment")
        self.appointment_confirmation_label = (By.XPATH,"//h2[text()='Appointment Confirmation']")
        self.go_home_btn = (By.XPATH,"//a[.='Go to Homepage']")


    def click_appointment(self):
        self.driver.find_element(*self.make_appointment_btn).click()

    def click_home(self):
        self.driver.find_element(*self.home_btn).click()

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def click_navigation(self):
        self.driver.find_element(*self.navigation_btn).click()

    def home_is_active(self):
        if self.driver.find_element(*self.home_btn).is_displayed()!=0:
            return True
        else:
            return False
        
    def login_is_active(self):
        if self.driver.find_element(*self.login_btn).is_displayed()!=0:
            return True
        else:
            return False
        
    
    def logout_is_active(self):
        if self.driver.find_element(*self.logout_btn).is_displayed()==True:
            return True
        else:
            return False

    def click_logout(self):
        self.driver.find_element(*self.logout_btn).click()
    

    def select_facility(self):
        self.driver.find_element(*self.facility_value).click()

    def check_readmission(self):
        self.driver.find_element(*self.readmission_check).click()

    def click_program(self):
        self.driver.find_element(*self.program_radio).click()

    def type_visitdate(self,date):
        self.driver.find_element(*self.visitdate_txt).send_keys(date)

    def type_comment(self,comment):
        self.driver.find_element(*self.comment_txt).send_keys(comment)

    def click_bookappointment(self):
        self.driver.find_element(*self.bookappointment_btn).click()

    def appointment_is_confirmed(self):
        if self.driver.find_element(*self.appointment_confirmation_label).is_displayed()==True:
            return True
        else:
            return False
        

    def click_go_to_home(self):
        self.driver.find_element(*self.go_home_btn).click()