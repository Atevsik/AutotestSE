from pages.cotakts import Contakt
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_podpiska(browser):
    contakt = Contakt(browser)
    contakt.open()
    contakt.h1()
    contakt.email()
    contakt.tel()
    contakt.podpiska()
    contakt.h2()
    contakt.oformit()

