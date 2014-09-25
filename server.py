#! /usr/bin/python
import socket

class IRCServer:
	""" Server Information """

	def __init__(self, serv, chan, nickname, description):
	  self.address = serv
	  self.channel = chan
	  self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	  self.port = 6667
	  self.nick = nickname
	  self.desc = description
	
	def joinchan(self, chan):
	  self.ircsock.send("JOIN " + chan + "\n")
	 
	def login(self):
	  authStr = "USER " + self.nick + " " + self.nick + " " 
	  authStr = authStr +  self.nick + " " + self.desc
	  authStr = authStr + "\n"
	  nickStr = "NICK " + self.nick + "\n"
	  self.ircsock.connect((self.address, self.port))
	  self.ircsock.send(authStr)
	  self.ircsock.send(nickStr)
	  self.joinchan(self.channel)

	def sendmsg(self, chan, msg):
	  self.ircsock.send("PRIVMSG " + chan + " :"+ msg + "\n") 

	def getMsg(self):
	  ircmsg = self.ircsock.recv(2048)
	  ircmsg = ircmsg.strip('\n\r')
	  print(ircmsg)
	  return ircmsg

	def ping(self):
	  self.ircsock.send("PONG :Pong\n")
	  print("PONG :Pong\n")


