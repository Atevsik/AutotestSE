from pages.glavnfootball import GlavnFootball
from selenium.webdriver.common.by import By

def test_glavnnews(browser):
    glawnnews = GlavnFootball(browser)
    glawnnews.open_glavn_football()
    glawnnews.menu_nadlogo()
    glawnnews.plitka_glavn()
    glawnnews.glavn_news()
    glawnnews.news()
    glawnnews.video()
    glawnnews.reviews()
    glawnnews.podval()
    glawnnews.poll()
    glawnnews.result()
    glawnnews.title()
    glawnnews.sport_navigator()
    glawnnews.vid_materiala()
    glawnnews.block_reklama()
    glawnnews.bokmeker()
    glawnnews.stavka()
