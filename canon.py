#!/usr/bin/python

import usb.core
import usb.util
import sys
 
# find our device
#idVendor=0x04a9
#idProduct=0x3040

#bRequest Values
GET_STATUS = 0x00
CLEAR_FEATURE = 0x01
SET_FEATURE = 0x03
SET_ADDRESS = 0x05
GET_DESCRIPTOR = 0x06
SET_DESCRIPTOR = 0x07
GET_CONFIGURATION = 0x08
SET_CONFIGURATION = 0x09

dev = usb.core.find(idVendor=0x04a9, idProduct=0x3040)
#for d in dev:
#   print d

# was it found?
if dev is None:
   raise ValueError('Device not found')

# Linux kernel sets up a device driver for USB device, which you have
# to detach. Otherwise trying to interact with the device gives a
# 'Resource Busy' error.
try:
   dev.detach_kernel_driver(0)
except Exception, e:
   pass # already unregistered
 
# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()


# Let's fuzz around! 
 
# Lets start by Reading 1 byte from the Device using different Requests
# bRequest is a byte so there are 255 different values
#req_read = 0xC0 #0b11000000
bmRequestType = 0x80 #0b10000000
wValue = 0
wIndex = 0
wLength = 64
bRequest = GET_STATUS #This is the only thing that resonds. 
for bRequest in range(255):
   try:
      #dev.ctrl_transfer(bmRequestType, bmRequest, wValue, wIndex, msg/bytes)
      ret = dev.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, wLength)
      print "bRequest ",bRequest
      print ret
   except:
      # failed to get data for this request
      pass
 
print "all done"
