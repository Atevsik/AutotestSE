from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageFight:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.sport-express.ru/tag/hoakin-bakli-25917/')



