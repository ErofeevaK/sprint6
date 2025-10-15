from locators.questions_section_locators import QuestionsSectionLocators
from locators.order_locators import OrderLocators

class UsersTestData:
    # Текст "Заказ оформлен"
    ORDER_CONFIRMATION_TEXT = 'Заказ оформлен'
    # Первый набор данных
    SET_1 = {
        # Данные пользователя (для первой формы)
        "user": {
            "username": "Иван",
            "usersurname": "Кличко",
            "address": "ул. Ленина, 1",
            "telephone": "+79991112233",
            "station_locator": (OrderLocators.STATION_LIST_4)  # Локатор для станции 1
        },
        # Данные заказа (для второй формы)
        "order": {
            "date": "20.05.2025",
            "period": (OrderLocators.RENTAL_DAYS_4),
            "color": (OrderLocators.SCOOTER_BLACK),
            "comment": "Позвонить за час"
        }

    }

    # Второй набор данных
    SET_2 = {
        "user": {
            "username": "Мария",
            "usersurname": "Иванова",
            "address": "пр. Мира, 10-154",
            "telephone": "+79994445566",
            "station_locator": (OrderLocators.STATION_LIST_10)  # Локатор для станции 2
        },
    "order": {
        "date": "22.05.2025",
        "period": (OrderLocators.RENTAL_DAYS_2),
        "color": (OrderLocators.SCOOTER_GRAY),
        "comment": "Не звонить"
        }
    }


class QuestionsData:
    questions_and_answers = [
            {
                "question_locator": QuestionsSectionLocators.QUESTION_COST_PAYMENT,
                "answer_locator": QuestionsSectionLocators.ANSWER_COST_PAYMENT,
                "expected_answer": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
            },
            {
                "question_locator": QuestionsSectionLocators.QUESTION_MULTIPLE_SCOOTERS,
                "answer_locator": QuestionsSectionLocators.ANSWER_MULTIPLE_SCOOTERS,
                "expected_answer": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
            },
            {
                "question_locator": QuestionsSectionLocators.QUESTION_RENTAL_TIME,
                "answer_locator": QuestionsSectionLocators.ANSWER_RENTAL_TIME,
                "expected_answer": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
            },
            {
                "question_locator": QuestionsSectionLocators.QUESTION_SAME_DAY_RENTAL,
                "answer_locator": QuestionsSectionLocators.ANSWER_SAME_DAY_RENTAL,
                "expected_answer": "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
            },
            {
                "question_locator": QuestionsSectionLocators.QUESTION_EARLY_RETURN,
                "answer_locator": QuestionsSectionLocators.ANSWER_EARLY_RETURN,
                "expected_answer": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
            },
            {
                "question_locator": QuestionsSectionLocators.QUESTION_SCOOTER_CHARGER,
                "answer_locator": QuestionsSectionLocators.ANSWER_SCOOTER_CHARGER,
                "expected_answer": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
            },
            {
                "question_locator": QuestionsSectionLocators.QUESTION_CANCEL_ORDER,
                "answer_locator": QuestionsSectionLocators.ANSWER_CANCEL_ORDER,
                "expected_answer": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
            },
            {
                "question_locator": QuestionsSectionLocators.QUESTION_MKAD_DELIVERY,
                "answer_locator": QuestionsSectionLocators.ANSWER_MKAD_DELIVERY,
                "expected_answer": "Да, обязательно. Всем самокатов! И Москве, и Московской области."
            }
        ]