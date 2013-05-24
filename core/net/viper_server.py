#coding:utf-8
'''
Created on May 24, 2013

@author: HP
'''

from log.viper_log import ViperLogger
from server import serverFactory
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

def running():
    print 'Server Started'

class ViperBalanceServer():
    
    def __init__(self):
        pass
    
    def start(self):
        logger = ViperLogger.getLogger()
        logger.info('Selector Type:' + str(sys.modules['twisted.internet.reactor']))
        reactor.listenTCP(SERVER_PORT, serverFactory())
        reactor.callWhenRunning(running)
        reactor.run()
    