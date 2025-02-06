from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.rplglavn import FootbalGlavn


def test_rpl_gol(browser):
   glan_rpl = FootbalGlavn(browser)
   glan_rpl.open()
   glan_rpl.comands(16)
   glan_rpl.krilia()
   glan_rpl.legend()



