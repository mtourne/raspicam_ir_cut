from picamera import PiCamera
from time import sleep

import ir_cut

## XX (mtourne): cam led (ir cut filter)
## can't be controlled easily from pi 3-b because
## gpio is not accessible directly on the arm cpu but via
## gpio extender
## see : https://github.com/waveform80/picamera/issues/265

## import RPi.GPIO as GPIO
##
## # Use GPIO numbering
## GPIO.setmode(GPIO.BCM)
##
## # Set GPIO for camera LED
## # Use 5 for Model A/B and 32 for Model B+
## #CAMLED = 5
## CAMLED = 32
##
## # Set GPIO to output
## GPIO.setwarnings(False)
## GPIO.setup(CAMLED, GPIO.OUT, initial=True)
##
## # high normal, low: night mode
## #GPIO.output(CAMLED, True) # normal
## #GPIO.output(CAMLED, False) # night mode

camera = PiCamera()


#ir_cut.enable_filter()
ir_cut.disable_filter()
camera.start_preview()
sleep(20)
camera.stop_preview()
