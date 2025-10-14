import allure
from pages.base_page import BasePage

class QuestionsSectionPage(BasePage):

    @allure.step("Кликает по вопросу")
    def click_question(self, question_locator):
        # Используем метод из BasePage вместо self.driver.find_element
        self.click_on_element(question_locator)

    @allure.step("Получает текст ответа")
    def get_answer_text(self, answer_locator):
        # Используем метод из BasePage вместо прямого WebDriverWait
        answer = self.wait_for_element_visible(answer_locator)
        return answer.text