from selenium.webdriver.common.by import By

class NewsPage:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://www.sport-express.ru/news/')

    def logo_news(self):
        logo_news = self.browser.find_element(By.XPATH, '//div[@class="se-logo"]')

    def h1_news(self):
        h1_news = self.browser.find_element(By.XPATH, '//h1[contains(text(),"Весь спорт.")]')

    def button_glvn(self, count):
        button_glvn = self.browser.find_elements(By.XPATH, '//div[@class="se-material-list-filter__button-holder"]')
        assert len(button_glvn) == count

    def button_glvn_click(self):
        button_glvn_click = self.browser.find_element(By.XPATH, '//a[contains(text(),"Главные")]')
        button_glvn_click.click()
        assert 'https://www.sport-express.ru/news/?isEditorialChoice=1' == 'https://www.sport-express.ru/news/?isEditorialChoice=1', "Неверный урл Главные кнпк"

    def button_readers(self):
        button_readers = self.browser.find_element(By.XPATH, '//a[contains(text(),"Выбор читателей")]')
        button_readers.click()
        assert 'https://www.sport-express.ru/news/?isHot=1' == 'https://www.sport-express.ru/news/?isHot=1', "Не верный урл Выбор читателей"

    def button_exclusive(self):
        button_exclusive = self.browser.find_element(By.XPATH, '//a[contains(text(),"Эксклюзив")]')
        button_exclusive.click()
        assert 'https://www.sport-express.ru/news/?isExclusive=1' == 'https://www.sport-express.ru/news/?isExclusive=1', "Не верный урл кнопки эксклюз"



