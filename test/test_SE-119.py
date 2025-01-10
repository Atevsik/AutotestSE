from pages.mc1 import Mc1
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def test_mc1(browser):
    mc1 = Mc1(browser)
    mc1.open()
    mc1.menu_nadlogo()
    mc1.reklama()
    mc1.booker()
    mc1.vid_materiala()
    mc1.filtr_date()
    mc1.football_mc()
    mc1.logo_bok()
    mc1.stavki()