#coding:utf-8
'''
Created on 2013-5-26

@author: wolf_m
'''
from biz.ConnectorGroup import ConnectorGroup
from log.viper_log import ViperLogger
import json

logger = ViperLogger.getLogger()
group = ConnectorGroup.getGroup()

def clientInit(protocol, message):
    msg = {}
    msg['name'] = 'client_init'
    connectorServer = group.getNextAvailableConnector()
    if connectorServer == None:
        msg['msg'] = '停机维护中...'
        msg['result'] = False
    else:
        msg['result'] = True
        msg['ip']  = connectorServer.getIP();
    protocol.sendLine(json.dumps(msg))
    protocol.transport.loseConnection()
