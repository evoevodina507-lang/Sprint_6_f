from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-cookie")

    TOP_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']"
    )

    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']"
    )

    FAQ_QUESTIONS = (
        By.XPATH,
        "//div[contains(@class, 'accordion__heading')]"
    )

    FAQ_ANSWERS = (
        By.XPATH,
        "//div[contains(@class, 'accordion__panel')]"
    )

    YANDEX_LOGO = (
        By.XPATH,
        "//a[contains(@class, 'Header_LogoYandex')]"
    )

    SCOOTER_LOGO = (
        By.XPATH,
        "//a[contains(@class, 'Header_LogoScooter')]"
    )