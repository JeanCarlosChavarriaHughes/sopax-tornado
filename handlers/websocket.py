from handlers.base import BaseHandler
import tornado.websocket
import multiprocessing
import json

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class WebSocketHandler(tornado.websocket.WebSocketHandler, BaseHandler):
    def __init__(self, clients=[], input_queue=multiprocessing.Queue(), output_queue=multiprocessing.Queue()):
        self._clients = clients 
        self.input_queue = input_queue
        self.output_queue = output_queue
    
    @property
    def clients(self):
        return self._clients

    @property
    def input_queue(self):
        return self._input_queue

    @property
    def output_queue(self):
        return self._output_queue


    def open(self):
        print ('new connection')
        self.clients.append(self)
        self.write_message("connected")
 
    def on_message(self, message):
        print ('tornado received from client: %s' % json.dumps(message))
        #self.write_message('ack')
        self.input_queue.put(message)
 
    def on_close(self):
        print ('connection closed')
        self.clients.remove(self)

    ## check the queue for pending messages, and rely that to all connected clients
    def checkQueue(self):
        if not self.output_queue.empty():
            message = self.output_queue.get()
            for c in self.clients:
                c.write_message(message)