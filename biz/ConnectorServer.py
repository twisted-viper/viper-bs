'''
Created on 2013-5-26

@author: wolf_m
'''
from log.viper_log import ViperLogger
import time

logger = ViperLogger.getLogger()

class ConnectorServer():
    
    def __init__(self, protocol):
        self.protocol = protocol
        self.isActive = False
        self.pingTime = 0;
        
    def sendMessage(self, msg):
        logger.debug('Seng Message ' + msg)
        self.protocol.sendLine(msg)
        
    def setPingTime(self):
        self.pingTime = time.time()
    
    def getPingTime(self):
        return self.pingTime
    
    def getId(self):
        return str(self.protocol.transport.getPeer())
    
    def setActive(self, active):
        self.isActive = active
    
    def closeConnecton(self):
        self.protocol.transport.loseConnection()
        
    def isActive(self):
        return self.isActive
