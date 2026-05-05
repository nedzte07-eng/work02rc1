from playwright.sync_api import Page

class DevgPage:
    def __init__(self, page:Page):
        self._page = page
        self._title = page.locator('h4.page-title')
        self._travelers = page.locator('a.nav-link[href="#travelers"]')
        self._save_travelers = page.get_by_role("button", name="Save Travelers")

    def get_title(self):
        return self._title

    def click_travelers(self):
        self._travelers.click()

    def get_save_travelers(self):
        return self._save_travelers

class TravelersTab(DevgPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._counter = page.locator('a.nav-link[href="#travelers"] span.order-edit__counter')

    def get_counter_value(self):
        return self._counter.inner_text()

    def save_travelers(self):
        self._save_travelers.click()

