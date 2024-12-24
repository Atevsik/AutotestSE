from pages.detalreviews import DetalReviews

def test_detalreviews(browser):
    detalreviews = DetalReviews(browser)
    detalreviews.open_detal_reviews()
    detalreviews.menu_nadlogo()
    detalreviews.podval()
    detalreviews.tegi(7)
    detalreviews.like_dis()
    detalreviews.podelit()
    detalreviews.proverka_podelit(5)
    detalreviews.perexod_calendar()
    detalreviews.selector_season()
    detalreviews.tour()
