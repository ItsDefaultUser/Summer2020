import os
import hub
import utime
from spike import DistanceSensor



wall_detector = DistanceSensor('A')

run_amount = 0

while run_amount < 1000 :
    dist_cm = wall_detector.get_distance_cm()
    hub.port.F.motor.run_at_speed(speed = dist_cm)
    run_amount+=1

hub.port.F.motor.brake()
#hub.sound.beep(440,100)
#hub.display.show('JEREMY ', loop=True, delay=500)

