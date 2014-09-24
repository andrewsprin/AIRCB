#! /usr/bin/python
# Adds functionality to process input from IRC chat


class inputProcessor:
	def getUserName(delim, string):
		pos = string.index(delim)
		return string[0:pos]

	def getOptions(string):
		#returns a list of strings
		return string.split()

	def runTests():
		isOkay = True;
		isOkay = testGetUserName()

	def testGetUserName():
		isOkay = True
		if(getUserName(":", "e10byagrue: after") != "e10byagrue"):
			isOkay = False
		return isOkay

	def lookFor(query, string):
		options = string.split()
		for s in options:
			if s.find(query) != -1:
				return s

