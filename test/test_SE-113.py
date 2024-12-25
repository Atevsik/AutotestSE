from pages.newsphoto import NewsPhoto
from selenium.webdriver.common.by import By

def test_detalphoto(browser):
    newsphoto = NewsPhoto(browser)
    newsphoto.open_photo_news()
    newsphoto.menu_nadlogo()
    newsphoto.selector_photo()
    newsphoto.comento_scroll()
    newsphoto.commento_check()
    newsphoto.commento_check_newComment()
    newsphoto.podval()
    newsphoto.click_statistik()
    newsphoto.statistik_select()
    newsphoto.igrok_statistik()
    newsphoto.top3(3)


