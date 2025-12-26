import jarray
import jmri

class regiojet_vectron(base_automated_route):

    address = 7
    sens_start = "IS58"
    running = "IS59"

    def init(self):
        self.throttle = self.getThrottle(self.address, False)
        self.auto = sensors.provideSensor(self.sens_start)
        self.auto_s = sensors.provideSensor(self.running)

        self.rychlost_stanice = 0.25
        self.rychlost_jizda = 0.3
        self.rychlost_koridor = 0.35

        self.smer = True
        self.priority = 1

        self.zh_b_1 = 2000
        self.zh_b_2 = 2000
        self.zh_b_3 = 2000
        
        self.hz_a_1 = 2000
        self.hz_a_2 = 2000
        self.hz_a_3 = 2000

        self.h2wait = 2000
        self.h4wait = 2500
        self.z4wait = 4500
        self.z2wait = 4500
        self.z5wait = 2000

    def run_route(self):
        self.throttle.setF0(True)

        self.zabreh_2_odj_b()
        self.autoblock_zh_b()
        self.hostejn_smer_b()
        self.autoblock_hz_a()
        self.zabreh_2_vj_a()

regiojet_vectron().start()