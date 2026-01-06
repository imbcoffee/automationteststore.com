from Pages.home import HomePage
from Config.prod import BASE_URL, EXPECTED_TITLE


def test_pilot(driver):
    home_page= HomePage(driver)
    home_page.open(BASE_URL)
    title= home_page.get_title()
    assert title==EXPECTED_TITLE, "Title is incorrect"


#latest code



