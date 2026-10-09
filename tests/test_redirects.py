from pages.main_page import MainPage
from data import Urls


class TestRedirects:

    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.MAIN_PAGE_URL)
        main_page.accept_cookies()

        main_page.click_yandex_logo()
        main_page.switch_to_next_window()

        main_page.wait_for_url_contains("dzen.ru")

        assert "dzen.ru" in main_page.get_current_url()