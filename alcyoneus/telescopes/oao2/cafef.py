from typing import Union, List

from scrapy.loader import ItemLoader
from scrapy.exceptions import CloseSpider

from alcyoneus.citadel.client import get_source_decryption
from alcyoneus.telescopes.items import CosmicMessageItem

import scrapy
import re


class CafefSpider(scrapy.Spider):
    name = 'cafef.vn'

    decryption_rules = None

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        source_decryption = get_source_decryption(cls.name)
        if source_decryption:
            cls.decryption_rules = source_decryption
            cls.start_urls = [cls.decryption_rules.start_url]
            spider = super().from_crawler(crawler, *args, **kwargs)
            return spider
        raise CloseSpider(f"No `{cls.name}` spider decryption rules found!")

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

    def validate_pagination(self, response) -> bool:
        if response.url in self.start_urls:
            return True
        match = re.match(self.decryption_rules.pagination_limit, response.url)
        if match and match.group(1).isalnum():
            return int(match.group(1)) <= self.settings.get('PAGINATION_LIMIT', float('inf'))
        else:
            # Check by datetime
            return False

    def parse(self, response, **kwargs):
        # Parse Article links
        # yield from response.follow_all(xpath=self.decryption_rules.article_url, callback=self.parse)
        # Parse pagination
        if self.validate_pagination(response):
            yield from response.follow_all(xpath=self.decryption_rules.pagination,
                                           callback=self.parse)

    def parse_message(self, response, **kwargs):
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
