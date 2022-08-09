class StoreCMessagePipeline:
    def __init__(self, stats):
        self.session = None
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        return cls(stats=crawler.stats)

    def open_spider(self, spider):
        self.session = db_session_mysql()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        return item


