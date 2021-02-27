import re
import scrapy
import json


class Target(scrapy.Spider):
    name = 'target'

    def __init__(self, name=None, url='', **kwargs):
        super().__init__(name, **kwargs)
        self.url = url

    def start_requests(self):
        self.tcin = re.findall('A-(\d+)', self.url)[0]
        url = f'https://redsky.target.com/redsky_aggregations/v1/web/pdp_client_v1?key=ff457966e64d5e877fdbad070f276d18ecec4a01&tcin={self.tcin}&store_id=2188&has_store_id=true&pricing_store_id=2188&scheduled_delivery_store_id=none&has_scheduled_delivery_store_id=false&has_financing_options=false'
        headers = {"Upgrade-Insecure-Requests": "1",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                   "Sec-Fetch-Site": "none",
                   "Sec-Fetch-Mode": "navigate",
                   "Sec-Fetch-User": "?1",
                   "Sec-Fetch-Dest": "document"}
        yield scrapy.FormRequest(url=url, callback=self.parse, dont_filter=True, headers=headers)

    def parse(self, response):

        data = json.loads(response.text)
        try:
            title = data['data']['product']['item']['product_description']['title']
        except:
            title = ''
        try:
            tcin = data['data']['product']['children'][0]['tcin']
        except:
            tcin = ''
        try:
            upc = data['data']['product']['children'][0]['item']['primary_barcode']
        except:
            upc = ''
        try:
            price = data['data']['product']['price']['current_retail_min']
        except:
            price = ''
        try:
            description = data['data']['product']['item']['product_description']['downstream_description']
        except:
            description = ''
        try:
            specs = data['data']['product']['item']['product_description']['bullet_descriptions']
            specification = dict()
            for spec in specs:
                spec = spec.replace('<B>', '').replace('</B>', '').split(':')
                specification.update({

                    spec[0].strip(): spec[1].strip()
                })

        except:
            specification = dict()

        output = {
            "url": self.url,
            "tcin": tcin,
            "upc": upc,
            "price": price,
            "currency": 'USD',
            "title": title,
            "description": description,
            "specs": specification

        }
        print(output)


from scrapy.cmdline import execute

# execute("scrapy crawl target -a url=https://www.target.com/p/levi-s-men-s-512-slim-taper-fit-jeans/-/A-79691588".split())
