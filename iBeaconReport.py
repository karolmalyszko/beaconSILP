import math
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

    def __repr__(self):     # for testing purposes for easier debugging
        return "{}, {}, {}, {}, {}, {}, {}".format(self.MACAddress, self.UID, self.Major, self.Minor, self.TxPower[0], self.measuredPower[0], self.timestamp)

    def setDistanceFriis(self):
        self.accuracy =  math.pow(2, (self.TxPower - self.measuredPower) / 6 )

    def setDistanceFSPL(self):
        # Free-space path loss method
        K = -27.55 # constant dependant of distance unit -> 32.44 if distance in [km], -27.55 if distance in [m]
        Ptx = -15 # transmitter power; between -30dBm and +4dBm; unknown at the moment
        Prx = self.measuredPower # receiver sensitivity
        CLtx = 0 # transmitter cable loss; 0 if no cables
        CLrx = 0 # receiver cable loss; 0 if no cables
        AGtx = 0 # transmitter antenna gain; assume 0
        AGrx = 0 # receiver antenna gain; assume 0
        FM = 22 # fade margin; assume 22 for no obstacles between transmitter and receiver
        f = 2400 # signal frequency -> 2.4 GHz for bluetooth; has to be in MHz, so assume 2400

        FSPL = Ptx - CLtx + AGrx + AGtx - CLrx - Prx - FM # free-space path loss value
        self.accuracy = math.pow( 10, (FSPL - K - (20*math.log10(f)) ) / 20 )