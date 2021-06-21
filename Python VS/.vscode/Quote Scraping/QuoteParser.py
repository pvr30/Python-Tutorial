from .QuotesLocators import QuoteLocator

class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def content(self):
        locator = QuoteLocator.CONTENT_LOCATOR