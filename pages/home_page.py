import allure
from pages.base_page import BasePage
from locators.home_locators import HomeLocators


class HomePage(BasePage):
    @allure.step("Нажать на лого Яндекс")
    def click_logo_yandex(self):
        self.click_on_element(HomeLocators.LOGO_YA)

    @allure.step("Нажать на лого Самокат")
    def click_logo_scooter(self):
        self.click_on_element(HomeLocators.LOGO_SCOOTER)