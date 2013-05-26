'''
Created on 2013-5-26

@author: wolf_m
'''

from biz.ConnectorGroup import ConnectorGroup
from log.viper_log import ViperLogger
import time


logger = ViperLogger.getLogger()
group = ConnectorGroup.getGroup()

def connectorPing(connectorId, message):
    connectorServer = group.getConnectorServer(connectorId)
    connectorServer.setPingTime(time.time())
