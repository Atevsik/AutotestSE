from pages.onlinepage import OnlinePage
from selenium.webdriver.common.by import By

def test_onlinepage(browser):
    onlinepage = OnlinePage(browser)
    onlinepage.open_online()
    onlinepage.h1_news_online()
    onlinepage.button_online(3)
    onlinepage.button_photo_online()
    onlinepage.vid_sporta_button_online()
    onlinepage.vid_materiala_button_online()
