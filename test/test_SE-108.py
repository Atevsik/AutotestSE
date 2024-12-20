from selenium.webdriver.common.by import By
from pages.newspaperpage import PaperGazeta

def test_newspapers(browser):
    newspaperspage = PaperGazeta(browser)
    newspaperspage.open_gazeta()
    newspaperspage.calendar_gazet()
    newspaperspage.calendar_gazet_prov()
    newspaperspage.filtr_gaz()
    newspaperspage.vid_sporta_gaz()
    newspaperspage.proverka_Vid_sporta()






