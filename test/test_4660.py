from selenium.webdriver.common.by import By
from pages.storypage import StoryPage

def test_storypage(browser):
    storypage = StoryPage(browser)
    storypage.open_story()
    storypage.h1_news_story()
    storypage.button_story(3)
    storypage.button_story_click()
    storypage.vid_sporta_button_story()
    storypage.vid_materiala_button_story()
    storypage.bask_button()
    storypage.button_nextpage()





