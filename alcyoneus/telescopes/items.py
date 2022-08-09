# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy import Item, Field
from itemloaders.processors import MapCompose

from .normalizer import ConvertToDatetime


class CosmicMessageItem(Item):
    """
    CITADEL Tabel: `cosmic_message`
    """
    sid: int = Field()
    cid: int = Field()
    url: str = Field()
    title: str = Field()
    author: str = Field()
    tags: str = Field()
    description: str = Field()
    abstract: str = Field()
    content: str = Field()
    media: str = Field()
    pub_time: str = Field(
        input_processor=MapCompose(ConvertToDatetime))

    def to_dict(self):
        return self.__dict__['_values']