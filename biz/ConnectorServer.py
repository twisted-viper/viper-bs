'''
Created on 2013-5-26

@author: wolf_m
'''

class ConnectorServer():
    def __init__(self,protocol):
        self.id = str(protocol.transport.getPeer())
        
    def getId(self):
        return self.id
