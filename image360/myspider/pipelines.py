# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from urllib import request

#r='http://p0.so.qhmsg.com/t010f249a371fd6624f.jpg'


class MyspiderPipeline(object):
    def __init__(self):
        self.path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'image')
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        title=item['title']
        #获取的URL有时候为list，有时候是一个单独的url
        #如果出现错误，抛出的是不可识别的url:'h'的时候，就说明只有一个url
        #这样访问是必然会出错的
        url=item['url']
        image_name=url.split('.')[-1]
        #注意urllib.request.urlretrieve下载保存图片的时候，一定要对应好格式
        #要一定指明好路径和名字，否则打不开，或者出错 例如'123.jpg'才是正确的写法
        request.urlretrieve(url,os.path.join(self.path,(title+'.jpg')))
        return item

# class ImagePipeline(ImagesPipeline):
#     def file_path(self, request, response=None, info=None):
#         url = request.url
#         file_name = url.split('/')[-1]
#         return file_name
#
#     def item_completed(self, results, item, info):
#         image_paths = [x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem('Image Downloaded Failed')
#         return item
#
#     def get_media_requests(self, item, info):
#         yield scrapy.Request(item['url'])
