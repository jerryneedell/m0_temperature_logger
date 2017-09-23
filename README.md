# m0_temperature_logger

WARNING - This is test code - use at your own risk!

sample code for loging cpu temperature to M0 file system
This is a simple modification to an example of writing to the FS provided by Don Blalr.
https://github.com/edgecollective/circuitpython-flash-logger

Just getting started.

Next steps are to add error checking, especially for when the FS is full.
Temperature sampling rate should be much slower for a useful example as well.


Uses pin D0 to determine File System State
D0 - Grounded - boot to allow CircuitPython to Write to FS
D0- Open - boot to normal USB writeble FS

use code.py for automatic execution on RESET 
use m0_templogger.py to manually execute from REPL

if installed as code.py 
then when D0 - open - the RED LED (D13) will blink every second and the FS wil be mounted normaly

if D0 - grounded - then RED LED will blink rapidly when a temperture value is logged every minute and every  two seconds in between readings

If a FS error is detected (out of space or any other error) the Red LED will blink every half second.


