'''
Created on 2013-5-26

@author: wolf_m
'''

from log.viper_log import ViperLogger
from twisted.internet import reactor
import time

CHECK_CONNECTOR_SERVER_INTERVAL = 60 * 5
logger = ViperLogger.getLogger()

class ConnectorGroup():
    inst = None
    def __init__(self):
        self.connectorDic = {}
        self.connectorSize = 0
    
    def addConnectorServer(self, connector):
        if not self.connectorDic.has_key(connector.getId()):
            self.connectorDic[connector.getId()] = connector
            self.connectorSize = self.connectorSize + 1
        
    def getConnectorServer(self, connectorServerId):
        if self.connectorDic.has_key(connectorServerId):
            return self.connectorDic[connectorServerId]
        return None
    
    def delConnectorServer(self, connectorId):
        if self.connectorDic.has_key(connectorId):
            del self.connectorDic[connectorId]
            self.connectorSize = self.connectorSize - 1
        else:
            logger.error("Delete ungrouped connector!")
    
    def getConnectorServerSize(self):
        return self.connectorSize
    
    def broadcast(self):
        pass
    
    def checkConnectorServerStatus(self):
        logger.debug('Check Connector server status...')
        for key in self.connectorDic:
            connectorServer = self.connectorDic[key]
            nowTime = time.time()
            if not connectorServer.isActive or nowTime - connectorServer.getPingTime() > CHECK_CONNECTOR_SERVER_INTERVAL:
                connectorServer.closeConnecton()
                
        reactor.callLater(CHECK_CONNECTOR_SERVER_INTERVAL, self.checkConnectorServerStatus)
        
    
    @staticmethod
    def getGroup():
        if not ConnectorGroup.inst:
            ConnectorGroup.inst = ConnectorGroup()
        return ConnectorGroup.inst
