from playwright.sync_api import Page, expect

class AdminPage:
    def __init__(self, page:Page):
        self._page = page
        self._logo = page.locator('span.logo-name')
        self._order_link = page.locator('//a[@class="side-nav-link active" and contains(@href,"/admin/order")]')

    def get_logo(self):
        #to check if logo is present
        return self._logo

