'''
Created on 2013-5-26

@author: wolf_m
'''
from biz.ConnectorGroup import ConnectorGroup
from biz.ConnectorServer import ConnectorServer
from biz.MessageFactory import MESSAGE_ACTION
from biz.ProtocolGroup import ProtocolGroup
from log.viper_log import ViperLogger
import json


logger = ViperLogger.getLogger()
group = ConnectorGroup.getGroup()
    
    
def onViperBalanceServerRunning():
    logger.debug('Viper Balance Server Started')
    
def onConectorConnectionMade(protocol): 
    logger.debug('Connection made ' + str(protocol.transport.getPeer()))
    ProtocolGroup.getInstance().addProtocol(protocol)

def onConectorConnectionLost(protocol, reason):
    connectorId = str(protocol.transport.getPeer())
    group.delConnectorServer(connectorId)
    ProtocolGroup.getInstance().removeProtocol(protocol)
    logger.debug('Connector connection lost ' + connectorId)
    
def onLineReceived(protocol, line):
    logger.debug('Message Received ' + line)
    message = json.loads(line)
    messageParse = MESSAGE_ACTION.get(message['name'])
    if messageParse == None:
        logger.error('Unrecognized message received ' + message['name'])
        protocol.transport.loseConnection()
    else:
        messageParse(protocol, message)
    
