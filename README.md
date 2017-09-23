# m0_temperature_logger

WARNING - This is test code - use at your own risk!

sample code for loging cpu temperature to M0 file system
This example was based on an example of writing to the FS provided by Don Blalr.
https://github.com/edgecollective/circuitpython-flash-logger

Thanks to https://github.com/sigafoos for writing th guide and for adding the error handling. 

Note: make sure you have CircuitPython 2.0.0 or above on your device!

2.0.0 was released 9/12/2017, so if you bought your board before or around that time there’s a good chance it needs updating. Download the update and follow the instructions on the 2.0.0 release page.
Getting the temperature
One of the new packages included in 2.0.0 is microcontroller.cpu.temperature: this gives you the temperature (in Celsius) of the board’s CPU. It isn’t as accurate as a TMP36 or DHT22, since it’s the temperature of the CPU, not the ambient air, but it’s pretty close!

Getting the temperature is as simple as can be. In the REPL:
```
Adafruit CircuitPython 2.0.0 on 2017-09-12; Adafruit Gemma M0 with samd21e18
>>> import microcontroller
>>> microcontroller.cpu.temperature
29.6556
```
If you’d like it in Fahrenheit, you can create a function for that:
```
>>> def fahrenheit(celsius):
...     return (celsius * 9 / 5) + 32
...
>>> fahrenheit(microcontroller.cpu.temperature)
90.1077
```


Writing to the filesystem

Getting the temperature in the REPL is all well and good, but requires you to type the command every time.

Thankfully, CircuitPython 2.0.0 also introduced the storage module, which lets you access the internal storage of the board. There isn’t a lot of it, but for storing a few readings it should be plenty. By default you can write to the system via USB (ie saving code.py) and not in code, so first you’ll need to change that.

Setting readonly to False on boot
You can only use this in boot.py, which is executed before the USB connection is made. If boot.py doesn’t exist, create it with this:

Warning: once you start this you need to continue until the end of the section or you’ll have problems writing code to the board. If you’d prefer to be safe, just read this and skip to the next section, “Selectively setting readonly to False on boot”.
```
import storage

storage.remount("/", readonly=False)
```
On every boot the root filesystem will be mounted so that CircuitPython can write to it.

You can now write to the internal storage via the REPL:
```
>>> with open("/tmp.txt", "a") as fp:
...     fp.write("X")
...
```
You might need to reboot the board before you see the file, but it will be there in the file explorer.



Only one thing can have write access at a time, though, so by allowing your Python code to write to the device you’ve disabled USB write access. This means updating code.py will no longer work! Even worse, you can’t edit boot.py either, so at first you might think you’re stuck like this forever. Luckily, you can edit and remove files via the REPL:
```
>>> import os
>>> os.remove("/boot.py")
```
Then reboot the device and you’ll be able to edit via USB as normal.
Selectively setting readonly to False on boot
Recreate boot.py:
```
import digitalio
import board
import storage

Switch = digitalio.DigitalInOut(board.D0)
switch.switch_to_input(pull=digitalio.Pull.UP)

storage.remount("/", readonly=switch.value)
```
This will read the value of the D0 pin, which has been set to a pullup: it reads True (HIGH, 1, etc in Arduino) if it has not been grounded, but if connected to ground it reads False. Since we want it to be readonly False when the board should be written by the code and not USB, you only need to connect the D0 pin to ground when you want the board to be able to write via the code.

The Circuit Playground makes this easy: the D0 pin is the toggle switch. On other boards, like the Gemma M0, you’ll need to use wires or alligator clips. This example runs on all the CircuitPlayGound Express, Gemma M0 and Trinket M0.

Logging the temperature
m0_templogger.py  contains exanmple code for logging the temperature to a file.
You can execute it from the REPL:
```
import m0_temlogger
```
or use code.py as the file name for automatic execution oon boot.

This code creates a led variable, sets it to the D13 pin and configures it for output (this is the built-in LED pin).  It also creates a coundown counter to control the logger frequency independenly of the LED blink frequency. For the exampl the temperature is logged once per minute. It is initialised to zero so it writes a value immediately st the start. when it write, the countdown is reset and it jsut blinnks the LED on/off every second (2 second cycle). If it is time to write, it opens the temperature.txt file for appending (so future reboots add to the end of the file instead of overwriting it), gets the temperature and writes it to the file with a line break after each reading (on Windows, some editors like Notepad won’t recognize the line ending). At ech writem the LED is blinked rapidly a few times.


There could be an error opening the file for writing, or for writing the file: maybe your board doesn’t have D0 pulled low to enable writing. Maybe your internal storage is out of space. The except block handles an OSError exception. If the error code is 28 that means the device is out of space. The LED will blink four times a second to indicate this. Otherwise the “issue” is probably that the board set to read-only (which is probably by design!) and will blink once a second.

Keep going
You now have code that will change the read/write status of the drive depending on a pin state, log the temperature once a second a provide three different status indicators. But there could be more to do, if you’d like.

Maybe you want to add better error reporting (the OSError error code for a read only device is 30). Or log differently, or log to a different file. This was only a starting point, so make it your own!
