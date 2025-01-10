from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class Nakazanie:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/football/L/russia/first/2023-2024/statistics/cards/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def filtri(self):
        filtri = self.browser.find_element(By.XPATH, "//div[@class='se19-select-wr mb_20']")

    def player(self):
        player = self.browser.find_element(By.XPATH, "//a[contains(text(),'Заурбек Плиев')]")
        player.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/player/21733/seasons/2024-2025/', "Не правиьный урл игрока"
        self.browser.back()

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")









