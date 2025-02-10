from pages.datallive import DetalLive
from selenium.webdriver.common.by import By

def test_detallive(browser):
    detallive = DetalLive(browser)
    detallive.open_detal_live()
    detallive.menu_nadlogo()
    detallive.datelive()
    detallive.podval()
    detallive.dopknopkalive()
    detallive.videoclicklive()
    detallive.h1_video()
