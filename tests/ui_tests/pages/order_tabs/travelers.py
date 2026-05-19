from playwright.sync_api import Page
from tests.ui_tests.pages.devg_page import DevgPage
import json
from pathlib import Path
from typing import List
from pydantic import BaseModel, Field


def load_travelers():

    json_path = Path(__file__).resolve().parent.parent.parent / "test_data" / "travelers.json"

    with open(json_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    # створюємо Pydantic-об’єкт
    data = TravelersData(**raw_data)
    return data.travelers

class Traveler(BaseModel):
    prefix: str
    first_name: str
    last_name: str
    date_of_birth: str = Field(..., description="Format: DD MMM YYYY")
    gender: str

class TravelersData(BaseModel):
    travelers: List[Traveler]

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

        # THIRD TRAVELER
        self._radio_03 = page.locator('//tbody/tr[3]/td[1]//input[@type="radio"]')
        self._prefix_03 = page.locator('//tbody/tr[3]/td[2]//select[contains(@class,"traveler__select--prefix")]')
        self._first_name_03 = page.locator('//tbody/tr[3]/td[3]//input[@class="form-control traveler__name-input"]')
        self._middle_name_03 = page.locator('//tbody/tr[3]/td[4]//input[@class="form-control traveler__name-input"]')
        self._last_name_03 = page.locator(
            '//tbody/tr[3]/td[5]//input[@class="form-control traveler__name-input" and @value="Adult three"]')
        self._date_of_birth_03 = page.locator('//tbody/tr[3]/td[7]//input[@placeholder="DD M YYYY"]')
        self._gender_03 = page.locator('//tbody/tr[3]/td[9]//select[contains(@class,"traveler__select--gender")]')

        # FOURTH TRAVELER
        self._radio_04 = page.locator('//tbody/tr[4]/td[1]//input[@type="radio"]')
        self._prefix_04 = page.locator('//tbody/tr[4]/td[2]//select[contains(@class,"traveler__select--prefix")]')
        self._first_name_04 = page.locator('//tbody/tr[4]/td[3]//input[@class="form-control traveler__name-input"]')
        self._middle_name_04 = page.locator('//tbody/tr[4]/td[4]//input[@class="form-control traveler__name-input"]')
        self._last_name_04 = page.locator(
            '//tbody/tr[4]/td[5]//input[@class="form-control traveler__name-input" and @value="Adult four"]')
        self._date_of_birth_04 = page.locator('//tbody/tr[4]/td[7]//input[@placeholder="DD M YYYY"]')
        self._gender_04 = page.locator('//tbody/tr[4]/td[9]//select[contains(@class,"traveler__select--gender")]')


        #FIRST CHILD
        self._radio_05 = page.locator('//tbody/tr[3]/td[1]//input[@type="radio"]')
        self._prefix_05 = page.locator('//tbody/tr[3]/td[2]//select[contains(@class,"traveler__select--prefix")]')
        self._first_name_05 = page.locator('//tbody/tr[3]/td[3]//input[@class="form-control traveler__name-input"]')
        self._middle_name_05 = page.locator('//tbody/tr[3]/td[4]//input[@class="form-control traveler__name-input"]')
        self._last_name_05 = page.locator(
            '//tbody/tr[3]/td[5]//input[@class="form-control traveler__name-input" and @value="Child three"]')
        self._date_of_birth_05 = page.locator('//tbody/tr[3]/td[7]//input[@placeholder="DD M YYYY"]')
        self._gender_05 = page.locator('//tbody/tr[3]/td[9]//select[contains(@class,"traveler__select--gender")]')

        # SECOND CHILD
        self._radio_06 = page.locator('//tbody/tr[4]/td[1]//input[@type="radio"]')
        self._prefix_06 = page.locator('//tbody/tr[4]/td[2]//select[contains(@class,"traveler__select--prefix")]')
        self._first_name_06 = page.locator('//tbody/tr[4]/td[3]//input[@class="form-control traveler__name-input"]')
        self._middle_name_06 = page.locator('//tbody/tr[4]/td[4]//input[@class="form-control traveler__name-input"]')
        self._last_name_06 = page.locator(
            '//tbody/tr[4]/td[5]//input[@class="form-control traveler__name-input" and @value="Child four"]')
        self._date_of_birth_06 = page.locator('//tbody/tr[4]/td[7]//input[@placeholder="DD M YYYY"]')
        self._gender_06 = page.locator('//tbody/tr[4]/td[9]//select[contains(@class,"traveler__select--gender")]')





    def get_counter_value(self):
        return self._counter.inner_text()

    def save_travelers(self):
        self._save_travelers.click()

    def set_2_adults(self):

        travelers = load_travelers()

        first_traveler = travelers[0]
        self._prefix_01.select_option(first_traveler.prefix)
        self._first_name_01.fill(first_traveler.first_name)
        self._last_name_01.fill(first_traveler.last_name)
        self._date_of_birth_01.click()
        self._date_of_birth_01.clear()
        self._date_of_birth_01.type(first_traveler.date_of_birth)
        self._date_of_birth_02.press('Enter')
        self._gender_01.select_option(first_traveler.gender)


        second_traveler = travelers[1]
        self._prefix_02.select_option(second_traveler.prefix)
        self._first_name_02.fill(second_traveler.first_name)
        self._last_name_02.fill(second_traveler.last_name)
        self._date_of_birth_02.click()
        self._date_of_birth_02.clear()
        self._date_of_birth_02.type(second_traveler.date_of_birth)
        self._date_of_birth_02.press('Enter')
        self._gender_02.select_option(second_traveler.gender)

        self._page.get_by_role("button", name="Save Travelers").click()

    def set_4_adults(self):

        travelers = load_travelers()

        first_traveler = travelers[0]
        self._prefix_01.select_option(first_traveler.prefix)
        self._first_name_01.fill(first_traveler.first_name)
        self._last_name_01.fill(first_traveler.last_name)
        self._date_of_birth_01.click()
        self._date_of_birth_01.clear()
        self._date_of_birth_01.type(first_traveler.date_of_birth)
        self._date_of_birth_02.press('Enter')
        self._gender_01.select_option(first_traveler.gender)


        second_traveler = travelers[1]
        self._prefix_02.select_option(second_traveler.prefix)
        self._first_name_02.fill(second_traveler.first_name)
        self._last_name_02.fill(second_traveler.last_name)
        self._date_of_birth_02.click()
        self._date_of_birth_02.clear()
        self._date_of_birth_02.type(second_traveler.date_of_birth)
        self._date_of_birth_02.press('Enter')
        self._gender_02.select_option(second_traveler.gender)

        third_traveler = travelers[2]
        self._prefix_03.select_option(third_traveler.prefix)
        self._first_name_03.fill(third_traveler.first_name)
        self._last_name_03.fill(third_traveler.last_name)
        self._date_of_birth_03.click()
        self._date_of_birth_03.clear()
        self._date_of_birth_03.type(third_traveler.date_of_birth)
        self._date_of_birth_03.press('Enter')
        self._gender_03.select_option(third_traveler.gender)

        fourth_traveler = travelers[3]
        self._prefix_04.select_option(fourth_traveler.prefix)
        self._first_name_04.fill(fourth_traveler.first_name)
        self._last_name_04.fill(fourth_traveler.last_name)
        self._date_of_birth_04.click()
        self._date_of_birth_04.clear()
        self._date_of_birth_04.type(fourth_traveler.date_of_birth)
        self._date_of_birth_04.press('Enter')
        self._gender_04.select_option(fourth_traveler.gender)

        self._page.get_by_role("button", name="Save Travelers").click()

    def set_2_adults_2_children(self):

        travelers = load_travelers()

        first_traveler = travelers[0]
        self._prefix_01.select_option(first_traveler.prefix)
        self._first_name_01.fill(first_traveler.first_name)
        self._last_name_01.fill(first_traveler.last_name)
        self._date_of_birth_01.click()
        self._date_of_birth_01.clear()
        self._date_of_birth_01.type(first_traveler.date_of_birth)
        self._date_of_birth_02.press('Enter')
        self._gender_01.select_option(first_traveler.gender)


        second_traveler = travelers[1]
        self._prefix_02.select_option(second_traveler.prefix)
        self._first_name_02.fill(second_traveler.first_name)
        self._last_name_02.fill(second_traveler.last_name)
        self._date_of_birth_02.click()
        self._date_of_birth_02.clear()
        self._date_of_birth_02.type(second_traveler.date_of_birth)
        self._date_of_birth_02.press('Enter')
        self._gender_02.select_option(second_traveler.gender)

        third_traveler = travelers[4]
        self._prefix_05.select_option(third_traveler.prefix)
        self._first_name_05.fill(third_traveler.first_name)
        self._last_name_05.fill(third_traveler.last_name)
        self._date_of_birth_05.click()
        self._date_of_birth_05.clear()
        self._date_of_birth_05.type(third_traveler.date_of_birth)
        self._date_of_birth_05.press('Enter')
        self._gender_05.select_option(third_traveler.gender)

        fourth_traveler = travelers[5]
        self._prefix_06.select_option(fourth_traveler.prefix)
        self._first_name_06.fill(fourth_traveler.first_name)
        self._last_name_06.fill(fourth_traveler.last_name)
        self._date_of_birth_06.click()
        self._date_of_birth_06.clear()
        self._date_of_birth_06.type(fourth_traveler.date_of_birth)
        self._date_of_birth_06.press('Enter')
        self._gender_06.select_option(fourth_traveler.gender)

        self._page.get_by_role("button", name="Save Travelers").click()





