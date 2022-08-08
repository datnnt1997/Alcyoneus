from typing import Union, List

from citadel.client import get_source_decrption
from telescopes.items import CosmicMessageItem

from scrapy.loader import ItemLoader

import scrapy


class CafefSpider(scrapy.Spider):
    name = 'cafef.vn'

    decryption_rules = get_source_decrption(name)

    def extract_url(self, response) -> str:
        return response.url

    def extract_category(self, response) -> Union[str, None]:
        return response.xpath(self.decryption_rules.category).get()

    def extract_title(self, response) -> str:
        return response.xpath(self.decryption_rules.title).get()

    def extract_author(self, response) -> Union[str, None]:
        if self.decryption_rules.author is None:
            return None
        return response.xpath(self.decryption_rules.author).get()

    def extract_tags(self, response) -> Union[List[str], None]:
        if self.decryption_rules.tags is None:
            return None
        return response.xpath(self.decryption_rules.tags).getall()

    def extract_description(self, response) -> Union[str, None]:
        if self.decryption_rules.description is None:
            return None
        return response.xpath(self.decryption_rules.description).get()

    def extract_content(self, response) -> Union[List[str], None]:
        if self.decryption_rules.content is None:
            return None
        return response.xpath(self.decryption_rules.content).getall()

    def extract_media(self, response) -> Union[List[str], None]:
        if self.decryption_rules.media is None:
            return None
        return response.xpath(self.decryption_rules.media).getall()

    def extract_pub_time(self, response) -> Union[str, None]:
        if self.decryption_rules.pub_time is None:
            return None
        return response.xpath(self.decryption_rules.pub_time).get()

    def start_requests(self):
        return [scrapy.Request(url=self.decryption_rules.start_url, callback=self.parse_pagination_and_article_links)]

    def parse_pagination_and_article_links(self, response, **kwargs):
        # Parse Article links
        yield from response.follow_all(xpath=self.decryption_rules.article_url, callback=self.parse)
        # Parse pagination
        yield from response.follow_all(xpath=self.decryption_rules.pagination,
                                       callback=self.parse_pagination_and_article_links)

    def parse(self, response, **kwargs):
        loader = ItemLoader(item=CosmicMessageItem(), selector=response)
        loader.add_value('sid', self.decryption_rules.sid)
        loader.add_value('cid', self.extract_category(response))
        loader.add_value('url', self.extract_url(response))
        loader.add_value('title', self.extract_title(response))
        loader.add_value('author', self.extract_author(response))
        loader.add_value('tags', self.extract_tags(response))
        loader.add_value('description', self.extract_description(response))
        loader.add_value('content', self.extract_content(response))
        loader.add_value('media', self.extract_media(response))
        loader.add_value('pub_time', self.extract_pub_time(response))
        return loader.load_item()



