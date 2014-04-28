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
	if(sepchar == ""):
		raise Exception("Invalid seperation char.")
	if(not type(data) is list):
		raise TypeError("Invalid data type: " + str(type(data)))
	encdata = str(sepchar).join(data)
	message = "START" + str(sepchar) + encdata + str(sepchar) + "END"
	return message

	
#this function take a valid string in the format above and decodes it to an array
#data is the string
def parse_data(data):
