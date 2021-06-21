import requests
from bs4 import BeautifulSoup

# Main Page Locators
class QuotesPageLocators:
    QUOTES = 'div.quote'

# For Location Of Particular Attributes
class QuotesLocators:
    CONTENT_LOCATOR = 'span.text'
    AUTHOR_LOCATOR = 'small.author'
    TAGS_LOCATORS = 'div.tags a.tag'

# To Get Content in __repr__ method and for scraping


class QuotesParser:
    def __init__(self, parent):
        self.parent = parent


    def __repr__(self):
        return f"Quote : {self.content} By {self.author}"

    @property
    def content(self):
        locator = QuotesLocators.CONTENT_LOCATOR
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuotesLocators.AUTHOR_LOCATOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuotesLocators.TAGS_LOCATORS
        return self.parent.select(locator).string


# For Scraping page using BeautifulSoup
class QuotePage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        return [QuotesParser(e) for e in self.soup.select(QuotesPageLocators.QUOTES)]


page_content = requests.get('http://quotes.toscrape.com').content
page = QuotePage(page_content)

for quote in page.quotes:
    print(quote.author)
    print(quote)
    print('\n')
