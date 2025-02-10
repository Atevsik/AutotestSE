from pages.mcfootball import McFootball
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def test_mcfootball(browser):
    mcfootball = McFootball(browser)
    mcfootball.open()
    mcfootball.football_mc()
    mcfootball.filtr_date()
    mcfootball.knopka_kalendar()
    mcfootball.tomorow()
    mcfootball.logo_bok()
    mcfootball.stavki()
    mcfootball.podval()
    mcfootball.navigator_sport()
    mcfootball.regbi()
    mcfootball.read_news()
