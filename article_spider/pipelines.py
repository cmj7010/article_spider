# -*- coding: utf-8 -*-
#与数据存储相关
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ArticleSpiderPipeline(object):
    def process_item(self, item, spider):
        return item