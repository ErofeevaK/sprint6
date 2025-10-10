import allure
from pages.base_page import BasePage
from locators.order_locators import OrderLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrderPage(BasePage):
    @allure.step("Нажать на кнопку Заказать вверху страницы")
    def click_order_button_top(self):
        self.click_on_element(OrderLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать на кнопку Заказать внизу страницы")
    def click_order_button(self):
        self.click_on_element(OrderLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Заполнить первую форму заказа")
    def fill_first_order_form(self, test_data):
        user_info = test_data["user"]
        # Ввод Имени
        self.input_text(OrderLocators.NAME, user_info["username"])
        # Ввод Фамилии
        self.input_text(OrderLocators.SURNAME, user_info["usersurname"])
        # Ввод адреса
        self.input_text(OrderLocators.ADDRESS, user_info["address"])
        # Выбор станции метро
        self.click_on_element(OrderLocators.METRO_STATION)
        station = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(user_info["station_locator"]))
        station.click()
        # Ввод номера телефона
        self.input_text(OrderLocators.TELEPHONE, user_info["telephone"])
        # Нажать кнопку Далее
        self.click_on_element(OrderLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую форму заказа")
    def fill_second_order_form(self, order_data):
        # Выбор даты
        calendar_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderLocators.WHEN_BRING_SCOOTER))
        self.click_on_element(OrderLocators.WHEN_BRING_SCOOTER)
        calendar_input.send_keys(order_data["date"])
        calendar_input.send_keys(Keys.ESCAPE)

        # Выбор срока аренды
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderLocators.RENTAL_PERIOD)).click()
        self.click_on_element(order_data["period"])

        # Выбор цвета
        self.click_on_element(order_data["color"])

        # Комментарий
        self.input_text(OrderLocators.COMMENT, order_data["comment"])

        # Подтверждение заказа
        self.click_on_element(OrderLocators.ORDER_BUTTON)
        self.click_on_element(OrderLocators.YES_BUTTON)

    @allure.step("Ожидание видимости модального окна и получение текста окна Заказ оформлен")
    def is_order_successful(self):
        modal = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderLocators.CONFIRM_MODAL))
        element_text = modal.find_element(*OrderLocators.ORDER_PLACED).text
        return element_text