from twisted.python.failure import Failure
from scrapy.logformatter import LogFormatter
from scrapy.utils.request import referer_str

import logging
import os


STOREDMSG = "[STORED]: %(url)s"
SCRAPEDMSG = "[SCRAPED]: %(src)s" + os.linesep
DROPPEDMSG = "[DROPPED]: %(exception)s" + os.linesep + "scraped from %(url)"
CRAWLEDMSG = "[CRAWLED]: (%(status)s) %(request)s%(request_flags)s (referer: %(referer)s)%(response_flags)s"
PIPEERRORMSG = "[PERROR]: `%(exception)s` when processing %(url)s"
ITEMERRORMSG = "[ERROR]: processing %(url)"
SPIDERERRORMSG = "Spider error processing %(request)s (referer: %(referer)s)"
DOWNLOADERRORMSG_SHORT = "Error downloading %(request)s"
DOWNLOADERRORMSG_LONG = "Error downloading %(request)s: %(errmsg)s"


class AlcyoneusLogFormatter(LogFormatter):
    def crawled(self, request, response, spider):
        """Logs a message when the crawler finds a webpage."""
        request_flags = f' {str(request.flags)}' if request.flags else ''
        response_flags = f' {str(response.flags)}' if response.flags else ''
        return {
            'level': logging.DEBUG,
            'msg': CRAWLEDMSG,
            'args': {
                'status': response.status,
                'request': request,
                'request_flags': request_flags,
                'referer': referer_str(request),
                'response_flags': response_flags,
                # backward compatibility with Scrapy logformatter below 1.4 version
                'flags': response_flags
            }
        }

    def stored(self, item, spider):
        """Logs a message when a spider stores an item."""
        return {
            'level': logging.DEBUG,
            'msg': STOREDMSG,
            'args': {
                'url': item['url'],
            }
        }

    def scraped(self, item, response, spider):
        """Logs a message when an item is scraped by a spider."""
        if isinstance(response, Failure):
            src = response.getErrorMessage()
        else:
            src = response
        return {
            'level': logging.DEBUG,
            'msg': SCRAPEDMSG,
            'args': {
                'src': src,
            }
        }

    def dropped(self, item, exception, response, spider):
        """Logs a message when an item is dropped while it is passing through the item pipeline."""
        return {
            'level': logging.DEBUG,
            'format': DROPPEDMSG,
            'exception': exception,
            'args': {
                'exception': exception,
                'url': response.url,
            }
        }

    def pipe_error(self, item, exception, spider):
        """Logs a message when an item causes an error while it is passing
                through the item pipeline.

        .. versionadded:: 2.0
        """
        return {
            'level': logging.ERROR,
            'msg': PIPEERRORMSG,
            'args': {
                'exception': str(exception),
                'url': item['url'],
            }
        }

    def item_error(self, item, exception, response, spider):
        """Logs a message when an item causes an error while it is passing
                through the item pipeline.

        .. versionadded:: 2.0
        """
        return {
            'level': logging.ERROR,
            'msg': ITEMERRORMSG,
            'args': {
                'url': response.url,
            }
        }

    def spider_error(self, failure, request, response, spider):
        """Logs an error message from a spider.

        .. versionadded:: 2.0
        """
        return {
            'level': logging.ERROR,
            'msg': SPIDERERRORMSG,
            'args': {
                'request': request,
                'referer': referer_str(request),
            }
        }

    def download_error(self, failure, request, spider, errmsg=None):
        """Logs a download error message from a spider (typically coming from
        the engine).

        .. versionadded:: 2.0
        """
        args = {'request': request}
        if errmsg:
            msg = DOWNLOADERRORMSG_LONG
            args['errmsg'] = errmsg
        else:
            msg = DOWNLOADERRORMSG_SHORT
        return {
            'level': logging.ERROR,
            'msg': msg,
            'args': args,
        }