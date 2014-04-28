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
	encdata = str(sepchar).join(data)
	message = "START" + str(sepchar) + encdata + str(sepchar) + "END"
	return message

print encode_data(["abba"],"")