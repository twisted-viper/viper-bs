'''
Created on 2013-5-26

@author: wolf_m
'''
from biz.ConnectorGroup import ConnectorGroup
from log.viper_log import ViperLogger

logger = ViperLogger.getLogger()
group = ConnectorGroup.getGroup()

def clientInit(connectorId, message):
    pass