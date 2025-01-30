from pages.detalnews import DetalNews
from selenium.webdriver.common.by import By

def test_detalnews(browser):
    detalnews = DetalNews(browser)
    detalnews.open_detal_news()
    detalnews.menu_nadlogo()
    detalnews.polog_comand()
    detalnews.polog_comand1()
    detalnews.right_news()
    detalnews.samie_obsyj()
    detalnews.podval()
    detalnews.perexod_table()
    detalnews.perexod()
    detalnews.block_comment()
    detalnews.block_commetn_click()