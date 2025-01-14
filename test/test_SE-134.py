from pages.mmaraiting import MmaRaiting
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_mmarait(browser):
    mmarait = MmaRaiting(browser)
    mmarait.open()
    mmarait.menu_nadlogo()
    mmarait.h1()
    mmarait.boets(15)
    mmarait.champion()
    mmarait.stolb(4)
    mmarait.japan()
    mmarait.prom()
    mmarait.prom1()
    mmarait.reklama()
    mmarait.seson()
    mmarait.seson2()
    mmarait.raitingi()
    mmarait.dopprover()
