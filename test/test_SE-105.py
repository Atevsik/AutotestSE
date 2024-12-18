from selenium.webdriver.common.by import By
from pages.videopage import VideoPage

def test_reviewspage(browser):
    videopage = VideoPage(browser)
    videopage.open_video()
    videopage.h1_news_video()
    videopage.button_video(3)
    videopage.button_video_click()
    videopage.button_readers_video()
    videopage.button_exclusive_video()
