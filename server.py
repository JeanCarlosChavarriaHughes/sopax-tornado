#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.gen
from tornado.options import define, options
import os
import time
import serialworker

from settings import settings
from urls import url_patterns
from handlers.websocket import WebSocketHandler


# define("port", default=8888, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('/templates/index.html')

class StaticFileHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('media/js/main.js')

class TornadoBoilerplate(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)


if __name__ == '__main__':
    ## start the serial worker in background (as a deamon)
    main_web_socket = WebSocketHandler
    sp = serialworker.SerialProcess(main_web_socket.input_queue, main_web_socket.output_queue)
    sp.daemon = True
    sp.start()

    # Start Web Application
    tornado.options.parse_command_line()
    app = TornadoBoilerplate()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

    """
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/static/(.*)", tornado.web.StaticFileHandler, {'path':  './'}),
            (r"/ws", WebSocketHandler)
        ]
    )
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(options.port)
    """
    print ("Listening on port:", options.port)

    mainLoop = tornado.ioloop.IOLoop.instance()
    ## adjust the scheduler_interval according to the frames sent by the serial port
    scheduler_interval = 100
    scheduler = tornado.ioloop.PeriodicCallback(main_web_socket.checkQueue, scheduler_interval, io_loop = mainLoop)
    scheduler.start()
    mainLoop.start()