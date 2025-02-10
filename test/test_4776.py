from pages.statisticplayer import StatisticPlayer
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def test_statisticplayer(browser):
    stplayer = StatisticPlayer(browser)
    stplayer.open()
    stplayer.menu_nadlogo()
    stplayer.kard()
    stplayer.infkard()
    stplayer.match()
    stplayer.reklama()
    stplayer.sopernik()
    stplayer.dinamo()
    stplayer.legend()