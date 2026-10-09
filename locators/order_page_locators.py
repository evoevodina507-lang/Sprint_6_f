from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Первая форма
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']"
    )
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']"
    )
    NEXT_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Button') and normalize-space()='Далее']"
    )

    # Метро — динамический локатор
    METRO_OPTION = (
        By.XPATH,
        "//button[contains(@class, 'select-search__option') "
        "and contains(., '{metro}')]"
    )

    # Вторая форма
    DATE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']"
    )
    DATEPICKER = (By.CSS_SELECTOR, ".react-datepicker")
    DATEPICKER_CURRENT_MONTH = (
        By.CSS_SELECTOR,
        ".react-datepicker__current-month"
    )
    DATEPICKER_NEXT_MONTH = (
        By.CSS_SELECTOR,
        ".react-datepicker__navigation--next"
    )

    # День в календаре — динамический локатор
    DATEPICKER_DAY = (
        By.XPATH,
        "//div[contains(@class, 'react-datepicker__day') "
        "and normalize-space()='{day}' "
        "and not(contains(@class, 'react-datepicker__day--outside-month'))]"
    )

    RENTAL_PLACEHOLDER = (By.CSS_SELECTOR, ".Dropdown-placeholder")
    RENTAL_OPTIONS = (By.CSS_SELECTOR, ".Dropdown-option")

    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")

    COMMENT_INPUT = (
        By.XPATH,
        "//input[@placeholder='Комментарий для курьера']"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Button') and normalize-space()='Заказать']"
    )

    CONFIRM_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Order_Modal')]"
    )

    CONFIRM_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Modal')]//button[normalize-space()='Да']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader')]"
    )