def test_title(browser):
    browser.get(browser.url)
    assert "Your Store" in browser.title
