# coding: utf-8
import os
import sys
from twisted.internet import protocol, reactor, endpoints
import re
from twisted.internet.defer  import  Deferred
from twisted.python.failure  import  Failure

sysStat = 0

class Echo(protocol.Protocol):
	def __init__(self, factory):
		self.factory = factory
		self.clientHost = "127.0.0.1"
		self.clientPort = 0

	def connectionMade(self):
		self.clientHost = self.transport.getPeer().host
		self.clientPort = self.transport.getPeer().port
		self.factory.addClient()
		self.transport.write(
			b"Welcome %s:%d ! There are currently %d open connections.\r\n" %
			(str.encode(self.clientHost),self.clientPort,self.factory.getClientCount(),))

	def connectionLost(self, reason):
		self.factory.removeClient()

	def dataReceived(self, data):
		global sysStat
		print(data,'-->',type(data))

		rcvStr= re.sub(r"\r\n|\n","",str(data, encoding = "utf-8",errors = 'ignore') )
		#bytes to utf-8(str)
		print(rcvStr,'-->',type(rcvStr))
		if len(rcvStr) == 0:
			return


		#utf-8(str) to bytes
		self.transport.write(str.encode(rcvStr))
		self.transport.write(b"-->OK\r\n")

		print('')
		print(rcvStr, '-->', type(rcvStr))
		if rcvStr == 'quit':
			print('program will end.')
			sysStat = 1




class EchoFactory(protocol.Factory):
	def __init__(self):
		self.numProtocols = 0

	def addClient(self):
		self.numProtocols += 1

	def removeClient(self):
		self.numProtocols -= 1

	def getClientCount(self):
		return self.numProtocols

	def buildProtocol(self, addr):
		return Echo(self)

def checkStatus():
	global sysStat
	if sysStat == 1:
		reactor.stop()
	else:
		reactor.callLater(1,checkStatus)


endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
print("start ....")
reactor.callWhenRunning(checkStatus)
reactor.run()
print("stopped!")