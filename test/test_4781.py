from pages.tennisraiting import TennisRaiting
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_tenisraiting(browser):
    tenisraiting = TennisRaiting(browser)
    tenisraiting.open()
    tenisraiting.menu_nadlogo()
    tenisraiting.vibor()
    tenisraiting.vibor()
    tenisraiting.vivod()
