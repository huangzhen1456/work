import tornado.web
from prj.views import *

handlers = [
    (r"/", MainHandler),
    (r"/love", LoveHandler),
]




