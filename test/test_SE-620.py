from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.pagefight import PageFight



def test_page_boets(browser):
    page_fight = PageFight(browser)


