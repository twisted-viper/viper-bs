#coding:utf-8
'''
Created on May 24, 2013

@author: HP
'''

from log.viper_log import ViperLogger
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

class ViperBalanceServerProtocol(LineReceiver):
    def __init__(self):
        print type(reactor)
        
    def connectionMade(self):
        print 'connectionMade'
    
    def connectionLost(self, reason):
        print 'connectionLost'
        
    def lineReceived(self, line):
        print line

        
class ViperBalanceServerFactory(Factory):
    def buildProtocol(self, addr):
        return ViperBalanceServerProtocol()

def viperBalanceServerRunning():
    print 'Viper Balance Server Started'

class ViperBalanceServer():
    
    def __init__(self):
        pass
    
    def start(self):
        logger = ViperLogger.getLogger()
        logger.info('Selector Type:' + str(sys.modules['twisted.internet.reactor']))
        reactor.listenTCP(SERVER_PORT, ViperBalanceServerFactory())
        reactor.callWhenRunning(viperBalanceServerRunning)
        reactor.run()
    