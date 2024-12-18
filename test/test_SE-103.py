from selenium.webdriver.common.by import By
from pages.newspage import NewsPage

def test_newspage(browser):
    newspage = NewsPage(browser)
    newspage.open()
    newspage.logo_news()
    newspage.button_glvn(3)
    newspage.button_glvn_click()
    newspage.button_exclusive()
    newspage.button_readers()