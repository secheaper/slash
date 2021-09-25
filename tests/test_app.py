import formatter
import scraper
import formatter

def test_formatSearchQuery():
    assert formatter.formatSearchQuery("1 2") == "1+2"

def test_sortList():
    arr = [{"price":"$10"}, {"price":"$20"}, {"price":"$0"}]
    ansArr = [{"price":"$0"}, {"price":"$10"}, {"price":"$20"}]
    revAnsArr = [{"price":"$20"}, {"price":"$10"}, {"price":"$0"}]
    test1 = formatter.sortList(arr, "pr", False) == ansArr
    test2 = formatter.sortList(arr, "pr", True) == revAnsArr
    assert test1 and test2

def test_formatTitle():
    test1 = formatter.formatTitle("0"*50) == "0"*40+"..."
    test2 = formatter.formatTitle("0"*5) == "0"*5
    assert test1 and test2

def test_getNumbers():
    test1 = formatter.getNumbers("some chars and $10.00") == 10.0
    test2 = formatter.getNumbers("some chars and $10.99 some other chars") == 10.99
    assert test1 and test2