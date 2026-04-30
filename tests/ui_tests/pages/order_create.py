from playwright.sync_api import Page

class OrderCreatePage:
    def __init__(self, page:Page):
        self._page = page
        self._title = page.locator('h4.page-title')
        self._number_of_adults = page.locator('input#adultsCount')
        self._number_of_children = page.locator('input#childrenCount')
        self._input_start_date = page.locator('input#startDate')
        self._input_end_date = page.locator('input#endDate')
        self._create_button = page.locator('//button[@class="btn btn-primary"]')

    def get_title(self):
        return self._title

    def create_gvv_with_2_adults(self, start_date:str, end_date:str):
        self._number_of_adults.fill('2')
        self._input_start_date.fill(start_date)
        self._input_end_date.fill(end_date)
        self._create_button.click()



