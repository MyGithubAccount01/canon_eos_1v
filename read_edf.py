#!/usr/bin/python

#This is a discovery of what the EDF file is
#NOTES: 
#Values are little endian
#most values appear to be hex based integers.


#Roll information
#byte 39 of the first metadata block is the film ID
#byte 46 is hour
#byte 47 is minutes
#byte 48 is seconds
#byte 49 is ???
#byte 50 is frame count
#byte 51
#byte 52
#byte 53
#byte 54-55 is ISO
#byte 56-62 ???
#byte 63 is frames per row -- this might be just application data

#Per frame information
#byte 20:
#byte 21:
#byte 22:
#byte 24: frame number
#byte 32-33: ISO
#byte 34...
#byte 56-57: year
#byte 58: month
#byte 59: day
#byte 60: hour
#byte 61: minutes
#byte 62: seconds
#
import binascii
import struct

BLOCK_SIZE = 512
name = "/mnt/data/canon_eos_1v/FI000000.EFD"
def get_size(edf_file):
   edf_file.seek(0,2)
   size = edf_file.tell()
   #go back to the beginning
   edf_file.seek(0,0)
   return size

edf = open(name, "rb")

block = edf.read(BLOCK_SIZE)
block_array = [] #[block] #bytearray(block)

#print block
while block:
#   for b in block:
#      block_bytes.append(b)
   #print binascii.hexlify(bytearray(block_bytes)
   block_array.append(block)
   block = edf.read(BLOCK_SIZE)
edf.close()

#print binascii.hexlify(bytearray(block_array[0]))
#my_byte = block_array[1]#[25]
#print binascii.hexlify(bytearray(my_byte))

#get the film ID
meta_block = bytearray(block_array[0])
print "film id: ", meta_block[38]

#get the date
#Month - byte 44 
#Day - byte 45
#Year - bytes 42-43
year_bytes = '{:02x}'.format(meta_block[43]) + '{:02x}'.format(meta_block[42])
year = int(year_bytes, 16) 
month = meta_block[44]
day = meta_block[45]
hour = meta_block[46]
minute = meta_block[47]
seconds = meta_block[48]


print "time stamp: ", year, "-", month, "-", day, " ", hour, ":", minute, ":", seconds

for i in range(0, len(block_array)):
   frame_byte = bytearray(block_array[i])
   print frame_byte[24]
   #for j in range(len(block_array[i])):
   #   if 
   #if my_byte == block_array[i][0]
   
