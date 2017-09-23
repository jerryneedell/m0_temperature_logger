import board
import digitalio
import microcontroller
import time

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()

#create logging interval counter
logInterval = 0

try:
    with open("/temperature.txt", "a") as fp:
        while True:
            if(logIntererval == 60)
                temp = microcontroller.cpu.temperature
                # do the C-to-F conversion here if you would like
                fp.write('{0:f}\n'.format(temp))
                fp.flush()
                # 5 quick blinks
                while (blinkLoop in range(5):
                    led.value = not led.value
                    time.sleep(.2)
                # reset Interval counter
                logInterval = 0
            #blink the led
            led.value = not led.value
            time.sleep(1)
            logInterval += 1
except OSError as e:
    delay = 0.5
    if e.args[0] == 28:
        delay = 0.25
    while True:
        led.value = not led.value
        time.sleep(delay)

