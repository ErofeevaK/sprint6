import allure
import pytest
from locators.order_locators import OrderLocators
from pages.order_page import OrderPage
from data import UsersTestData

class TestOrderForm:
    @allure.title("Тест формы заказа самоката")
    @pytest.mark.parametrize("start_button,test_data",
                             [(OrderLocators.ORDER_BUTTON_TOP, UsersTestData.SET_1),
                              (OrderLocators.ORDER_BUTTON_BOTTOM, UsersTestData.SET_2)])
    def test_order_form(self, driver, start_button, test_data):
        order_page = OrderPage(driver) # Инициализация страницы
        order_page.accept_cookies() # Принятие куков
        order_page.click_on_element(start_button)
        order_page.fill_first_order_form(test_data)
        order_page.fill_second_order_form(test_data["order"])
        confirmation_text = order_page.is_order_successful()
        assert UsersTestData.ORDER_CONFIRMATION_TEXT in confirmation_text, f"Ожидался текст '{UsersTestData.ORDER_CONFIRMATION_TEXT}', но получили: {confirmation_text}"