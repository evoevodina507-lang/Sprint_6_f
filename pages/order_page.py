from datetime import datetime

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def fill_first_form(self, name, surname, address, metro, phone):
        self.input_text(OrderPageLocators.NAME_INPUT, name)
        self.input_text(OrderPageLocators.SURNAME_INPUT, surname)
        self.input_text(OrderPageLocators.ADDRESS_INPUT, address)

        self.click(OrderPageLocators.METRO_INPUT)

        metro_locator = (
            OrderPageLocators.METRO_OPTION[0],
            OrderPageLocators.METRO_OPTION[1].format(metro=metro)
        )
        self.click(metro_locator)

        self.input_text(OrderPageLocators.PHONE_INPUT, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    def select_date(self, date):
        target_date = datetime.strptime(date, "%d.%m.%Y")
        target_day = str(target_date.day)

        self.click(OrderPageLocators.DATE_INPUT)
        self.wait_for_visibility(OrderPageLocators.DATEPICKER)

        month_names = {
            1: "январ", 2: "феврал", 3: "март", 4: "апрел",
            5: "май", 6: "июн", 7: "июл", 8: "август",
            9: "сентябр", 10: "октябр", 11: "ноябр", 12: "декабр"
        }

        for _ in range(24):
            current_month = self.find_element(
                OrderPageLocators.DATEPICKER_CURRENT_MONTH
            ).text.strip()

            target_month_name = month_names[target_date.month]

            if (
                target_month_name in current_month.lower()
                and str(target_date.year) in current_month
            ):
                break

            self.click(OrderPageLocators.DATEPICKER_NEXT_MONTH)

        day_locator = (
            OrderPageLocators.DATEPICKER_DAY[0],
            OrderPageLocators.DATEPICKER_DAY[1].format(day=target_day)
        )
        self.click(day_locator)

        self.wait_for_invisibility(OrderPageLocators.DATEPICKER)

    def select_rental_period(self, rental_period):
        self.click(OrderPageLocators.RENTAL_PLACEHOLDER)

        self.wait_for_condition(
            lambda driver: any(
                option.is_displayed()
                for option in self.find_elements(OrderPageLocators.RENTAL_OPTIONS)
            )
        )

        options = self.find_elements(OrderPageLocators.RENTAL_OPTIONS)

        for option in options:
            if option.is_displayed() and option.text.strip() == rental_period:
                option.click()
                return

        available = [
            option.text.strip()
            for option in options
            if option.is_displayed()
        ]
        raise AssertionError(
            f"Не найден срок аренды '{rental_period}'. "
            f"Доступные варианты: {available}"
        )

    def select_scooter_color(self, color):
        if color == "black":
            color_locator = OrderPageLocators.COLOR_BLACK
        elif color == "grey":
            color_locator = OrderPageLocators.COLOR_GREY
        else:
            raise ValueError(f"Неизвестный цвет самоката: {color}")

        color_checkbox = self.wait_for_presence(color_locator)

        self.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            color_checkbox
        )

        if not color_checkbox.is_selected():
            self.execute_script("arguments[0].click();", color_checkbox)

        self.wait_for_condition(
            lambda driver: color_checkbox.is_selected()
        )

    def click_order_button(self):
        buttons = self.find_elements(OrderPageLocators.ORDER_BUTTON)
        visible_buttons = [
            b for b in buttons if b.is_displayed() and b.is_enabled()
        ]

        if not visible_buttons:
            raise AssertionError(
                "Не найдена доступная кнопка 'Заказать' на второй форме"
            )

        self.click_element(visible_buttons[-1])

    def fill_second_form(self, date, rental_period, color, comment):
        self.select_date(date)
        self.select_rental_period(rental_period)
        self.select_scooter_color(color)
        self.input_text(OrderPageLocators.COMMENT_INPUT, comment)
        self.click_order_button()
        self.wait_for_visibility(OrderPageLocators.CONFIRM_MODAL)

    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    def is_success_message_displayed(self):
        return self.wait_for_visibility(
            OrderPageLocators.SUCCESS_MESSAGE
        ).is_displayed()