from selenium.webdriver.common.by import By

class OrderLocators:
    #Кнопка "Заказать" вверху страницы
    ORDER_BUTTON_TOP = (By.XPATH,"//button[@class='Button_Button__ra12g' and text()='Заказать']")

    # Кнопка "Заказать" внизу страницы
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']")

    # Локаторы для первой части формы (Для кого самокат):

    NAME = (By.XPATH,"//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH,"//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH,"//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH,"//input[@placeholder='* Станция метро']")
    # Элементы списка (станции)
    STATION_LIST_4 = (By.XPATH, "//li[@class='select-search__row' and @data-index='4']")
    STATION_LIST_10 = (By.XPATH, "//li[@class='select-search__row' and @data-index='10']")
    TELEPHONE = (By.XPATH,"//input[@ placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH,"//button[text()='Далее']")

    # Локаторы для второй части формы (Про аренду):

    # поле ввода даты:
    WHEN_BRING_SCOOTER = (By.XPATH,"//input[@placeholder='* Когда привезти самокат']")
    # выпадающий календарь (появляется после клика)
    CALENDAR = (By.XPATH,"//div[contains(@class, 'react-datepicker')]")
    # выбор даты в календаре (число {day_to_select} (подставить нужное) текущего месяца)
    day_to_select = 20
    DATE_CURRENT_MONTH = (By.XPATH,f"//div[contains(@class, 'react-datepicker__day') and text()='{day_to_select}']")
    # кнопка переключения месяца вперед
    NEXT_MONTH = (By.XPATH, "//button[contains(@class,'react-datepicker__navigation--next')]")

    # поле "Срок аренды"
    RENTAL_PERIOD = (By.XPATH, "//div[contains(text(),'* Срок аренды')]")
    # выпадающий список "Срока аренды" - четверо суток
    RENTAL_DAYS_4 = (By.XPATH, "//div[@class='Dropdown-option' and text()='четверо суток']")
    RENTAL_DAYS_2 = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")

    # цвет самоката
    SCOOTER_COLOR = (By.XPATH, "//div[@class ='Dropdown-option']")
    # цвет самоката чекбоксы
    SCOOTER_BLACK = (By.XPATH, "//input[@id='black']")
    SCOOTER_GRAY = (By.XPATH, "//input[@id='grey']")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    BACK_BUTTON =("//button[text()='Назад']")

    # Локаторы для подтверждения заказа (модальное окно после нажатия кнопки "Заказать"):

    PLACE_ORDER = (By.XPATH, "//div[contains(text(),'Хотите оформить заказ?')]")
    YES_BUTTON = (By.XPATH, "//button[text() ='Да']")
    NO_BUTTON = (By.XPATH, "//button[text()='Нет']")

    # Локатор подтверждения заказа (модальное окно после нажатия "Да"):
    CONFIRM_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    ORDER_PLACED = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Заказ оформлен')]")
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")