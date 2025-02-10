from selenium.webdriver.common.by import By
from pages.videopage import VideoPage
from time import sleep

def test_videopage(browser):
    videopage = VideoPage(browser)
    videopage.open_video()
    videopage.h1_news_video()
    videopage.button_video(3)
    videopage.button_video_click()
    videopage.button_readers_video()
    videopage.button_exclusive_video()
    videopage.vid_sporta_button_vid()
    videopage.vid_materiala_button_vid()
    videopage.mma_button()

