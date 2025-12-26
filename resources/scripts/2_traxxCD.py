import jarray
import jmri

class traxx(base_automated_route):

    address = 2
    sens_start = "IS62"
    running = "IS63"

    def init(self):
        self.throttle = self.getThrottle(self.address, False)
        self.auto = sensors.provideSensor(self.sens_start)
        self.auto_s = sensors.provideSensor(self.running)

        self.rychlost_stanice = 0.4
        self.rychlost_jizda = 0.55
        self.rychlost_koridor = 0.6

        self.smer = True
        self.priority = 1

        self.zh_b_1 = 7500
        self.zh_b_2 = 7500
        self.zh_b_3 = 7500
        
        self.hz_a_1 = 7500
        self.hz_a_2 = 7500
        self.hz_a_3 = 7000

        self.h2wait = 8700
        self.h4wait = 9700
        self.z2wait = 9100

    def run_route(self):
        self.throttle.setF0(True)

        self.zabreh_2_odj_b()
        self.autoblock_zh_b()
        self.hostejn_smer_b()
        self.autoblock_hz_a()
        self.zabreh_2_vj_a()

traxx().start()