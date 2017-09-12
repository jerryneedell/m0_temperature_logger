# m0_temperature_logger

WARNING - This is test code - use at your own risk!
It does not check for the File system being full - yet

sample code for loging cpu temperature to M0 file system
This is a simple modification to an example of writing to the FS provided by Don Blalr.
Just getting started.

Next stpes are to add error checking, especially for when the FS is full.
Temperaturd sampling rate should be much slower for a useful example as well.


Uses pin D0 to determine File System State
D0 - Grounded - boot to allow CircuitPython to Write to FS
D0- Open - boot to normal USB writeble FS

use code.py for automatic execution on RESET 
ue fs_gemma.py to manually execute from REPL

if installed as code.py 
then when D0 - open - the RED LED (D13) will blink rapidly and the FS wil be mounted normaly
if D0 - grounded - then RED LED will blink every 2 seconds and 10 samples of the cpu etmperature will be written to temp_log.txt
