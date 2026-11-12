import pytest
from pages.login_page import LoginPage


def test_successful_login(page):
    """TC-01: ትክክለኛ መግቢያ → ወደ ምርቶች ገጽ መሄድ አለበት"""
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    login.expect_success()
    print("\n✅ TC-01 PASSED: ትክክለኛ ተጠቃሚ ወደ ምርቶች ገጽ ገብቷል")


def test_locked_out_user(page):
    """TC-02: የተቆለፈ ተጠቃሚ → የስህተት መልእክት ማሳየት አለበት"""
    login = LoginPage(page)
    login.goto()
    login.login("locked_out_user", "secret_sauce")
    login.expect_error("Sorry, this user has been locked out")
    print("✅ TC-02 PASSED: የተቆለፈ ተጠቃሚ በትክክል ተከልክሏል")


def test_invalid_password(page):
    """TC-03: የተሳሳተ የይለፍ ቃል → የስህተት መልእክት ማሳየት አለበት"""
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "wrong_password")
    login.expect_error("Username and password do not match")
    print("✅ TC-03 PASSED: የተሳሳተ የይለፍ ቃል በትክክል ተከልክሏል")


def test_empty_credentials(page):
    """TC-04: ባዶ መስኮች → 'Username is required' ማሳየት አለበት"""
    login = LoginPage(page)
    login.goto()
    login.login("", "")
    login.expect_error("Username is required")
    print("✅ TC-04 PASSED: ባዶ መስኮች በትክክል ተከልክለዋል")
