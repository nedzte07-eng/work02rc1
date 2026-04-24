from playwright.sync_api import Page, expect

class AdminPage:
    def __init__(self, page:Page):
        self._page = page
        self._logo = page.locator('span.logo-name')

    def get_logo(self):
        #to check if logo is present
        return self._logo

