import pytest
from utils.config import Config
from pages.login_page import LoginPage
from users.credentials import UserCredentials

@pytest.mark.login
def test_login(driver):
    driver.get(Config.LOGIN_URL)
    
    login_page = LoginPage(driver)
    login_page.enter_username(UserCredentials.username)
    login_page.enter_password(UserCredentials.password)
    login_page.click_login()
    try:
        if login_page.get_error():
            print(login_page.get_error())
            assert False,"This is error due to invalid credentials"
    except Exception as e:
        print(f'Error label not found :{e.with_traceback}')
    
    finally:
        expected_url = 'https://katalon-demo-cura.herokuapp.com/#appointment'
        assert driver.current_url == expected_url , f"URL mismatch: expected {expected_url}, got {driver.current_url}"
