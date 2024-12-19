from selenium.webdriver.common.by import By
from pages.photopage import PhotoPage

def test_photopages(browser):
    photopage = PhotoPage(browser)
    photopage.open_photo()
    photopage.h1_news_photo()
    photopage.button_photo(3)
    photopage.button_photo_click()
    photopage.vid_sporta_button_photo()
    photopage.vid_materiala_button_photo()
    photopage.fig_button()


