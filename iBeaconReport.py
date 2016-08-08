from __future__ import division
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
        Adstring += self.timestamp.strftime("%d-%m-%Y %H:%M:%S")
        
        return Adstring

    def abbrToString(self):
        Adstring = "\n MAC Address :: "
        Adstring += self.MACAddress
        Adstring += "\n Accuracy :: "
        Adstring += "%f" % self.accuracy
        Adstring += "\n Timestamp :: "
        Adstring += self.timestamp.strftime("%d-%m-%Y %H:%M:%S")
        return Adstring

    def __cmp__(self, other):
        if hasattr(other, 'Major'):
            return self.Major.__cmp__(other.Major)

    def __repr__(self):
#        return '{} {} {} {}'.format(self.MACAddress, self.Major, self.Minor, self.timestamp)
#        return '{} {} {} {}'.format(self.MACAddress, self.UID, self.Minor, self.timestamp)
        return "['{}', '{}', '{}', '{}', '{}', '{}', '{}']".format(self.MACAddress, self.UID, self.Major, self.Minor, self.TxPower[0], self.measuredPower[0], self.timestamp)

    def setAccuracy( TxPower, MeasuredPower ):  #wymagane podanie zmiennych typu Int
        accuracy = math.pow(12.0, 1.5 * ( (txpower / measuredPower) -1 ))