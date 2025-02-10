from pages.detalstory import DetalStory
from selenium.webdriver.common.by import By

def test_detalstory(browser):
    detalsory = DetalStory(browser)
    detalsory.open_detal_story()
    detalsory.menu_nadlogo()
    detalsory.podval()
    detalsory.block_reviews()
    detalsory.block_news()
    detalsory.block_video()
    detalsory.block_photo()
    detalsory.rev_knp(4)
    detalsory.click_knp()
    detalsory.calendar_nad_menu()
    detalsory.h1_calend_det()
    detalsory.filtri()
    detalsory.click_match()