import tornado.web
from prj.views import *

handlers = [
    (r"/", MainHandler),
    (r"/news", NewsHandler),
    (r"/love", LoveHandler),
]




