from playwright.sync_api import Page, expect

class LoginPage:
    """የመግቢያ ገጽ አካላት በአንድ ቦታ ተሰብስበዋል።
    ገጹ ሲቀየር ይህ ፋይል ብቻ ይስተካከላል፣ ፈተናዎቹ አይነኩም።"""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.saucedemo.com"
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def goto(self):
        self.page.goto(self.url, timeout=60000)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_success(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def expect_error(self, text: str):
        expect(self.error_message).to_contain_text(text)
