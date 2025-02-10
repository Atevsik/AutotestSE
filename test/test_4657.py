from selenium.webdriver.common.by import By
from pages.reviewspage import ReviewsPage

def test_reviewspage(browser):
    reviewspage = ReviewsPage(browser)
    reviewspage.open()
    reviewspage.h1_rev()
    reviewspage.button_glvn_rev(3)
    reviewspage.button_glvn_click_rev()
    reviewspage.button_readers_rev()
    reviewspage.button_exclusive_rev()
    reviewspage.vid_materiala_button_rev()
    reviewspage.vid_sporta_button_rev()
    reviewspage.hockey_button()