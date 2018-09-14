import tornado.web
from prj.views import *

handlers = [
    (r"/", MainHandler),
    (r"/love", LoveHandler),
    (r"/lovebook", LoveBookHandler),
    (r"/danmu", DanMuHandler),
    (r"/thanks", ThanksHandler),
    (r"/love520", Love520Handler),
    (r"/weixin", WeiXinHandler),
    (r"/weixin/token", WeiXinTokenHandler),
    (r"/MP_verify_BZX94GyZpOPmjWqh.txt", WeiXinYanZhengHandler),
]




