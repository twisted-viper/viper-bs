'''
Created on 2013-5-26

@author: wolf_m
'''
from biz.message.client_init import clientInit
from biz.message.connector_init import connectorInit
from biz.message.connector_ping import connectorPing

MESSAGE_ACTION = {
    "connector-init": connectorInit,
    "client-init": clientInit,
    "connector-ping": connectorPing,
}
