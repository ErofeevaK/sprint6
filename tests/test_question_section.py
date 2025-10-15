import allure
import pytest
from pages.faq_page import QuestionsSectionPage
from locators.questions_section_locators import QuestionsSectionLocators
from data import QuestionsData

class TestQuestionsSection:
    @allure.title("Тест соответствия текста ответа на вопрос")
    @pytest.mark.parametrize('test_case', QuestionsData.questions_and_answers)
    def test_faq_dropdown(self, driver, test_case):
        faq_page = QuestionsSectionPage(driver) # Инициализация страницы
        faq_page.accept_cookies()  # Принятие куков
        faq_page.scroll_to_element(QuestionsSectionLocators.QUESTION_COST_PAYMENT) # Скроллим до нужного элемента с вопросом
        faq_page.wait_for_element_visible(test_case["question_locator"]) # Подождать видимости элемента
        faq_page.click_question(test_case["question_locator"]) # Кликаем по вопросу
        faq_page.wait_for_element_visible(test_case["answer_locator"]) # Ждем появления ответа
        actual_text = faq_page.get_answer_text(test_case["answer_locator"]) # Получаем фактический и ожидаемый текст ответа
        expected_text = test_case["expected_answer"]
        assert actual_text == expected_text # Проверяем соответствие текста