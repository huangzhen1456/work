#coding=utf-8
import tornado.web
import tornado.gen
from prj.decorator import *
from prj.sql import SQL
from prj.user.models import *


class MainHandler(tornado.web.RequestHandler):
    #首页
    def get(self):

        items = {
            'content': u'欢迎光临黄镇的个人网站，正在建设中！'
        }
        self.render('../static/templates/index.html', items=items)


class LoveHandler(tornado.web.RequestHandler):
    #520专题
    def get(self):
        items = {

        }
        self.render('../static/templates/love.html', items=items)


class LoveBookHandler(tornado.web.RequestHandler):
    #520book
    def get(self):
        items = {

        }
        self.render('../static/templates/lovebook.html', items=items)


class DanMuHandler(tornado.web.RequestHandler):
    #弹幕测试
    def __init__(self, application, request, **kwargs):
        super(DanMuHandler, self).__init__(application, request, **kwargs)
        self.sql = SQL()

    def on_finish(self):
        # close sql connection
        self.sql.close()

    def get(self):

        user = self.sql.query(User).filter(User.name == 'huangzhen')
        items = {
            'user': user
        }
        self.render('../static/templates/danmu.html', items=items)
