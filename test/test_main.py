from selenium.webdriver.common.by import By
import time
from pages.homepage import HomePage

def test_open_sp(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.se_click()




