#! /usr/bin/python
import socket
import random

###############################################################################
# Variables for the main server
server = "irc.freenode.net" 		# CONFIGURE
channel = "#channel"			# CONFIGURE
botnick = "gollum"			# CONFIGURE 
botdesc = "A mindless little guy"	# CONFIGURE
#Funny vars for the main server
worship = False
master = "yournick"			# CONFIGURE

# Variables for the MetaServer (backup server that gives external IP 
# When prompted
#
###############################################################################

###############################################################################
#Function Definition
###############################################################################

def ping():
  #Essential Fn Responds to server pings
  ircsock.send("PONG :Pong\n")  

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): # This function is used to join channels.
  ircsock.send("JOIN "+ chan +"\n")

def hello(newnick): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")

def hello():
  sendmsg(channel, "Hello")

def roll():
  # TODO make it roll a number here
  sendmsg(channel, str(random.randint(1, 20)))

###############################################################################
#Begin the fun (Entry Point)
###############################################################################

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Standard Port Number
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick + botdesc + "\n") # user authentication
ircsock.send("NICK "+ botnick +"\n") # Give the bot the name
joinchan(channel)

while 1:
  ircmsg = ircsock.recv(2048) # receive data from the server
  ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
  print(ircmsg) # Here we print what's coming from the server

  if ircmsg.find(":Hello "+ botnick) != -1:
    hello()
  if ircmsg.find("PING :") != -1: #Need to respond for some things
    ping()
  if ircmsg.find(":" + master) != -1:
	if worship:
		sendmsg(channel, "and so it was written.")
  if ircmsg.find(botnick + ": worship") != -1:
	worship = not worship
  if ircmsg.find(botnick + ": master") != -1:
	#TODO Fix this
	print("Should be switching master here, but this is broken")
  if ircmsg.find(botnick + ": roll") != -1:
	roll()


