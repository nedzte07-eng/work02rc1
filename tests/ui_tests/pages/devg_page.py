from playwright.sync_api import Page

class DevgPage:
    def __init__(self, page:Page):
        self._page = page
        self._title = page.locator('h4.page-title')

    def get_title(self):
        return self._title