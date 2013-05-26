'''
Created on 2013-5-26

@author: wolf_m
'''
from log.viper_log import ViperLogger

logger = ViperLogger.getLogger()
class ConnectorGroup():
    inst = None
    def __init__(self):
        self.connectorDic = {}
        self.connectorSize = 0
    
    def addConnector(self, connector):
        if not self.connectorDic.has_key(connector.getId()):
            self.connectorDic[connector.getId()] = connector
            self.connectorSize = self.connectorSize + 1
    
    def delConnector(self, connectorId):
        if self.connectorDic.has_key(connectorId):
            del self.connectorDic[connectorId]
            self.connectorSize = self.connectorSize - 1
        else:
            logger.error("Delete ungrouped connector!")
    
    def getConnectorSize(self):
        return self.connectorSize
    
    def broadcast(self):
        pass
    
    @staticmethod
    def getGroup():
        if not ConnectorGroup.inst:
            ConnectorGroup.inst = ConnectorGroup()
        return ConnectorGroup.inst
