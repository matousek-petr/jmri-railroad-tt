import jarray
import jmri

class regiojet(base_automated_route):

    address = 1
    sens_start = "IS54"
    running = "IS55"

    def init(self):
        self.throttle = self.getThrottle(self.address, False)
        self.auto = sensors.provideSensor(self.sens_start)
        self.auto_s = sensors.provideSensor(self.running)

        self.rychlost_stanice = 0.6
        self.rychlost_jizda = 0.7
        self.rychlost_koridor = 0.8

        self.smer = False 
        self.priority = 1

        self.zh1 = 7500
        self.zh2 = 7500
        self.zh3 = 7500
        
        self.hz1 = 7500
        self.hz2 = 7500
        self.hz3 = 1200        

        self.sobotin_wait = 2400
        self.petrov1_zabreh_wait = 2700
        self.petrov2_zabreh_wait = 2900
        self.petrov1_sobotin_wait = 2200
        self.petrov2_sobotin_wait = 2400
        self.petrov_zabreh_wait = 10000
        self.petrov2k_wait = 2620

        self.z3wait = 4200
        self.z5wait = 3000
        self.zvswait = 6500

        self.h3wait = 4500

    def run_route(self):
        self.throttle.setF0(True)
        
        self.sobotin_1_odj()
        self.petrov_s_z()
        self.zabreh_3_vj_c()
        self.zabreh_3_odj_c()
        self.petrov_z_s()
        self.sobotin_1_vj()

regiojet().start()