import jarray
import jmri

class regiospider2(base_automated_route):

    address = 8
    sens_start = "IS70"
    running = "IS71"

    def __init__(self):
        self.throttle = self.getThrottle(self.address, False)
        self.auto = sensors.provideSensor(self.sens_start)
        self.auto_s = sensors.provideSensor(self.running)

        self.rychlost_stanice = 0.75
        self.rychlost_jizda = 0.9
        self.rychlost_koridor = 0.95
        self.smer = False
        self.priority = 1

        self.sobotin_wait = 3400
        self.s2akwait = 1000
        
        self.petrov1_zabreh_wait = 2300
        self.petrov2_zabreh_wait = 2600
        self.petrov1_sobotin_wait = 2500
        self.petrov2_sobotin_wait = 2200

        self.petrov_zabreh_wait = 20000

        self.zh_a_1 = 3000
        self.zh_a_2 = 3000
        self.zh_a_3 = 3000
        
        self.hz_b_1 = 2000
        self.hz_b_2 = 3000
        self.hz_b_3 = 3000   

        self.h1wait = 2000
        self.h3wait = 2000                     

        self.z5wait = 3000
        self.z5bkwait = 1500

        self.zvswait = 6500

        self.pauza = 120000

    def run_route(self):
        self.throttle.setF0(True)
        self.throttle.setF1(True)

        self.zabreh5bk_sobotin_zabreh5bk()

regiospider2().start()