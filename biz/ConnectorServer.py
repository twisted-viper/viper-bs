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
        self.ip = protocol.transport.getHost().host
        self.isActive = False
        self.pingTime = 0
        self.name = ''
        self.clientCount = 0
        
    def sendMessage(self, msg):
        logger.debug('Seng Message ' + msg)
        self.protocol.sendLine(msg)
        
    def setClientCount(self,count):
        self.clientCount = count
        
    def getClientCount(self):
        return self.clientCount
        
    def setPingTime(self):
        self.pingTime = time.time()
    
    def getPingTime(self):
        return self.pingTime
    
    def getId(self):
        return str(self.protocol.transport.getPeer())
    
    def setActive(self, active):
        self.isActive = active
        
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def getIP(self):
        return self.ip
    
    def closeConnecton(self):
        self.protocol.transport.loseConnection()
        
    def isActive(self):
        return self.isActive
