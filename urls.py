from handlers.foo import FooHandler
from handlers.index import IndexHandler
from handlers.websocket import WebSocketHandler

import tornado.web

url_patterns = [
    (r"/foo", FooHandler),
    (r"/", IndexHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {'path':  './'}),
    (r"/ws", WebSocketHandler)
]
