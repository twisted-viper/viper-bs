#coding:utf-8
from settings import SERVER_PORT
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
import sys

try:
    from twisted.internet import epollreactor
    epollreactor.install()
except:
    pass


class serverProtocol(LineReceiver):
    def __init__(self):
        print type(reactor)
        
class serverFactory(Factory):
    def buildProtocol(self, addr):
        return serverProtocol()
    
if __name__ == '__main__':
    print sys.modules['twisted.internet.reactor']
    reactor.listenTCP(SERVER_PORT, serverFactory())
    reactor.run()