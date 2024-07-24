import pytest
from utils.config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from .test_login import test_login
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

count = 0
facility = ["Tokyo CURA Healthcare Center","Hongkong CURA Healthcare Center","Seoul CURA Healthcare Center"]
program = ["medicare","medicaid","none"]

# simple testcase for checking home
def test_home(driver):
    driver.get(Config.BASE_URL)

    home_page = HomePage(driver)
    home_page.click_appointment()
    expected_url = 'https://katalon-demo-cura.herokuapp.com/profile.php#login'
    assert driver.current_url == expected_url  ,f"URL mismatch: expected {expected_url}, got {driver.current_url}"
    return driver

# testcase for navigate to home
@pytest.mark.navhome
def test_home_navigation(driver):
    driver.get(Config.BASE_URL)
    home_page = HomePage(driver)
    if home_page.home_is_active():
        home_page.click_home()
        assert driver.current_url == Config.BASE_URL
    else:
        home_page.click_navigation()
        home_page.click_home()
        assert driver.current_url == Config.BASE_URL

# test case for moving from home to login
@pytest.mark.navlogin
def test_login_navigation(driver):
    driver.get(Config.BASE_URL)
    home_page = HomePage(driver)
    if home_page.login_is_active():
        home_page.click_login()
        assert driver.current_url == Config.LOGIN_URL
    else:
        home_page.click_navigation()
        home_page.click_login()
        assert driver.current_url == Config.LOGIN_URL
    


# testcase for validating logout functionality
@pytest.mark.logout
def test_logout(driver):
    driver = test_login(driver)
    home_page = HomePage(driver)
    home_page.click_navigation()
    if home_page.logout_is_active():
        home_page.click_logout()
        assert driver.current_url == Config.BASE_URL
        return driver

# reading test data from test_data.json    
with open("test_data.json") as f:
    test_data = json.load(f)


# testcase for Registration 
@pytest.mark.parametrize("data",test_data)
def test_registration(driver ,data):
    driver.get(Config.LOGIN_URL)
    login_page = LoginPage(driver)
    login_page.enter_username(Config.username)
    login_page.enter_password(Config.password)
    login_page.click_login()
    home_page = HomePage(driver,facility=data['facility'],program=data['program'])
    home_page.select_facility()
    home_page.check_readmission() if data['readmission'] else None
    home_page.click_program()
    home_page.type_visitdate(data['visit_date'])
    home_page.type_comment(data['comment'])
    home_page.click_bookappointment()

    assert home_page.appointment_is_confirmed()== True
    # Wait for the "Go to Homepage" button to be clickable
    wait = WebDriverWait(driver, 10)
    go_home_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[.='Go to Homepage']")))
    go_home_btn.click()
    
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"

    
    
    


