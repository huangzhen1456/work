import tornado.web
import tornado.httpserver
import tornado.ioloop
import os
from prj.urls import handlers

SITE_ROOT = os.path.dirname(os.path.abspath(__file__))

settings = dict(
    static_path=os.path.join(SITE_ROOT, 'static'),
)

port = 8888

if __name__ == '__main__':

    application = tornado.web.Application(handlers, **settings)
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
