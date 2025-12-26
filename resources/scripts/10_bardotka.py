import jarray
import jmri

class bardotka(base_automated_route):

    address = 10
    sens_start = "IS64"
    running = "IS65"

    def __init__(self):
        self.throttle = self.getThrottle(self.address, False)
        self.auto = sensors.provideSensor(self.sens_start)
        self.auto_s = sensors.provideSensor(self.running)

        self.rychlost_stanice = 0.3
        self.rychlost_jizda = 0.4
        self.rychlost_koridor = 0.45
        self.smer = True 
        self.priority = 1

        self.zh_a_1 = 4000
        self.zh_a_2 = 4000
        self.zh_a_3 = 4000
        
        self.hz_b_1 = 4000
        self.hz_b_2 = 4000
        self.hz_b_3 = 4000

        self.h3wait = 4600
        self.z1wait = 8500
        self.z2wait = 5500        
        self.z3wait = 6000
        self.z4wait = 4500         
        self.z5wait = 3500

    def run_route(self):
        self.throttle.setF0(True)
        
        self.hostejn_3_odj_b()
        self.autoblock_hz_b()
        self.zabreh_smer_b_24351()
        self.autoblock_zh_a()
        self.hostejn_3_vj_a()

bardotka().start()