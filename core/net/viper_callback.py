'''
Created on 2013-5-26

@author: wolf_m
'''
from biz.ConnectorGroup import ConnectorGroup
from biz.ConnectorServer import ConnectorServer
from log.viper_log import ViperLogger
import json


logger = ViperLogger.getLogger()
group = ConnectorGroup.getGroup()

def onViperBalanceServerRunning():
    logger.debug('Viper Balance Server Started')
    
def onConectorConnectionMade(protocol): 
    connectorServer = ConnectorServer(protocol)
    group.addConnector(connectorServer)
    logger.debug('Conector connection made ' + connectorServer.getId())

def onConectorConnectionLost(protocol,reason):
    connectorId = str(protocol.transport.getPeer())
    group.delConnector(connectorId)
    logger.debug('Conector connection lost ' + connectorId)
    
def onLineReceived(protocol, line):
    logger.debug(line)
    message = json.loads(line)
    
