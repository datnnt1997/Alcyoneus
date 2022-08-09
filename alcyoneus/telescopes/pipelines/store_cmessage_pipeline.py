__name__ = 'pipeline.store_cmessage'
from scrapy.utils.log import logformatter_adapter

from alcyoneus.citadel.client import db_session_mysql
from alcyoneus.citadel.models import CosmicMessage

import logging

logger = logging.getLogger(__name__)


class StoreCMessagePipeline:
    def __init__(self, stats, logformatter):
        self.session = None
        self.stats = stats
        self.logformatter = logformatter

    @classmethod
    def from_crawler(cls, crawler):
        return cls(stats=crawler.stats, logformatter=crawler.logformatter)

    def open_spider(self, spider):
        self.session = db_session_mysql()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        logkws = None
        try:
            new_message = CosmicMessage(**item)
            self.session.add(new_message)
            self.session.flush()
            logkws = self.logformatter.stored(item=item, spider=spider)
        except Exception as e:
            self.session.rollback()
            logkws = self.logformatter.pipe_error(item=item, exception=e, spider=spider)
        finally:
            if logkws is not None:
                logger.log(*logformatter_adapter(logkws), extra={"spider": spider})
        return item


