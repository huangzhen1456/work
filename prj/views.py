#coding=utf-8
import tornado.web
import tornado.gen
from prj.decorator import *


class MainHandler(tornado.web.RequestHandler):

    def get(self):

        items = {
            'content': u'欢迎光临镇镇的个人网站，正在建设中！'
        }
        self.render('../static/templates/index.html', items=items)


class NewsHandler(tornado.web.RequestHandler):
    def get(self):
        items = {
            'content': u'龙之谷手游最新内容！'
        }
        self.render('../static/templates/index.html', items=items)


class LoveHandler(tornado.web.RequestHandler):
    def get(self):
        items = {

        }
        self.render('../static/templates/love.html', items=items)

