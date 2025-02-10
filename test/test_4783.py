from pages.cardplayer import CardPlayer
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_cardpayer(browser):
    cardpayer = CardPlayer(browser)
    cardpayer.open()
    cardpayer.menu_nadlogo()
    cardpayer.info()
    cardpayer.match()
    cardpayer.click_match()
    cardpayer.reklama()
    cardpayer.filtr()