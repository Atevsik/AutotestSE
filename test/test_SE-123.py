from pages.calendargame import CalendarGame
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def test_tablecomands(browser):
    calendargame = CalendarGame(browser)
    calendargame.open()
    calendargame.match()
    calendargame.podval()
