import pytest
from utils.config import Config
from pages.home_page import HomePage

# simple testcase for checking home
def test_home(driver):
    driver.get(Config.BASE_URL)

    home_page = HomePage(driver)
    home_page.click_appointment()
    expected_url = 'https://katalon-demo-cura.herokuapp.com/profile.php#login'
    assert driver.current_url == expected_url  ,f"URL mismatch: expected {expected_url}, got {driver.current_url}"
    

# testcase for vaigate to home
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


