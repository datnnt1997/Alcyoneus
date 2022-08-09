from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst, Join

from .normalizer import (ConvertToDatetime, ConvertToJsonString,
                         NormalizeText, NormalizeAuthor)


class CosmicMessageItem(Item):
    """
    CITADEL Tabel: `cosmic_message`
    """
    sid: int = Field(output_processor=TakeFirst())
    cid: int = Field(output_processor=TakeFirst())
    url: str = Field(output_processor=TakeFirst())
    title: str = Field(input_processor=MapCompose(NormalizeText()),
                       output_processor=TakeFirst())
    author: str = Field(input_processor=MapCompose(NormalizeText(), NormalizeAuthor()),
                        output_processor=TakeFirst())
    tags: str = Field(input_processor=MapCompose(NormalizeText()),
                      output_processor=ConvertToJsonString())
    description: str = Field(input_processor=MapCompose(NormalizeText()),
                             output_processor=Join('\n'))
    abstract: str = Field(input_processor=MapCompose(NormalizeText()),
                          output_processor=Join('\n'))
    content: str = Field(input_processor=MapCompose(NormalizeText()),
                         output_processor=Join('\n'))
    media: str = Field(output_processor=ConvertToJsonString())
    pub_time: str = Field(
        input_processor=MapCompose(ConvertToDatetime()),
        output_processor=TakeFirst())

    def to_dict(self):
        return self.__dict__['_values']
