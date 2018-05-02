#!/usr/bin/python

import usb.core
import usb.util
import sys
 
#Interesting requests
#bmRequestType = 0xC1
#bRequest = 2
#wValue = 0x0000
#wIndex = 0
#wLength = 2

#bRequest  5
#bmRequest  0
#2
#bRequest  5
#bmRequest  0
#64


# find our device
#idVendor=0x04a9
#idProduct=0x3040

#Standard Device Requests
GET_STATUS        = 0x00
CLEAR_FEATURE     = 0x01
SET_FEATURE       = 0x03
SET_ADDRESS       = 0x05
GET_DESCRIPTOR    = 0x06
SET_DESCRIPTOR    = 0x07
GET_CONFIGURATION = 0x08
SET_CONFIGURATION = 0x09

#Standard Interface Requests
GET_INTERFACE     = 0x0A
SET_INTERFACE     = 0x11

#Standard Endpoint Requests
SYNCH_FRAME       = 0x12

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

#print device configurations
#for cfg in dev:
#   print "Configuration:\n"
#   sys.stdout.write(str(cfg.bConfigurationValue) + '\n')
#   for intf in cfg:
#      print "Interface:\n"
#      sys.stdout.write('\t' + \
#         str(intf.bInterfaceNumber) + \
#         ',' + \
#         str(intf.bAlternateSetting) + \
#         '\n')
#      for ep in intf:
#         print "Endpoint:\n"
#         sys.stdout.write('\t\t' + \
#            str(ep.bEndpointAddress) + \
#            '\n')

# Lets start by Reading 1 byte from the Device using different Requests
# bRequest is a byte so there are 255 different values
bmRequestType = 0x00
bRequest = 5
wValue = 0x0000
wIndex = 0
wLength = 64
try:
   ret = dev.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, wLength)
   print ret
except:
   #FAIL!
   pass
#for bRequest in range(255):
#   for bmRequestType in range(255):
#      try:
#         #dev.ctrl_transfer(bmRequestType, bmRequest, wValue, wIndex, msg/bytes)
#         ret = dev.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, wLength)
#         print "bRequest ",bRequest
#         print "bmRequest ", bmRequestType
#         print ret
#      except:
#         # failed to get data for this request
#         pass
 
print "all done"
