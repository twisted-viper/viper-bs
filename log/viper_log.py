'''
Created on May 24, 2013

@author: HP
'''

from settings import LOG
import datetime
import logging
import os
import time

class ViperLogger():
    inst = None
    
    def __init__(self):
        self.VIPER_LOGGER = logging.getLogger()
        handler = logging.FileHandler(os.path.join(LOG['path'], 'error.log'))
        self.VIPER_LOGGER.addHandler(handler)
        self.VIPER_LOGGER.setLevel(LOG['level'])
    
    def getTimeStame(self):
        now = time.localtime()
        timeStr = time.strftime('%Y-%m-%d %H:%M:%S', now)
        return '[' + timeStr + '] '
  
    def error(self, msg):
        outputMsg = self.getTimeStame() + "ERROR: " + msg
        print outputMsg
        self.VIPER_LOGGER.error(outputMsg)
        
    def critical(self, msg):
        outputMsg = self.getTimeStame() + "CRITIAL: " + msg
        print outputMsg
        self.VIPER_LOGGER.critical(outputMsg)
        
    def warning(self, msg):
        outputMsg = self.getTimeStame() + "WARNING: " + msg
        print outputMsg
        self.VIPER_LOGGER.warning(outputMsg)
        
    def debug(self, msg):
        outputMsg = self.getTimeStame() + "DEBUG: " + msg
        print outputMsg
        self.VIPER_LOGGER.debug(outputMsg)
    
    def info(self, msg):
        outputMsg = self.getTimeStame() + "INFO: " + msg
        print outputMsg
        self.VIPER_LOGGER.info(outputMsg)
        
        
    @staticmethod
    def getLogger():
        if not ViperLogger.inst:
            ViperLogger.inst = ViperLogger()
        return ViperLogger.inst
