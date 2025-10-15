from selenium.webdriver.common.by import By

class HomeLocators:
    # Локатор логотипа Яндекс
    LOGO_YA = (By.XPATH, "//a[@href='//yandex.ru' and @ class ='Header_LogoYandex__3TSOI']")

    # Локатор логотипа Самокат
    LOGO_SCOOTER = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']/img[@alt='Scooter']")