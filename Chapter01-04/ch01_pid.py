import matplotlib
matplotlib.use('Agg')

import PID
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

P = 1.4
I = 1
D = 0.001
pid = PID.PID(P, I, D)

pid.SetPoint = 0.0
pid.setSampleTime(0.25)  # a second

total_sampling = 100
sampling_i = 0
measurement = 0
feedback = 0

feedback_list = []
time_list = []
setpoint_list = []


def get_soil_moisture():
    # reading from Arduino
    # value 0 - 1023
    return 200



print('PID controller is running..')
try:
    while 1:
        pid.update(feedback)
        output = pid.output

        soil_moisture = get_soil_moisture()        
        if soil_moisture is not None:

            # # ## testing
            # if 23 < sampling_i < 50:
            #     soil_moisture = 300
            
            # if 65 <= sampling_i < 75:
            #     soil_moisture = 350
            
            # if sampling_i >= 85:
            #     soil_moisture = 250
            # # ################
                                
            if pid.SetPoint > 0:
                feedback += soil_moisture + output

            print('i={0} desired.soil_moisture={1:0.1f} soil_moisture={2:0.1f} pid.out={3:0.1f} feedback={4:0.1f}'
                  .format(sampling_i, pid.SetPoint, soil_moisture, output, feedback))
            if output > 0:
                print('turn on watering system')
            elif output < 0:
                print('turn off watering system')

        if 20 < sampling_i < 60:
            pid.SetPoint = 300  # soil_moisture

        if 60 <= sampling_i < 80:
            pid.SetPoint = 200  # soil_moisture

        if sampling_i >= 80:
            pid.SetPoint = 260  # soil_moisture

        

        time.sleep(0.5)
        sampling_i += 1

        feedback_list.append(feedback)
        setpoint_list.append(pid.SetPoint)
        time_list.append(sampling_i)

        if sampling_i >= total_sampling:
            break

except KeyboardInterrupt:
    print("exit")


print("pid controller done.")
print("generating a report...")
time_sm = np.array(time_list)
time_smooth = np.linspace(time_sm.min(), time_sm.max(), 300)
feedback_smooth = spline(time_list, feedback_list, time_smooth)

fig1 = plt.gcf()
fig1.subplots_adjust(bottom=0.15, left=0.1)

plt.plot(time_smooth, feedback_smooth, color='red')
plt.plot(time_list, setpoint_list, color='blue')
plt.xlim((0, total_sampling))
plt.ylim((min(feedback_list) - 0.5, max(feedback_list) + 0.5))
plt.xlabel('time (s)')
plt.ylabel('PID (PV)')
plt.title('Soil Moisture PID Controller')


plt.grid(True)
fig1.savefig('pid_soil_moisture.png', dpi=100)
print("finish")

