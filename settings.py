#coding:utf-8
'''
Created on May 24, 2013

@author: HP
'''
import logging
import os

SERVER_PORT = 55024
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

LOG = {
       'path':os.path.join(SITE_ROOT, 'log'),
       'level':logging.NOTSET
}


