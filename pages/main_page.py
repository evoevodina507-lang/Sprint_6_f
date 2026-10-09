from data import Urls
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def open(self):
        self.open_url(Urls.MAIN_PAGE_URL)

    def accept_cookies(self):
        try:
            self.click(MainPageLocators.COOKIE_ACCEPT_BUTTON)
        except Exception:
            pass

    def click_order_button(self, position):
        if position == "top":
            locator = MainPageLocators.TOP_ORDER_BUTTON
        else:
            locator = MainPageLocators.BOTTOM_ORDER_BUTTON

        self.click(locator)

    def click_faq_question(self, index):
        # На всякий случай повторно принимаем куки,
        # чтобы баннер не перекрывал вопрос
        self.accept_cookies()

        questions = self.find_elements(MainPageLocators.FAQ_QUESTIONS)
        question = questions[index]

        # Прокручиваем к вопросу
        self.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            question
        )

        # Ждём, что вопрос виден и активен
        self.wait_for_condition(
            lambda driver: question.is_displayed() and question.is_enabled()
        )

        # Пробуем кликнуть; если перехвачено — кликаем через JS
        try:
            question.click()
        except Exception:
            self.execute_script("arguments[0].click();", question)

    def get_faq_answer(self, index):
        answers = self.find_elements(MainPageLocators.FAQ_ANSWERS)
        answer = answers[index]

        self.wait_for_condition(
            lambda driver: answer.is_displayed() and answer.text.strip() != ""
        )

        return answer.text.strip()

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    def switch_to_next_window(self):
        current_window = self.get_current_window_handle()
        self.wait_for_new_window()

        for window in self.get_window_handles():
            if window != current_window:
                self.switch_to_window(window)
                return

        raise AssertionError("Новое окно не найдено")