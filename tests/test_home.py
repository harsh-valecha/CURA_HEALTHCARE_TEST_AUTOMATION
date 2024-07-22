import pytest
from utils.config import Config
from pages.home_page import HomePage
from .test_login import test_login

facility = ["Tokyo CURA Healthcare Center","Hongkong CURA Healthcare Center","Seoul CURA Healthcare Center"]
program = ["medicare","medicaid","none"]

# simple testcase for checking home
def test_home(driver):
    driver.get(Config.BASE_URL)

    home_page = HomePage(driver)
    home_page.click_appointment()
    expected_url = 'https://katalon-demo-cura.herokuapp.com/profile.php#login'
    assert driver.current_url == expected_url  ,f"URL mismatch: expected {expected_url}, got {driver.current_url}"
    

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
        assert driver.current_url == Config.BASE_URL

# testcase for validating logout functionality
@pytest.mark.logout
def test_logout(driver):
    driver = test_login(driver)
    home_page = HomePage(driver)
    home_page.click_navigation()
    if home_page.logout_is_active():
        home_page.click_logout()
        assert driver.current_url == Config.BASE_URL
    
# testcase for Registration 
def test_registration(driver):
    driver = test_login(driver)
    home_page = HomePage(driver,facility=facility[0],program=program[1])
    home_page.select_facility()
    home_page.check_readmission()
    home_page.click_program()
    home_page.type_visitdate('21.02.2024')
    home_page.type_comment('Book it !!')
    home_page.click_bookappointment()
    assert home_page.appointment_is_confirmed()== True



