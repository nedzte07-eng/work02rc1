from playwright.sync_api import Page

class AdminPage:
    def __init__(self, page:Page):
        self._page = page
        self._logo = page.locator('span.logo-name')
        self._order_link = page.locator('//a[@class="side-nav-link" and contains(@href,"/admin/order")]')

    def get_logo(self):
        #to check if logo is present
        return self._logo

    def order_link_click(self):
        self._order_link.click()
        from tests.ui_tests.pages.order import OrderPage
        return OrderPage(self._page)





