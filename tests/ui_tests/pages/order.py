from playwright.sync_api import Page

class OrderPage:
    def __init__(self, page:Page):
        self._page = page
        self._title = page.locator('h4.page-title')
        self._create_button = page.locator('//a[contains(@href,"/admin/order/create")]')

    def get_title(self):
        return self._title

    def create_button_click(self):
        self._create_button.click()
        from tests.ui_tests.pages.order_create import OrderCreatePage
        return OrderCreatePage(self._page)








