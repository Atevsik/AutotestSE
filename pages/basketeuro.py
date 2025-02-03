from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasketEuro:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/basketball/euroleague/')

    def menu_nadlogo(self):
        menu_nadlogo = self.browser.find_element(By.XPATH, '//div[@class="se-menu-subtop se-menu-subtop--breadcrumb"]')

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_15645683733586888']")

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH, "//div[contains(text(),'Статьи')]")

    def news(self):
        news = self.browser.find_element(By.XPATH, "//div[@class='se-newsline']//section[@class='se-titled-block']")

    def photo(self):
        photo = self.browser.find_element(By.XPATH,"//div[contains(text(),'Фото')]")

    def podval(self):
        podval = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")

    def women(self):
        women = self.browser.find_element(By.XPATH,"//a[contains(text(),'Женщины')]")
        women.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/basketball/L/women/euroleague/2024-2025/', "не правильные женщины"

    def group(self,count):
        group = self.browser.find_elements(By.XPATH,"//td[@class='fs_18 t_left ph_10 nowrap']")
        assert len(group) == count











