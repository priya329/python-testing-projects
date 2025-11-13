from scraper import get_quotes

def test_get_quotes():
    quotes = get_quotes()
    assert isinstance(quotes, list)
    assert len(quotes) > 0