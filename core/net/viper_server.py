# coding:utf-8
'''
Created on May 24, 2013

@author: HP
'''


from biz.ConnectorGroup import ConnectorGroup
from core.net.viper_callback import onViperBalanceServerRunning, \
    onConectorConnectionMade, onConectorConnectionLost, onLineReceived
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
        pass
        
    def connectionMade(self):
        onConectorConnectionMade(self)
    
    def connectionLost(self, reason):
        onConectorConnectionLost(self, reason)
        
    def lineReceived(self, line):
        onLineReceived(self,line)

        
class ViperBalanceServerFactory(Factory):
    def buildProtocol(self, addr):
        return ViperBalanceServerProtocol()


class ViperBalanceServer():
    inst = None
    def __init__(self):
        pass
    
    @staticmethod
    def getInstance():
        if not ViperBalanceServer.inst:
            inst = ViperBalanceServer()
        return inst
    
    def getReactor(self):
        return reactor
        
    def start(self):
        group = ConnectorGroup.getGroup()
        logger = ViperLogger.getLogger()
        logger.info('Viper Balance Server selector type:' + str(type(reactor)))
        reactor.listenTCP(SERVER_PORT, ViperBalanceServerFactory())
        reactor.callWhenRunning(onViperBalanceServerRunning)
        reactor.callWhenRunning(group.checkConnectorServerStatus)
        reactor.run()
    
