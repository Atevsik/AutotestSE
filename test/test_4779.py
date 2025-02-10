from pages.stadions import Stadion
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def test_stadion(browser):
    stadion = Stadion(browser)
    stadion.open()
    stadion.menu_nadlogo()
    stadion.h1()
    stadion.scrolsmi()
    stadion.smi2()
