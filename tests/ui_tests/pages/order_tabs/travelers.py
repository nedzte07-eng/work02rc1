from playwright.sync_api import Page
from tests.ui_tests.pages.devg_page import DevgPage


class TravelersTab(DevgPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._counter = page.locator('a.nav-link[href="#travelers"] span.order-edit__counter')
        # FIRST TRAVELER
        self._radio_01 = page.locator('//tbody/tr[1]/td[1]//input[@type="radio"]')
        self._prefix_01 = page.locator('//tbody/tr[1]/td[2]//select[contains(@class,"traveler__select--prefix")]')
        self._first_name_01 = page.locator('//tbody/tr[1]/td[3]//input[@class="form-control traveler__name-input"]')
        self._middle_name_01 = page.locator('//tbody/tr[1]/td[4]//input[@class="form-control traveler__name-input"]')
        self._last_name_01 = page.locator('//tbody/tr[1]/td[5]//input[@class="form-control traveler__name-input" and @value="Adult one"]')
        # //tbody/tr[1]/td[6]//select[contains(@class,"traveler__select--suffix")]
        self._date_of_birth_01 = page.locator('//tbody/tr[1]/td[7]//input[@placeholder="DD M YYYY"]')
        # //tbody/tr[1]/td[8]
        self._gender_01 = page.locator('//tbody/tr[1]/td[9]//select[contains(@class,"traveler__select--gender")]')
        # // tbody / tr[1] / td[10]
        # // tbody / tr[1] / td[11]
        # // tbody / tr[1] / td[12] // button[contains(text(), "Show")]
        # // tbody / tr[1] / td[13] // button[contains(text(), "Assignments")]
        # // tbody / tr[1] / td[14] // button[contains( @class ,"btn-danger")]
        # SECOND TRAVELER
        self._radio_02 = page.locator('//tbody/tr[2]/td[1]//input[@type="radio"]')
        self._prefix_02 = page.locator('//tbody/tr[2]/td[2]//select[contains(@class,"traveler__select--prefix")]')
        self._first_name_02 = page.locator('//tbody/tr[2]/td[3]//input[@class="form-control traveler__name-input"]')
        self._middle_name_02 = page.locator('//tbody/tr[2]/td[4]//input[@class="form-control traveler__name-input"]')
        self._last_name_02 = page.locator('//tbody/tr[2]/td[5]//input[@class="form-control traveler__name-input" and @value="Adult two"]')
        self._date_of_birth_02 = page.locator('//tbody/tr[2]/td[7]//input[@placeholder="DD M YYYY"]')
        self._gender_02 = page.locator('//tbody/tr[2]/td[9]//select[contains(@class,"traveler__select--gender")]')


    def get_counter_value(self):
        return self._counter.inner_text()

    def save_travelers(self):
        self._save_travelers.click()

    def set_2_adults(self):
        self._prefix_01.select_option('Mr')
        self._first_name_01.fill('Tom')
        self._last_name_01.fill('Seaver')
        self._date_of_birth_01.click()
        self._date_of_birth_01.clear()
        self._date_of_birth_01.type('01 Jan 1991')
        self._date_of_birth_02.press('Enter')
        self._gender_01.select_option('M')

        self._prefix_02.select_option('Ms')
        self._first_name_02.fill('Emma')
        self._last_name_02.fill('Jonson')
        self._date_of_birth_02.click()
        self._date_of_birth_02.clear()
        self._date_of_birth_02.type('01 Jan 1992')
        self._date_of_birth_02.press('Enter')
        self._gender_02.select_option('F')
