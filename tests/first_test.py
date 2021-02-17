TITLE = "Your Store"

def test_title(browser):
    browser.open("")
    assert TITLE in browser.title