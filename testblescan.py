# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
from iBeaconReport import iBeaconReport
import bluetooth._bluetooth as bluez
import math
import datetime

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
beaconList = list()

for beacon in returnedList:
    macAddressSet.add(beacon.MACAddress)

beaconReport = iBeaconReport()
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
    
    #output beacon parameters
    beaconReport.MACAddress = macAddress
    beaconReport.UID = beacon.UID
    beaconReport.Major = beacon.Major
    beaconReport.Minor = beacon.Minor
    beaconReport.TxPower = beacon.TxPower
    beaconReport.measuredPower = measuredPowerAverage
    beaconReport.accuracy = math.pow(12.0, 1.5 * ( (beacon.TxPower[0] / measuredPowerAverage) -1 ))
    beaconReport.timestamp = datetime.datetime.now()

    beaconList.append(beaconReport)

    #for testing purposes
    print "MAC address :: " + macAddress + ", measured power sum :: %i" % measuredPowerSum + ", iterator %i" % iterator + ", average measured power :: %i" % measuredPowerAverage

blescan.hci_disable_le_scan(sock)

#for testing purposes
for ibeacon in beaconList:
    print ibeacon.toString()
