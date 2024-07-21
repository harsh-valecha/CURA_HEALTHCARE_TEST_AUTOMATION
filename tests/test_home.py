import pytest
from utils.config import Config
from pages.home_page import HomePage


def test_home(driver):
    driver.get(Config.BASE_URL)

    home_page = HomePage(driver)
    home_page.click_appointment()
    expected_url = 'https://katalon-demo-cura.herokuapp.com/profile.php#login'
    assert driver.current_url == expected_url  ,f"URL mismatch: expected {expected_url}, got {driver.current_url}"
    