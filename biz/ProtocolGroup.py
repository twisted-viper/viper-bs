# coding:utf-8
'''
Created on 2013-6-12

@author: wolf_m
'''
from biz.ConnectorGroup import ConnectorGroup
from log.viper_log import ViperLogger
from twisted.internet import reactor

CHECK_CONNECTOR_SERVER_INTERVAL = 30
group = ConnectorGroup.getGroup()
logger = ViperLogger.getLogger()

class ProtocolGroup():
    inst = None
    def __init__(self):
        self.protocolArr = []
    
    def addProtocol(self, protocol):
        self.protocolArr.append(protocol)
    
    def removeProtocol(self,protocol):
        self.protocolArr.remove(protocol)
        
    def checkProtocolStatus(self):
        logger.info('Check Protocol Status...')
        for protocol in self.protocolArr:
            protocolId = str(protocol.transport.getPeer())
            if group.getConnectorServer(protocolId) == None:
                logger.info('Close unused protocol' + protocolId)
                protocol.transport.loseConnection()
        reactor.callLater(CHECK_CONNECTOR_SERVER_INTERVAL, self.checkProtocolStatus)
        
    @staticmethod
    def getInstance():
        if ProtocolGroup.inst == None:
            ProtocolGroup.inst = ProtocolGroup()
        return ProtocolGroup.inst
        
