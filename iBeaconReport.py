class iBeaconReport:
    """Basic location report, designed to hold data from single iBeacon advertisement event"""


    MACAddress = ''
    UID = ''
    Major = ''
    Minor = ''
    TxPower = ''
    measuredPower = ''
    accuracy = ''
    timestamp = ''

    def toString(self):
        Adstring = "\n MAC Address :: "
        Adstring += self.MACAddress
        Adstring += "\n UID :: "
        Adstring += self.UID
        Adstring += "\n MAJOR :: "
        Adstring += "%i" % self.Major
        Adstring += "\n MINOR :: "
        Adstring += "%i" % self.Minor
        Adstring += "\n TxPower :: "
        Adstring += "%i" % self.TxPower
        Adstring += "\n Measured power (RSSI) :: "
        Adstring += "%i" % self.measuredPower
        Adstring += "\n Accuracy :: "
        Adstring += "%f" % self.accuracy
        Adstring += "\n Timestamp :: "
        Adstring += "%i" % self.timestamp
        
        return Adstring