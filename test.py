from __future__ import division
# Standalone script for ranging iBeacons with Raspberry Pi 3
# Karol.Malyszko@torneo.eu 8/8/2016

import BLEScanner
import sys
from iBeaconReport import iBeaconReport
import bluetooth._bluetooth as bluez
import math
import datetime

# Initialize the device
dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
except:
	print "Error accessing bluetooth device. Aborting."
        sys.exit(1)

# Set scan parameters and enable scan mode
BLEScanner.hci_le_set_scan_parameters(sock)
BLEScanner.hci_enable_le_scan(sock)

# Initiate one scan -> gather 100 advertisement reports from iBeacons in range
returnedList = BLEScanner.parse_events(sock)

macAddressSet = set()
beaconList = list()

# Build set of distinct iBeacons -> select by MAC address; Assume each iBeacon has distinct MAC address; if not, use third-party software to set different MAC addresses for each one
for beacon in returnedList:
    macAddressSet.add(beacon.MACAddress)

# Calculate average 'measuredPower' from multiple reports for each iBeacon
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
    beaconReport = iBeaconReport()
    beaconReport.MACAddress = macAddress
    beaconReport.UID = beacon.UID
    beaconReport.Major = beacon.Major
    beaconReport.Minor = beacon.Minor
    beaconReport.TxPower = beacon.TxPower[0]
    beaconReport.measuredPower = measuredPowerAverage
    beaconReport.setDistanceFriis()
#    beaconReport.setDistanceFSPL()
    beaconReport.timestamp = datetime.datetime.now()

    beaconList.append(beaconReport)

# Disable scanner
BLEScanner.hci_disable_le_scan(sock)

# Script completed

# For testing purposes
for ibeacon in beaconList:
    print ibeacon.toString()
