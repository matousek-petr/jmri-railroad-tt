import jarray
import jmri

class regiojet_vectron(dcc_automated_routes) :
   
    def init(self):

        self.rychlost_stanice = 0.5
        self.rychlost_jizda = 0.65
        self.rychlost_koridor = 0.65

        self.smer = True
        self.priority = 1

        self.zh_b_1 = 2000
        self.zh_b_2 = 2000
        self.zh_b_3 = 2000
        
        self.hz_a_1 = 2000
        self.hz_a_2 = 2000
        self.hz_a_3 = 2000

        self.h2wait = 5000
        self.h4wait = 5500
        self.z4wait = 6500
        self.z5wait = 4500
    
        self.adresa = 15
        self.sensor_1 = "IS72"
        self.sensor_2 = "IS73"
        
        self.throttle = self.getThrottle(self.adresa, False)
        
        self.auto = sensors.provideSensor(self.sensor_1)
        self.auto_s = sensors.provideSensor(self.sensor_2)
        
        return

    def handle(self):
      
        if (self.auto_s.getKnownState() == ACTIVE):
            return 0
            
        else:
            self.auto_s.setKnownState(ACTIVE)

            self.throttle.setF0(True)
            self.throttle.setF1(True)
            self.throttle.setF3(True)
            self.throttle.setF5(True)
            self.throttle.setF6(True)

            self.zabreh_5_odj_b()
            self.autoblock_zh_b()
            self.hostejn_smer_b()
            self.autoblock_hz_a()
            self.zabreh_5_vj_a()
            self.auto_s.setKnownState(INACTIVE)
        
            if (self.auto.getKnownState() == ACTIVE):
                return 1
            else:
                return 0

regiojet_vectron().start()


