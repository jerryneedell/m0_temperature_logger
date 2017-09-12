import digitalio
import board
import microcontroller
import time

switch=digitalio.DigitalInOut(board.D0)
switch.switch_to_input(pull=digitalio.Pull.UP)

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()

if switch.value==False: # if D0 is pulled low, then datalog mode -- no USB write allowed
    for i in range(10): # keep number of writes low for testing
        f=open('temp_log.txt','a')
        temp=microcontroller.cpu.temperature
        f.write('{0:03d}  {1:.3f}\n'.format(i,temp))
        f.close()
        led.value = not led.value # blink to indicate successful write
        time.sleep(1)
        
else:
    while True:
        led.value = not led.value #faster blink to indicate in USB read-write mode
        time.sleep(.2)
