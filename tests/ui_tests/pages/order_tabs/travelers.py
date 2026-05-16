from playwright.sync_api import Page
from tests.ui_tests.pages.devg_page import DevgPage
import json
from pathlib import Path


def load_travelers():

    json_path = Path(__file__).resolve().parent.parent.parent / "test_data" / "travelers.json"

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["travelers"]


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
        travelers = load_travelers()
        self._prefix_01.select_option(travelers[0]['prefix'])
        self._first_name_01.fill(travelers[0]['first_name'])
        self._last_name_01.fill(travelers[0]['last_name'])
        self._date_of_birth_01.click()
        self._date_of_birth_01.clear()
        self._date_of_birth_01.type(travelers[0]['date_of_birth'])
        self._date_of_birth_02.press('Enter')
        self._gender_01.select_option(travelers[0]['gender'])

        self._prefix_02.select_option(travelers[1]['prefix'])
        self._first_name_02.fill(travelers[1]['first_name'])
        self._last_name_02.fill(travelers[1]['last_name'])
        self._date_of_birth_02.click()
        self._date_of_birth_02.clear()
        self._date_of_birth_02.type(travelers[1]['date_of_birth'])
        self._date_of_birth_02.press('Enter')
        self._gender_02.select_option(travelers[1]['gender'])


