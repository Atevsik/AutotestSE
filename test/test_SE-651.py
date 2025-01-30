from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.tennisdevis import TennisDevis



def test_tennis_big(browser):
    devis = TennisDevis(browser)
    devis.open()
    devis.reviews()
    devis.news()
    devis.result()
    devis.god()
    devis.grupp()
    devis.reklama()








