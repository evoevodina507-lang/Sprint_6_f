import pytest

from data import Urls, OrderData
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @pytest.mark.parametrize(
        "user_data",
        [OrderData.DATA_SET_1, OrderData.DATA_SET_2]
    )
    def test_order_success(self, driver, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.accept_cookies()
        main_page.click_order_button(user_data["order_button"])

        order_page.fill_first_form(
            user_data["name"],
            user_data["surname"],
            user_data["address"],
            user_data["metro"],
            user_data["phone"]
        )

        order_page.fill_second_form(
            user_data["date"],
            user_data["rental_period"],
            user_data["color"],
            user_data["comment"]
        )

        order_page.confirm_order()

        assert order_page.is_success_message_displayed()

    def test_scooter_logo_returns_to_main_page(self, driver):
        main_page = MainPage(driver)

        main_page.open()
        main_page.accept_cookies()
        main_page.click_scooter_logo()

        assert main_page.get_current_url() == Urls.MAIN_PAGE_URL

    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)

        main_page.open()
        main_page.accept_cookies()

        original_window = main_page.get_current_window_handle()

        main_page.click_yandex_logo()
        main_page.switch_to_next_window()

        main_page.wait_for_url_contains("dzen.ru")

        assert main_page.get_current_window_handle() != original_window
        assert "dzen.ru" in main_page.get_current_url()