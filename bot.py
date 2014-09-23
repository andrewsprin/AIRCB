#! /usr/bin/python
"""
Simple IRC Robot
================

Usage
=====

"""


import socket
import random
import ipgetter

###########################################################################
# Variables for the main server
server = "##" 		# CONFIGURE
channel = "#voices"			# CONFIGURE
botnick = "gollum"			# CONFIGURE 
botdesc = "A mindless little guy"	# CONFIGURE
#Funny vars for the main server
worship = False
master = "##"			# CONFIGURE

# Variables for the MetaServer (backup server that gives external IP 
# when prompted
###########################################################################

###########################################################################
#Function Definition
###########################################################################
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

def ip():
  sendmsg(channel, ipgetter.myip())
    
###########################################################################
#Joke Functions
###########################################################################

def jokea(newnick): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :why did frodo cross the road!\n")

def jokea():
  sendmsg(channel, "The chicken was his guide!")

def jokeb(newnick): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :why did gimli cross the road!\n")

def jokeb():
  sendmsg(channel, "He Didn't, He was tossed!")

def joke(newnick): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :tell a joke!\n")

def joke():
  sendmsg(channel, "I don't Really Know Any Good Jokes... Why Dont You Ask Smeagul.")

###########################################################################
#Begin the fun (Entry Point)
###########################################################################

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
  if ircmsg.find(":tell a joke "+ botnick) != -1:
    joke()
  if ircmsg.find(":why did frodo cross the road "+ botnick) != -1:
    jokea()
  if ircmsg.find(":why did gimli cross the road "+ botnick) != -1:
    jokeb()
  if ircmsg.find("PING :") != -1:
	ping()
  if ircmsg.find(botnick + ": roll") != -1:
	roll()
  if ircmsg.find(botnick + ": ip") != -1:
	ip()


