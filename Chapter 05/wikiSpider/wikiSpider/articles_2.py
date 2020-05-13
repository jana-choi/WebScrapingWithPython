#https://docs.scrapy.org/en/latest/news.html#deprecation-removals
from scrapy.linkextractors import LinkExtractor #from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule    #from scrapy.contrib.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    name = "articles"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Benevolent_dictator_for_life"]
    rules = [
        Rule(LinkExtractor(allow="en.wikipedia.org/wiki/((?!:).)*$"),
            callback="parse_items", follow=True,
            cb_kwargs={"is_article": True}),
        Rule(LinkExtractor(allow=".*"), callback="parse_items",
            cb_kwargs={"is_article": False})
    ]

    def parse_items(self, response, is_article):
        url = response.url
        title = response.css("h1::text").extract_first()

        print("\n========================================================================")
        print("★★★ URL is: {}".format(url))

        if is_article:
            text = response.xpath("//div[@id=\"mw-content-text\"]//text()").extract()
            lastUpdated = response.css("li#footer-info-lastmod::text").extract_first()
            lastUpdated = lastUpdated.replace("This page was last edited on ", "")
           
            print("★★★ Title is: {}".format(title))
            print("★★★ Last updated: {}".format(lastUpdated))
            # print("★★★ Text is: {}".format(text))
        else:
            print("★★★ This is not an article: {}".format(title))

    def parse_items(self, response, is_article):
        url = response.url
        title = response.css("h1::text").extract_first()

        print("\n========================================================================")
        print("★★★ URL is: {}".format(url))

        if is_article:
            text_rule = "//div[@id=\"mw-content-text\"]//text()"
            text = response.xpath(text_rule).extract()

            update_rule = "li#footer-info-lastmod::text"
            update_delete = "This page was last edited on "
            lastUpdated = response.css(update_rule).extract_first()
            lastUpdated = lastUpdated.replace(update_delete, "")
            
            print("★★★ Title is: {}".format(title))
            print("★★★ Last updated: {}".format(lastUpdated))
            # print("★★★ Text is: {}".format(text))
        else:
            print("★★★ This is not an article: {}".format(title))
