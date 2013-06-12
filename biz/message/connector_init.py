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

def connectorInit(protocol, message):
    connectorServer = ConnectorServer(protocol)
    group.addConnectorServer(connectorServer)
    
    connectorServer.setActive(True)
    connectorServer.setName(message['connector']['name'])
    connectorInitMessage = {}
    connectorInitMessage['name'] = 'connector-init'
    connectorServer.sendMessage(json.dumps(connectorInitMessage))
