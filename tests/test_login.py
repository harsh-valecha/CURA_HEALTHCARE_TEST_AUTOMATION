import pytest
from utils.config import Config
from pages.login_page import LoginPage
from users.credentials import UserCredentials


def test_login(driver):
    driver.get(Config.LOGIN_URL)
    
    login_page = LoginPage(driver)
    login_page.enter_username(UserCredentials.username)
    login_page.enter_password(UserCredentials.password)
    login_page.click_login()
    expected_url = 'https://katalon-demo-cura.herokuapp.com/#appointment'
    assert driver.current_url == expected_url , f"URL mismatch: expected {expected_url}, got {driver.current_url}"
