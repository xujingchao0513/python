# -*- coding: utf-8 -*-
import scrapy

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
import re


class URLredirect(scrapy.Spider):
    name = 'urlredirect_spider'

    def start_requests(self):
        reqs = []
        url = 'http://www.iqiyi.com/v_19rrk4vf0k.html'
        req = scrapy.Request(url, headers=headers, meta={'url': url})
        reqs.append(req)
        return reqs

    def parse(self, response):
        responseURL = response.url
        requestURL = response.meta['url']
        print ('''Response's URL: ''', response.url)
        print ('''Request's  URL: ''', response.meta['url'])
        if str(responseURL).__eq__(requestURL):
            print (re.compile('<title>(.*?)</title>').findall(response.body)[0].decode('utf-8'))
        else:
            print ('--------------------->>>>>>>>Your request is redirect,retrying.....<<<<<-------------------------')
            yield scrapy.Request(url=requestURL, headers=headers, meta={'url': requestURL}, callback=self.parse)
