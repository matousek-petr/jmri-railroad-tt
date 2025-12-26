import jarray
import jmri

class cd_842(base_automated_route):

    address = 5
    sens_start = "IS66"
    running = "IS67"

    def __init__(self):
        self.throttle = self.getThrottle(self.address, False)
        self.auto = sensors.provideSensor(self.sens_start)
        self.auto_s = sensors.provideSensor(self.running)

        self.rychlost_stanice = 0.4
        self.rychlost_jizda = 0.6
        self.rychlost_koridor = 0.7

        self.smer = False 
        self.priority = 1

        self.zh_b_1 = 7000
        self.zh_b_2 = 7000
        self.zh_b_3 = 7000
        
        self.hz_a_1 = 7000
        self.hz_a_2 = 7000
        self.hz_a_3 = 7000

        self.z1wait = 8000
        self.z2wait = 8000
        self.z3wait = 8000
        self.z4wait = 7000
        self.z5wait = 6500
        self.z5bkwait = 2100

        self.h1wait = 1500
        self.h2wait = 6500
        self.h4wait = 7000

    def run_route(self):
        self.throttle.setF0(True)

        self.hostejn_2_odj_a()
        self.autoblock_hz_a()
        self.zabreh_smer_a_13524()
        self.autoblock_zh_b()
        self.hostejn_2_vj_b()

cd_842().start()