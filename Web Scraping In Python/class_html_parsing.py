# Using class we can make thing in a simpler way.


import re
from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''


class ParserItemLocator:

    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod div p'
    RATING_LOCATOR = 'article.product_pod p.star-rating'




class ParserItem:

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = ParserItemLocator.NAME_LOCATOR
        title = self.soup.select_one(locator).attrs['title']
        return title

    @property
    def link(self):
        locator = ParserItemLocator.LINK_LOCATOR
        link = self.soup.select_one(locator).attrs['href']
        return link

    @property
    def price(self):
        locator = ParserItemLocator.PRICE_LOCATOR
        price = self.soup.select_one(locator).string
        return price

    @property
    def rating(self):
        locator = ParserItemLocator.RATING_LOCATOR
        rating = self.soup.select_one(locator)
        star_rating_class = rating.attrs['class']
        rating_classes = [s for s in star_rating_class if s != 'star_rating']
        return rating_classes[1]  # Three


item = ParserItem(ITEM_HTML)

# Now You Can Call Function like this.

print(item.name)
print(item.link)
print(item.price)
print(item.rating)