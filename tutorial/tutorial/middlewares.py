from fake_useragent import UserAgent


class RandomUserAgentMiddleware(object):

    def __init__(self):
        self.ua = UserAgent()

    def process_request(self, request, spider):
        if hasattr(spider, 'user_agent'):
            request.headers['User-Agent'] = spider.user_agent
        else:
            new_ua = self.ua.random
            # print('-----------------------' + new_ua)
            request.headers['User-Agent'] = new_ua
