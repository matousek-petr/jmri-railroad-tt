import jarray
import jmri

class BrejlovecNajbrt(base_automated_route):

    addr = 6
    sens_start = "IS60"
    running = "IS61"

    def __init__(self):
        self.throttle = self.getThrottle(self.addr, False)
        self.auto = sensors.provideSensor(self.sens_start)
        self.auto_s = sensors.provideSensor(self.running)

        self.z1wait = 8500
        self.z2wait = 5500
        self.z3wait = 6400
        self.z4wait = 4500
        self.z5wait = 3500

        self.h1wait = 4000
        self.h3wait = 4600

        self.zh_a_1 = 2000
        self.zh_a_2 = 2000
        self.zh_a_3 = 2000
        
        self.hz_b_1 = 2000
        self.hz_b_2 = 2000
        self.hz_b_3 = 2000

        self.rychlost_stanice = 0.3
        self.rychlost_jizda = 0.6
        self.rychlost_koridor = 0.7

        self.smer = False
        self.priority = 1

    def run_route(self):
        self.throttle.setF0(True)
        self.hostejn_3_odj_b()
        self.autoblock_hz_b()
        self.zabreh_smer_b_24351()
        self.autoblock_zh_a()
        self.hostejn_3_vj_a()


BrejlovecNajbrt().start()
