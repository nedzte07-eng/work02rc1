import os

from playwright.sync_api import expect
from tests.ui_tests.pages.log_in_page import LogInPage

UI_URL = os.getenv('RC1_ORION')
RC1_ORION_EMAIL = os.getenv('RC1_ORION_EMAIL')
RC1_ORION_PASSWORD = os.getenv('RC1_ORION_PASSWORD')
RC1_ORION_BASIC_USER = os.getenv('RC1_ORION_BASIC_USER')
RC1_ORION_BASIC_PASS = os.getenv('RC1_ORION_BASIC_PASS')

def test_login_page(page):
    login = LogInPage(page)

    admin = login.navigate().login(RC1_ORION_EMAIL, RC1_ORION_PASSWORD)

    expect(admin.get_logo()).to_contain_text("Orion")

def test_create_order(page):
    login = LogInPage(page)

    admin_page = login.navigate().login(RC1_ORION_EMAIL, RC1_ORION_PASSWORD)

    expect(admin_page.get_logo()).to_contain_text("Orion")

    order_page = admin_page.order_link_click()

    expect(order_page.get_title()).to_contain_text("Order")

    order_create_page = order_page.create_button_click()
    expect(order_create_page.get_title()).to_contain_text("New Order")

    devg_page = order_create_page.create_gvv_with_2_adults('2026-07-20', '2026-07-25')
    expect(devg_page.get_title()).to_contain_text("DEVG")




