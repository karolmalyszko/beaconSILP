# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
from iBeaconReport import iBeaconReport
import bluetooth._bluetooth as bluez

def getKey(item):
    return item[2]

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	#print "ble thread started"

except:
	print "error accessing bluetooth device..."
        sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

#while True:
returnedList = blescan.parse_events(sock)

#oryginalna lista wyników
for beacon in returnedList:
	print beacon.abbrToString()

#sortowanie wyników po major i minor
sortedReturnedList = sorted(returnedList, key=getKey)
for beacon in sortedReturnedList:
	print beacon.abbrToString()

blescan.hci_disable_le_scan(sock)
#print "Test completed"