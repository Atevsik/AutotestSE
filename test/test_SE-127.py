from pages.srball import SrBall
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def test_srball(browser):
    srball = SrBall(browser)
    srball.open()
    srball.menu_nadlogo()
    srball.triigroka(3)
    srball.perexod_igrok()