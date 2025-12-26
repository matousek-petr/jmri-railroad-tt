import jarray
import jmri

class brejlovec_zeleny(base_automated_route):

    address = 11
    sens_start = "IS50"
    running = "IS51"

    def __init__(self):
        self.throttle = self.getThrottle(self.address, False)
        self.auto = sensors.provideSensor(self.sens_start)
        self.auto_s = sensors.provideSensor(self.running)

        self.rychlost_stanice = 0.4
        self.rychlost_jizda = 0.6
        self.rychlost_koridor = 0.65
        self.smer = False
        self.priority = 5

        self.zh_a_1 = 7000
        self.zh_a_2 = 9000
        self.zh_a_3 = 10000
        
        self.hz_b_1 = 5000
        self.hz_b_2 = 5000
        self.hz_b_3 = 5000

        self.h1wait = 6600
        self.z1wait = 10900

    def run_route(self):
        self.throttle.setF0(True)

        self.zabreh_1_odj_a()
        self.autoblock_zh_a()
        self.hostejn_1_vj_a()
        self.hostejn_1_odj_b()
        self.autoblock_hz_b()
        self.zabreh_1_vj_b()

brejlovec_zeleny().start()