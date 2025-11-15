import jarray
import jmri

class brejlovec_najbrt(dcc_automated_routes) :
   
    def init(self):

        self.rychlost_stanice = 0.1
        self.rychlost_jizda = 0.2
        self.rychlost_koridor = 0.25

        self.adresa = 17
        self.sensor_1 = "IS60"
        self.sensor_2 = "IS61"
        
        self.smer = False #True - neotočený, False - otočený
        self.priority = 1

        self.zh_a_1 = 5000
        self.zh_a_2 = 5000
        self.zh_a_3 = 5000
        
        self.hz_b_1 = 3000
        self.hz_b_2 = 3000
        self.hz_b_3 = 3000

        self.h1wait = 4000
        self.z3wait = 6400
        
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

            self.zabreh_3_odj_a()
            self.autoblock_zh_a()
            self.hostejn_1_pjz_a()
            self.autoblock_hz_b()
            self.zabreh_3_vj_b()
            
            self.auto_s.setKnownState(INACTIVE)
        
            if (self.auto.getKnownState() == ACTIVE):
                return 1
            else:
                return 0   

brejlovec_najbrt().start()

