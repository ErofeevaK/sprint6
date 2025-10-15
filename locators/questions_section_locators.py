from selenium.webdriver.common.by import By

class QuestionsSectionLocators:
    # Локатор раздела "Вопросы о важном"
    HOME_PAGE_QUESTIONS = (By.XPATH, "//div[contains(@class, 'Home_SubHeader') and text()='Вопросы о важном']")

    # Вопрос: "Сколько это стоит? И как оплатить?"
    QUESTION_COST_PAYMENT = (By.ID, "accordion__heading-0")
    # Ответ: "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    ANSWER_COST_PAYMENT = (By.ID, "accordion__panel-0")

    # Вопрос: "Хочу сразу несколько самокатов! Так можно?"
    QUESTION_MULTIPLE_SCOOTERS = (By.ID, "accordion__heading-1")
    # Ответ: "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    ANSWER_MULTIPLE_SCOOTERS = (By.ID, "accordion__panel-1")

    # Вопрос: "Как рассчитывается время аренды?"
    QUESTION_RENTAL_TIME = (By.ID, "accordion__heading-2")
    # Ответ: "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня.
    # Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру.
    # Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    ANSWER_RENTAL_TIME = (By.ID, "accordion__panel-2")

    # Вопрос: "Можно ли заказать самокат прямо на сегодня?"
    QUESTION_SAME_DAY_RENTAL = (By.ID, "accordion__heading-3")
    # Ответ: "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    ANSWER_SAME_DAY_RENTAL = (By.ID, "accordion__panel-3")

    # Вопрос: "Можно ли продлить заказ или вернуть самокат раньше?"
    QUESTION_EARLY_RETURN = (By.ID, "accordion__heading-4")
    # Ответ: "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    ANSWER_EARLY_RETURN = (By.ID, "accordion__panel-4")

    # Вопрос: "Вы привозите зарядку вместе с самокатом?"
    QUESTION_SCOOTER_CHARGER = (By.ID, "accordion__heading-5")
    # Ответ: "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    ANSWER_SCOOTER_CHARGER = (By.ID, "accordion__panel-5")

    # Вопрос: "Можно ли отменить заказ?"
    QUESTION_CANCEL_ORDER = (By.ID, "accordion__heading-6")
    # Ответ: "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    ANSWER_CANCEL_ORDER = (By.ID, "accordion__panel-6")

    # Вопрос: "Я жизу за МКАДом, привезёте?"
    QUESTION_MKAD_DELIVERY = (By.ID, "accordion__heading-7")
    # Ответ: "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    ANSWER_MKAD_DELIVERY = (By.ID, "accordion__panel-7")