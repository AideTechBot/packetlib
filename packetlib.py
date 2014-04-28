"""
packetlib

a dynamic packet library for encoding and parsing data

written by Aidetechbot
"""

#this returns a string of encoded data
#data is the data to encode(in an array)
#sepchar is the character that will seperate the data. 
#It's useful when you can only use certain chars (ex: baudot)
def encode_data(data,sepchar):

	#raise errors when the type is wrong
	if(sepchar == ""):
		raise Exception("Invalid seperation char.")
	if(not type(data) is list):
		raise TypeError("Invalid data type: " + str(type(data)))

	#put the seperators and join everthing together
	encdata = str(sepchar).join(data)
	message = "START" + str(sepchar) + encdata + str(sepchar) + "END"

	#return everything
	return message

	
#this function take a valid string in the format above and decodes it to an array
#sepchar is the same as above
#data is the string
def parse_data(data, sepchar):
	
	#this is the parsed data
	parsed = []
	#raise type errors when the type is wrong
	if(not type(data) is str and not type(sepchar) is str):
		raise TypeError("Invalid data type: " + str(type(data)))

	#check if the beginning is a packet
	y = 6
	if(data[0:y] == "START" + sepchar):
		#if it does start reading the data
		for x in range(6,len(data)):
			try:
				char = data[x]
			except IndexError as e:
				raise IndexError("packet parser passed packet len.")
			if(char == sepchar):
				if(not data[y:x] == ''):
					parsed.append(data[y:x])
				y = x + 1
	return parsed

