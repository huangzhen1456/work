#coding=utf-8
import tornado.web
import tornado.gen
from prj.decorator import *
from prj.sql import SQL
from prj.user.models import *
import urllib.request
import json


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


class ThanksHandler(tornado.web.RequestHandler):
    #感恩节专题
    def get(self):
        items = {

        }
        self.render('../static/templates/thanks.html', items=items)


class Love520Handler(tornado.web.RequestHandler):
    #520求婚专题
    def get(self):
        items = {

        }
        self.render('../static/templates/love520.html', items=items)


class WeiXinYanZhengHandler(tornado.web.RequestHandler):
    #微信验证
    def get(self):
        items = {

        }
        self.render('../static/templates/MP_verify_BZX94GyZpOPmjWqh.txt', items=items)


class WeiXinTokenHandler(tornado.web.RequestHandler):
    #微信获取token
    def post(self):
        code = self.get_argument('code', '')
        url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=wxfb418f3903c83820&secret=8934e7d15453e95707ef794cf7b0159d&code='+code+'&grant_type=authorization_code'
        print(url)
        response = urllib.request.urlopen(url, timeout=500)
        d = response.read().decode('utf-8')
        data = json.loads(d)
        return self.finish(data)


class WeiXinHandler(tornado.web.RequestHandler):
    #微信试验
    def get(self):
        items = {

        }
        self.render('../static/templates/weixin.html', items=items)