from twisted.python.failure import Failure
from scrapy.logformatter import LogFormatter
from scrapy.utils.request import referer_str

import logging
import os


SCRAPEDMSG = "[SCRAPED]: %(src)s" + os.linesep
DROPPEDMSG = "[DROPPED]: %(exception)s" + os.linesep + "scraped from %(url)"
CRAWLEDMSG = "[CRAWLED]: (%(status)s) %(request)s%(request_flags)s (referer: %(referer)s)%(response_flags)s"
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
        return {
            'level': logging.DEBUG,
            'format': DROPPEDMSG,
            'exception': exception,
            'args': {
                'exception': exception,
                'url': response.url,
            }
        }

    def item_error(self, item, exception, response, spider):
        return {
            'level': logging.ERROR,
            'msg': ITEMERRORMSG,
            'args': {
                'url': response.url,
            }
        }