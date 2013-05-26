'''
Created on 2013-5-26

@author: wolf_m
'''

class ConnectorServer():
    def __init__(self, protocol):
        self.protocol = protocol
        self.isActive = False
        
    def getId(self):
        return str(self.protocol.transport.getPeer())
    
    def setActive(self, active):
        self.isActive = active
    
    def closeConnecton(self):
        self.protocol.transport.loseConnection()
        
    def isActive(self):
        return self.isActive
