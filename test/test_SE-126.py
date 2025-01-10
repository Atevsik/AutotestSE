from pages.nakazanie import Nakazanie
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def test_nakazanie(browser):
    nakazanie = Nakazanie(browser)
    nakazanie.open()
    nakazanie.menu_nadlogo()
    nakazanie.filtri()
    nakazanie.player()
    nakazanie.reklama()