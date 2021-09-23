import scraper

def test_buildResult():
    assert scraper.buildResult([1,2,3]) == 1

def test_formatSearchQuery():
    assert scraper.formatSearchQuery("1 2") == "1+2"