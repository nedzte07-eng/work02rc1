import os
import pytest
import allure
from playwright.sync_api import expect

from tests.ui_tests.pages.devg_page import TravelersTab
from tests.ui_tests.pages.log_in_page import LogInPage


@allure.feature("Testing of Orion")
class TestOrionRC101:
    UI_URL = os.getenv('RC1_ORION')
    RC1_ORION_EMAIL = os.getenv('RC1_ORION_EMAIL')
    RC1_ORION_PASSWORD = os.getenv('RC1_ORION_PASSWORD')
    RC1_ORION_BASIC_USER = os.getenv('RC1_ORION_BASIC_USER')
    RC1_ORION_BASIC_PASS = os.getenv('RC1_ORION_BASIC_PASS')
    TEST_ORDER_ID = os.getenv('RC1_ORION_TEST_ORDER')

    @pytest.mark.skip(reason="Цей тест тимчасово вимкнено")
    @allure.story("Log in to Orion")
    @allure.title("Checking if user can Log in to Orion via applicable credentials")
    @allure.description("Ensure if user can Log in to Orion via applicable credentials")
    def test_login_page(self, page):
        login = LogInPage(page)

        admin = login.navigate().login(self.RC1_ORION_EMAIL, self.RC1_ORION_PASSWORD)
        with allure.step("Assert that the user is logged in"):
            expect(admin.get_logo()).to_contain_text("Orion")

    @pytest.mark.skip(reason="Цей тест тимчасово вимкнено")
    @allure.story("Creating an order")
    @allure.title("Checking if user can create an order for 2 travelers")
    @allure.description("Ensure if user can create an order for 2 travelers")
    def test_create_order(self, page):
        login = LogInPage(page)

        admin_page = login.navigate().login(self.RC1_ORION_EMAIL, self.RC1_ORION_PASSWORD)
        with allure.step("Creating an order for 2 travelers"):
            with allure.step("Assert that the user is logged in"):
                expect(admin_page.get_logo()).to_contain_text("Orion")

                order_page = admin_page.order_link_click()
            with allure.step("Assert that we on the Order page"):
                expect(order_page.get_title()).to_contain_text("Order")

                order_create_page = order_page.create_button_click()
            with allure.step("Assert that we on the Order Create page"):
                expect(order_create_page.get_title()).to_contain_text("New Order")

                devg_page = order_create_page.create_gvv_with_2_adults('2026-08-01', '2026-08-05')
            with allure.step("Assert that we created DEVG order"):
                expect(devg_page.get_title()).to_contain_text("DEVG")

                travelers_tab = TravelersTab(page)
                travelers_tab.click_travelers()
            with allure.step("Assert that we on Travellers tab"):
                expect(travelers_tab.get_save_travelers()).to_contain_text("Travelers")
                screenshot = travelers_tab.get_save_travelers().screenshot()
                allure.attach(
                    screenshot,
                    name="Save Travelers button",
                    attachment_type=allure.attachment_type.PNG
                )
            with allure.step("Assert that travellers counter is 2"):
                assert travelers_tab.get_counter_value() == "2"


    @allure.story("Opening the test order for 2 travelers")
    @allure.title("Checking if user can open the test order for 2 travelers")
    @allure.description("Ensure if user can open the test order for 2 travelers")
    def test_order_open_and_change(self, page):
        login = LogInPage(page)

        admin_page = login.navigate().login(self.RC1_ORION_EMAIL, self.RC1_ORION_PASSWORD)

        with allure.step("Opening the test order for 2 travelers"):
            with allure.step("Working with the test Order"):
                expect(admin_page.get_logo()).to_contain_text("Orion")

                test_order = admin_page.open_order_by_id(self.TEST_ORDER_ID)
            with allure.step("Check if we on the test order"):
                expect(test_order.get_title()).to_contain_text(f"{self.TEST_ORDER_ID}")

                travelers_tab = TravelersTab(page)
                travelers_tab.click_travelers()
            with allure.step("Assert that we on Travellers tab"):
                expect(travelers_tab.get_save_travelers()).to_contain_text("Travelers")
                screenshot = travelers_tab.get_save_travelers().screenshot()
                allure.attach(
                    screenshot,
                    name="Save Travelers button",
                    attachment_type=allure.attachment_type.PNG
                )
            with allure.step("Assert that travellers counter is 2"):
                assert travelers_tab.get_counter_value() == "2"
















