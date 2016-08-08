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

#budowanie listy kamieni (rozroznianie po MAC adresie)
macAddressSet = set()
for beacon in returnedList:
    macAddressSet.add(beacon.MACAddress)

#usrednianie wartosci parametru measuredPower
for macAddress in macAddressSet:
    measuredPowerSum = 0
    measuredPowerAverage = 0
    iterator = 0
    for beacon in returnedList:
        if beacon.MACAddress == macAddress:
            measuredPowerSum += beacon.measuredPower[0]
            iterator = iterator + 1
    measuredPowerAverage = measuredPowerSum / iterator
    
    #for testing purposes
    print macAddress + "%i" % measuredPowerAverage

blescan.hci_disable_le_scan(sock)
