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
        handler = logging.FileHandler(os.path.join(LOG['path'],'error.log'))
        self.VIPER_LOGGER.addHandler(handler)
        self.VIPER_LOGGER.setLevel(LOG['level'])
    
    def getTimeStame(self):
        now = time.localtime()
        timeStr = time.strftime('%Y-%m-%d %H:%M:%S', now)
        return '[' + timeStr + '] '
  
    def error(self):
        self.VIPER_LOGGER.error(self.getTimeStame() + "ERROR: This is an error message")
        
    def critical(self):
        self.VIPER_LOGGER.critical(self.getTimeStame() + "CRITIAL: This is an critical message")
        
    def warning(self):
        self.VIPER_LOGGER.warning(self.getTimeStame() + "WARNING: This is an warning message")
        
    def debug(self):
        self.VIPER_LOGGER.debug(self.getTimeStame() + "DEBUG: This is an debug message")
    
    def info(self):
        self.VIPER_LOGGER.info(self.getTimeStame() + "INFO: This is an info message")
        
        
    @staticmethod
    def getLogger():
        if not ViperLogger.inst:
            ViperLogger.inst = ViperLogger()
        return ViperLogger.inst
