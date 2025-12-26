import jarray
import jmri

class hektor(base_automated_route):

    address = 13
    sens_start = "IS68"
    running = "IS69"

    def __init__(self):
        self.throttle = self.getThrottle(self.address, False)
        self.auto = sensors.provideSensor(self.sens_start)
        self.auto_s = sensors.provideSensor(self.running)

        self.rychlost_stanice = 0.5
        self.rychlost_jizda = 0.6
        self.rychlost_koridor = 0.6
        self.priority = 1

        self.smer = False

        self.zh_b_1 = 4000
        self.zh_b_2 = 4000
        self.zh_b_3 = 4000
        
        self.hz_a_1 = 4000
        self.hz_a_2 = 4000
        self.hz_a_3 = 4000

        self.h4wait = 8000
        self.z1wait = 9000
        self.z2wait = 6000
        self.z3wait = 6000
        self.z4wait = 8000
        self.z5wait = 9000

    def run_route(self):
        self.throttle.setF0(True)

        self.hostejn_4_odj_a()
        self.autoblock_hz_a()
        self.zabreh_smer_a_1324()
        self.autoblock_zh_b()
        self.hostejn_4_vj_b()

hektor().start()