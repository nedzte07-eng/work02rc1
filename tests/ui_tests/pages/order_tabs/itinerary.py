from playwright.sync_api import Page, expect
from tests.ui_tests.pages.devg_page import DevgPage

class ItineraryTab(DevgPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._button_add_service = page.get_by_role("button", name="Add Service")
        self._modal_add_service = page.locator("div.modal-content").nth(1)
        self._modal_add_service_title = page.locator('div.m-0.modal-title.h4')


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

    def quote_a_service(self):
        self._modal_add_service_title.click()

