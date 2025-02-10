from pages.golpas import GolAndPass
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def test_golpas(browser):
    golpas = GolAndPass(browser)
    golpas.open()
    golpas.menu_nadlogo()
    golpas.filtri()
    golpas.top3(3)
    golpas.player()