'''
Created on 2013-5-26

@author: wolf_m
'''
from biz.ConnectorGroup import ConnectorGroup
from log.viper_log import ViperLogger


logger = ViperLogger.getLogger()
group = ConnectorGroup.getGroup()

def connectorInit(connectorId, message):
    connectorServer = group.getConnectorServer(connectorId)
    connectorServer.setActive(True)
    print group.getConnectorServerSize()