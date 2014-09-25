#! /usr/bin/python
import random
import ipgetter
from server import IRCServer

#make the server
svr = IRCServer("server", "#channel", "botNick", "myPrecious")
svr.login()

while 1:
  msg = ""
  msg = svr.getMsg()
  if msg.find("PING :") != -1:
    print("Should see a ping soon...\n")
    svr.ping()
