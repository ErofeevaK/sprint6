import allure
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QuestionsSectionPage(BasePage):

    @allure.step("Кликает по вопросу")
    def click_question(self, question_locator):
        question = self.driver.find_element(*question_locator)
        question.click()

    @allure.step("Получает текст ответа")
    def get_answer_text(self, answer_locator):
        answer = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(answer_locator))
        return answer.text