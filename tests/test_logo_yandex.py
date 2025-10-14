import allure
import time
from locators.order_locators import OrderLocators
from pages.home_page import HomePage
from urls import DZEN_URL


class TestLogoYandex:
    @allure.title("Тест проверки перехода с лого Яндекса на главную страницу Дзена в новом окне через редирект")
    def test_yandex_logo_redirect(self, driver):
        with allure.step("Открытие страницы заказа"):
            home_page = HomePage(driver)
            home_page.click_on_element(OrderLocators.ORDER_BUTTON_TOP)
            time.sleep(2)  # Добавил небольшую паузу для стабильности

        with allure.step("Запоминаем текущее окно"):
            main_window = home_page.get_current_window_handle()

        with allure.step("Находим и кликаем на логотип Яндекса"):
            home_page.click_logo_yandex()

        with allure.step("Ждем открытия нового окна"):
            home_page.wait_for_new_window_opened(timeout=10)  # Уменьшил таймаут

        with allure.step("Переключаемся на новое окно"):
            home_page.switch_to_new_window(main_window)

        with allure.step("Ждем загрузки страницы и проверяем URL"):
            home_page.wait_for_url_contains(DZEN_URL, timeout=10)  # Уменьшил таймаут

        with allure.step("Проверяем, что открылась страница Дзена"):
            current_url = home_page.get_current_url()
            assert DZEN_URL in current_url, f"Ожидался URL содержащий {DZEN_URL}, но получен {current_url}"

        with allure.step("Закрываем новое окно и возвращаемся к основному"):
            home_page.driver.close()  # Простое закрытие окна
            home_page.driver.switch_to.window(main_window)