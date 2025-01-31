from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class FormylaPailot:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/autosport/formula1/teams/')

    def text(self):
        text = self.browser.find_element(By.XPATH,"//span[contains(text(),'Команды')]")

    def menu_nad_logo(self):
        menu_nad_logo = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop se-menu-subtop--breadcrumb']")

    def oscar(self):
        oscar = self.browser.find_element(By.XPATH,"//div[4]//div[2]//div[1]//div[1]//div[2]//div[1]//div[2]//div[2]//div[1]//div[1]//div[1]//div[2]//a[1]")
        oscar.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/autosport/formula1/drivers/piastri-oskar-790/', "Не правильный оскар"
        self.browser.back()

    def comand(self):
        comand = self.browser.find_element(By.XPATH,"//a[normalize-space()='Alpine']")
        comand.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/autosport/formula1/teams/alpine-62/?season=2024', "Не правильная команда"
        self.browser.back()

    def eshe(self):
        eshe = self.browser.find_element(By.XPATH,"//div[@class='se-menu-subtop__link']")
        eshe.click()


    def pilot(self):
        pilot = self.browser.find_element(By.XPATH,"//a[contains(text(),'Пилоты')]")
        pilot.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/autosport/formula1/drivers/?season=2024', "Не правильный пилот"

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//span[contains(text(),'Пилоты')]")

    def bottas(self):
        bottas = self.browser.find_element(By.XPATH,"//a[contains(text(),'Валттери Боттас')]")
        bottas.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/autosport/formula1/drivers/bottas-valtteri-578/', "Не правильный боттас"
        self.browser.back()

    def mers(self):
        mers = self.browser.find_element(By.XPATH,"//div[15]//div[4]//div[1]//div[1]//a[1]//p[1]")
        mers.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/autosport/formula1/teams/mercedes-49/?season=2024', "Не правильный мерс"













