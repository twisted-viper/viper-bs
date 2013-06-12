# encoding: utf-8
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
    
    def addConnectorServer(self, connector):
        if not self.connectorDic.has_key(connector.getId()):
            self.connectorDic[connector.getId()] = connector
      
    def getConnectorServer(self, connectorServerId):
        if self.connectorDic.has_key(connectorServerId):
            return self.connectorDic[connectorServerId]
        return None
    
    def delConnectorServer(self, connectorId):
        if self.connectorDic.has_key(connectorId):
            del self.connectorDic[connectorId]
        else:
            logger.error("Delete ungrouped connector!")
    
    def getConnectorServerSize(self):
        return len(self.connectorDic.keys())
    
    def getNextAvailableConnector(self):
        '''
                    根据负载获取最合适的connector server
        '''
        minClientCount = 0
        connector = None
        for key in self.connectorDic.keys():
            if connector == None:
                connector = self.connectorDic[key]
                minClientCount = connector.getClientCount()
                
            tempCount = connector.getClientCount()  
            if minClientCount > tempCount:
                minClientCount = tempCount
                connector = self.connectorDic[key]
        return connector
    
    def broadcast(self):
        pass
    
    def checkConnectorServerStatus(self):
        logger.debug('Check Connector server status...')
        for key in self.connectorDic:
            connectorServer = self.connectorDic[key]
            nowTime = time.time()
            if not connectorServer.isActive or nowTime - connectorServer.getPingTime() > CHECK_CONNECTOR_SERVER_INTERVAL:
                logger.debug('Kill no response connector server:' + connectorServer.getName())
                connectorServer.closeConnecton()
                
        reactor.callLater(CHECK_CONNECTOR_SERVER_INTERVAL, self.checkConnectorServerStatus)
        
    
    @staticmethod
    def getGroup():
        if not ConnectorGroup.inst:
            ConnectorGroup.inst = ConnectorGroup()
        return ConnectorGroup.inst
