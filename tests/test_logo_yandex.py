import allure
import pytest
from locators.order_locators import OrderLocators
from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import DZEN_URL


class TestLogoYandex:
    @allure.title("Тест проверки перехода с лого Яндекса на главную странице Дзена в новом окне через редирект")
    def test_yandex_logo_redirect(self, driver):
        with allure.step("Открытие страницы заказа"):
            home_page = HomePage(driver)
            home_page.click_on_element(OrderLocators.ORDER_BUTTON_TOP)

        with allure.step("Запоминаем текущее окно"):
            main_window = home_page.get_current_window_handle()

        with allure.step("Находим и кликаем на логотип Яндекса"):
            home_page.click_logo_yandex()

        with allure.step("Ждем открытия нового окна"):
            home_page.wait_for_new_window_opened()

        with allure.step("Переключаемся на новое окно"):
            home_page.switch_to_new_window(main_window)

        with allure.step("Ждем загрузки страницы и проверяем URL"):
            home_page.wait_for_url(DZEN_URL)

        with allure.step("Проверяем, что открылась страница Дзена"):
            current_url = home_page.get_current_url()
            assert DZEN_URL in current_url