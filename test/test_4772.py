from pages.bombardiers import Bombardiers
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def test_bombordiers(browser):
    bombordiers = Bombardiers(browser)
    bombordiers.open()
    bombordiers.menu_nadlogo()
    bombordiers.filtri()
    bombordiers.top3(3)
    bombordiers.player()