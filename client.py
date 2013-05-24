'''
Created on May 20, 2013

@author: HP
'''
from sys import stdout
from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.protocol import Factory, Protocol, ClientFactory


class EchoProtocol(Protocol):
    def connectionLost(self,reason):
        print reason
    
    def dataReceived(self, data):
        print data


class EchoClientFactory(ClientFactory):
    protocol = EchoProtocol
    def startedConnecting(self, connector):
        print 'Started to connect.'

    def buildProtocol(self, addr):
        print 'Connected.'
        proto = ClientFactory.buildProtocol(self, addr)
        return proto

    def clientConnectionLost(self, connector, reason):
        print 'Lost connection.  Reason:', reason

    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed. Reason:', reason

def gotProtocol(p):
    p.sendMessage("Hello")
    reactor.callLater(1, p.sendMessage, "This is sent in a second")
    reactor.callLater(2, p.transport.loseConnection)

def calling():
    print 'started'

reactor.connectTCP('localhost', 8002, EchoClientFactory())
reactor.callWhenRunning(calling)
reactor.run()