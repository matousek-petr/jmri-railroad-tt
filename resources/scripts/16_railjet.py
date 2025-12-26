import jarray
import jmri

class railjet(base_automated_route):

    address = 16
    sens_start = "IS74"
    running = "IS75"

    def __init__(self):
        self.throttle = self.getThrottle(self.address, False)
        self.auto = sensors.provideSensor(self.sens_start)
        self.auto_s = sensors.provideSensor(self.running)

        self.rychlost_stanice = 0.4
        self.rychlost_jizda = 0.5
        self.rychlost_koridor = 0.55

        self.smer = True
        self.priority = 1

        self.zh_b_1 = 2000
        self.zh_b_2 = 2000
        self.zh_b_3 = 2000
        
        self.hz_a_1 = 2000
        self.hz_a_2 = 2000
        self.hz_a_3 = 2000

        self.h2wait = 7000
        self.h4wait = 9500
        self.z4wait = 8500

    def run_route(self):
        self.throttle.setF0(True)

        self.zabreh_4_odj_b()
        self.autoblock_zh_b()
        self.hostejn_smer_b()
        self.autoblock_hz_a()
        self.zabreh_4_vj_a()

railjet().start()