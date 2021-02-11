import sys

sys.path.append("C:\\Users\\86156\\Desktop\\pyspider")
from common.spider import AsyncSpider
from utils.log import get_logger

logger = get_logger("example_spider")


class ExampleSpider(AsyncSpider):
    proxy = ""
    worker_numbers = 4
    concurrency = 16
    retry_time = 1

    @staticmethod
    def make_headers():
        headers = {
            "authority": "ec.snssdk.com",
            "accept": "application/json, text/plain, */*",
            "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
            "origin": "https://haohuo.jinritemai.com",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://haohuo.jinritemai.com/",
            "accept-language": "zh-CN,zh;q=0.9",
        }
        return headers

    async def start_requests(self):
        shop_list = [
            "aDpceDB",
            "JIBMdzz",
            "QqkdRkd",
            "JlLHLNH",
            "wxATQZg",
            "zYfkZcb",
            "zYfkZcb",
            "hxiESSw",
            "lVKMfKy",
            "qIvUBNX",
            "PAZfwKy",
        ]
        for shop_id in shop_list[:]:
            for page in range(1, 2):
                url = f"https://ec.snssdk.com/shop/goodsList?shop_id={shop_id}&size=10&page={page}&b_type_new=0&device_id=0&is_outside=1"
                method = "GET"
                headers = self.make_headers()
                yield self.Request(
                    url,
                    method,
                    headers,
                    callback=self.parse,
                )
        # url = 'http://quotes.toscrape.com/page/1/'
        # yield self.Request(url, callback=self.parse)

    async def parse(self, res):
        self.logger.info(res.text)
        yield res.text
        for i in range(2, 3):
            url = f"http://quotes.toscrape.com/page/{i}/"
            yield self.Request(url, callback=self.parse_item)

    def parse_item(self, res):
        self.logger.info(res.text)


ExampleSpider.start(logger=logger, env="")
