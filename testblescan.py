# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
from iBeaconReport import iBeaconReport
import bluetooth._bluetooth as bluez

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	#print "ble thread started"

except:
	print "error accessing bluetooth device..."
        sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

#uruchomienie skanera; jeden cykl, zebranie 100 advertising reports
returnedList = blescan.parse_events(sock)

#print len(returnedList)

#oryginalna lista wynikow
#for beacon in returnedList:
#	print beacon.abbrToString()
#	print beacon.toString()
#	print beacon

#print "after sort"

#sortowanie wynikow po major i minor
sortedReturnedList = sorted(returnedList)
for beacon in sortedReturnedList:
#	print beacon.toString()
#	print beacon.abbrToString()
	print beacon

#distinct Major list
#lista = set(sortedReturnedList[2])
#print lista

blescan.hci_disable_le_scan(sock)
#print "Test completed"