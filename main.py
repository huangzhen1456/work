import tornado.web
import tornado.httpserver
import tornado.ioloop
from prj.urls import handlers
import os


SITE_ROOT = os.path.dirname(os.path.abspath(__file__))

settings = dict(
    static_path=os.path.join(SITE_ROOT, 'static'),
)

port = 8888

if __name__ == '__main__':

    application = tornado.web.Application(handlers, **settings)
    app = tornado.httpserver.HTTPServer(application)
    app.bind(port)
    app.start(3)
    tornado.ioloop.IOLoop.instance().start()
