import os

from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv()


class LogInPage:
    def __init__(self, page: Page):
        self.page = page

        self._email_input = page.locator('input[name="email"]')
        self._password_input = page.locator('input[name="password"]')
        self._login = page.locator('button[type="submit"]')
        self._ui_url = os.getenv("RC1_ORION") + "login"

    def navigate(self):
        """Метод для переходу на сторінку"""
        self.page.goto(self._ui_url)
        return self

    def login_button(self):
        self._login.click()
        from tests.ui_tests.admin import AdminPage
        return AdminPage(self.page)

    def enter_email(self, email: str):
        self._email_input.fill(email)
        return self

    def enter_password(self, password: str):
        self._password_input.fill(password)
        return self

    def login(self, email: str, password: str):
        self.enter_email(email)
        self.enter_password(password)
        return self.login_button()
