from pages.pollpage import PollPage
from selenium.webdriver.common.by import By

def test_pollpage(browser):
    polpage = PollPage(browser)
    polpage.open_poll()
    polpage.h1_news_poll()
    polpage.button_poll(3)
    polpage.button_photo_poll()
    polpage.vid_sporta_button_poll()
    polpage.vid_materiala_button_poll()
    polpage.knopka_eshe_poll()
    polpage.knopka_eshe_poll_click()

