#coding:utf-8
'''
Created on May 24, 2013

@author: HP
'''
from core.net.viper_server import ViperBalanceServer


if __name__ =='__main__' :
    viperBalanceServer = ViperBalanceServer.getInstance()
    viperBalanceServer.start()