import allure
import pytest
from locators.order_locators import OrderLocators
from pages.home_page import HomePage
from urls import BASE_URL

class TestLogoScooter:
    @allure.title("Тест проверки перехода с лого Самоката на главную страницу сайта")
    def test_logo_scooter(self, driver):
        with allure.step("Открытие страницы заказа"):
            home_page = HomePage(driver)
            home_page.click_on_element(OrderLocators.ORDER_BUTTON_TOP)

        with allure.step("Находим и кликаем на логотип Самоката"):
            home_page.click_logo_scooter()

        with allure.step("Ждем загрузки страницы и проверяем URL"):
            home_page.wait_for_url(BASE_URL)

        with allure.step("Проверяем, что открылась главная страница Самоката"):
            current_url = home_page.get_current_url()
            assert BASE_URL in current_url