import re

from playwright.sync_api import Page, expect, Dialog
from tests.ui_tests.pages.devg_page import DevgPage


class ItineraryTab(DevgPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._button_add_service = page.get_by_role("button", name="Add Service")
        self._modal_add_service = page.locator("div.modal-content").nth(1)
        self._modal_add_service_title = page.locator('div.m-0.modal-title.h4')
        self._delete_service_notification = page.locator('//div[contains(@class,"Toastify__toast-body")]')

    def is_button_add_service_present(self):
        expect(self._button_add_service).to_be_visible()
        return True

    def button_add_service_click(self):
        self._button_add_service.click()

    def is_modal_add_service_title_present(self):
        expect(self._modal_add_service_title).to_have_text("Add Service")
        return True

    def get_modal_add_service(self):
        return self._modal_add_service

    def get_delete_service_notification(self):
        return self._delete_service_notification

    def quote_an_accommodation_service(self):
        self._page.locator(
            ".form-row > div:nth-child(2) > .form-field__editor > .css-b62m3t-container > .react-select__control > .react-select__value-container").click()
        self._page.locator("#react-select-5-input").fill("dub")
        self._page.get_by_role("option", name="Ireland / Dublin").click()

        self._page.get_by_role("textbox", name="YYYY-MM-DD").first.click()
        self._page.get_by_role("textbox", name="YYYY-MM-DD").first.clear()
        self._page.get_by_role("textbox", name="YYYY-MM-DD").first.type('2026-07-20')
        self._page.get_by_role("textbox", name="YYYY-MM-DD").first.press('Enter')

        self._page.get_by_role("textbox", name="YYYY-MM-DD").nth(1).click()
        self._page.get_by_role("textbox", name="YYYY-MM-DD").nth(1).clear()
        self._page.get_by_role("textbox", name="YYYY-MM-DD").nth(1).type('2026-07-25')
        self._page.get_by_role("textbox", name="YYYY-MM-DD").nth(1).press('Enter')
        self._page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
        self._page.get_by_text("The Alex Hotel").click()
        sell_value_in_modal = self._page.locator("//tr[@class='table-row__hover']/td[5]").inner_text()
        self._page.on("dialog", lambda dialog: dialog.accept())
        self._page.locator("button.btn-warning.btn-block").click()
        self._page.get_by_role("button", name="Close").click()
        return sell_value_in_modal

    def get_quoted_accommodation_sell(self):
        return self._page.locator("div.text-quoted-price").first.inner_text()

    def delete_quoted_accommodation_service(self):
        self._page.get_by_role("button", name="Show").click()

        self._page.on("dialog", lambda dialog: dialog.accept())
        self._page.get_by_role("button", name="Delete Service").click()

        self._page.wait_for_timeout(1000)


