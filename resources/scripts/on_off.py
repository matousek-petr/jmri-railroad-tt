import jarray
import jmri
    
class on_off(jmri.jmrit.automat.AbstractAutomaton) :

    def init(self):
        return

    def handle(self):

        power = jmri.InstanceManager.getDefault(jmri.PowerManager).getPower()

        if(power == jmri.PowerManager.ON):
            powermanager.setPower(jmri.PowerManager.OFF)
 
        else:
            powermanager.setPower(jmri.PowerManager.ON)

        time.sleep(1)

        return 0

on_off().start()