import optparse
import os
import re
import sys

# Resul Ucar 
# Deep Packet Inspection
# To use: python3 dpi.py -f [wireshark output as a txt file] -s [the site you are trying to find (purdue, wsj, google)]

parser = optparse.OptionParser()

parser.add_option('-f','--file',dest='file',help='packets') # takes user file, should be username and hash of user password seperated by a space
parser.add_option('-s','--search',dest='search',help='search term') # takes user file, should be username and hash of user password seperated by a space

(options, args) = parser.parse_args()

if options.file == None:
    print('./regex.py -f [file]')
    sys.exit()

file = options.file # set first parameter to usersfile

search = options.search

a = open(file) # open a file to read

text = a.read() # read file

regex = re.compile(r'((.*'+search+'.*))',re.VERBOSE) #regex term

final = regex.findall(text)# itireate through to find all matches

z = str(final) #convert list to a string

print("       No. Time           Source                Destination           Protocol Length Info") # Header

length = len(final) #length of list

for i in range(length): #find all matches
	print(z.split(",")[i]) #format the matches found
	print(z.split(",")[i+1]) #format the matches found