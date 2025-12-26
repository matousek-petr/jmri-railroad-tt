import jarray
import jmri

class regiospider(base_automated_route):

    address = 9
    sens_start = "IS56"
    running = "IS57"

    def init(self):
        self.throttle = self.getThrottle(self.address, False)
        self.auto = sensors.provideSensor(self.sens_start)
        self.auto_s = sensors.provideSensor(self.running)

        self.rychlost_stanice = 0.35
        self.rychlost_jizda = 0.5
        self.rychlost_koridor = 0.5
        self.smer = False
        self.priority = 1

        self.sobotin_wait = 4400
        
        self.petrov1_zabreh_wait = 3400
        self.petrov2_zabreh_wait = 3700
        self.petrov1_sobotin_wait = 3300
        self.petrov2_sobotin_wait = 3200

        self.petrov_zabreh_wait = 30000

        self.h1wait = 2000
        self.h3wait = 2000        

        self.z5wait = 3000
        self.z3wait = 3000
        self.z5akwait = 2200

        self.zvswait = 8000

        self.zh_a_1 = 3000
        self.zh_a_2 = 3000
        self.zh_a_3 = 3000
        
        self.hz_b_1 = 2000
        self.hz_b_2 = 3000
        self.hz_b_3 = 3000        

        self.pauza = 180000

    def run_route(self):
        self.throttle.setF0(True)
        self.throttle.setF1(True)

        self.zabreh5ak_sobotin_zabreh5ak()

regiospider().start()