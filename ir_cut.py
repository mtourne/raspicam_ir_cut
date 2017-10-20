'''
Controlling the rpi ir_cut camera [1] 
on Rasbperry Pi 3 model B (and after?)

ir_cut mechanism is controlled by the led on the cam
on earlier raspberry this worked with a gpio
but there is no line back to the ARM cpu on rasberry pi 3+
See [2] for more


Using executable found here:
  https://github.com/6by9/rpi3-gpiovirtbuf

[1] waveshare.com/wiki/RPi_IR-CUT_Camera
[2] https://github.com/waveform80/picamera/issues/265

'''

import os


EXECUTABLE='../rpi3-gpiovirtbuf/rpi3-gpiovirtbuf'
GPIO=134

def enable_filter():
    ''' set gpio to 1 '''
    os.system('{} s {} 1'.format(EXECUTABLE, GPIO))


def disable_filter():
    ''' set gpio to 0 '''
    os.system('{} s {} 0'.format(EXECUTABLE, GPIO))
