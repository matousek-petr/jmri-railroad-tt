import jarray
import jmri

class arriva(base_automated_route):

    address = 14
    sens_start = "IS52"
    running = "IS53"

    def init(self):
        self.throttle = self.getThrottle(self.address, False)
        self.auto = sensors.provideSensor(self.sens_start)
        self.auto_s = sensors.provideSensor(self.running)

        self.rychlost_stanice = 0.3
        self.rychlost_jizda = 0.4
        self.rychlost_koridor = 0.45
        self.smer = True
        self.priority = 1

        self.s1wait = 2600
        self.h1wait = 4000
        self.h3wait = 4000

        self.p1waitz = 2500
        self.p2waitz = 2700
        self.p1waits = 2800
        self.p2waits = 2800

        self.z5wait = 2600
        self.z3wait = 3400
        self.z4wait = 5000
        self.z4wait_k = 7000
        self.z4kwait = 2500

        self.zh_a_1 = 6000
        self.zh_a_2 = 6000
        self.zh_a_3 = 6000
        
        self.hz_b_1 = 6000
        self.hz_b_2 = 6000
        self.hz_b_3 = 6000

        self.zvswait = 6000

        self.pauza = 0       

    def run_route(self):
        self.throttle.setF0(True)
        self.throttle.setF1(True)
        self.throttle.setF3(True)
        self.throttle.setF5(True)
        self.throttle.setF6(True)
        
        self.zabreh_4k_odj()
        self.zabreh_4_odj_a()
        self.autoblock_zh_a()
        self.hostejn_smer_a_31()
        self.autoblock_hz_b()
        self.zabreh_4_vj_b()
        self.zabreh_4k_vj()

arriva().start()