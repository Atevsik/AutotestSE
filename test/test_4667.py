from pages.detalvideo import DetalVideo
from selenium.webdriver.common.by import By

def test_detalvideo(browser):
    detalvideo = DetalVideo(browser)
    detalvideo.open_detal_video()
    detalvideo.menu_nadlogo()
    detalvideo.podval()
    detalvideo.eshe()
    detalvideo.perexod_stadium()
    detalvideo.h1_stadium()
    detalvideo.table_stadium()
    detalvideo.stadium_click()
    detalvideo.tag_stadium_check()