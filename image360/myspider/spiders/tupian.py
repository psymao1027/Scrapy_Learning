# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
#http://images.so.com/zj?ch=food&t1=299&sn=0&listtype=new&temp=1
#http://images.so.com/zj?ch=food&t1=299&sn=30&listtype=new&temp=1
#http://images.so.com/zj?ch=food&t1=299&sn=360&listtype=new&temp=1
import json
from myspider.items import MyspiderItem


class TupianSpider(scrapy.Spider):
    name = 'tupian'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com']

    def start_requests(self):
        base_url='http://images.so.com/zj?'
        i=0
        #让蜘蛛无限爬取下去
        while True:
            data={
                'ch':'food',
                't1':'299',
                'sn':i*30,
                'listtype':'new',
                'temp':1
                  }
            i=i+1
            #urlencode(),可以把每一个字典中的K-V，都转化为A&b&C&D这种形式
            params=urlencode(data)
            url=base_url+params
            yield scrapy.Request(url,callback=self.parse)

    def parse(self,response):
        #获取json数据
        result=json.loads(response.text)
        for image in result.get('list'):
            item=MyspiderItem()
            #item['id'] = image.get('imageid')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            yield item
















