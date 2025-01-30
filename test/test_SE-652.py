from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.tennisbill import TennisBilly



def test_tennis_big(browser):
    bill = TennisBilly(browser)
    bill.open()
    bill.news()
    bill.reviews()
    bill.result()
    bill.reklama()








