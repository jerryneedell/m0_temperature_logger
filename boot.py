import digitalio
import board
import storage

switch=digitalio.DigitalInOut(board.D0)
switch.switch_to_input(pull=digitalio.Pull.UP)

storage.remount("/", switch.value) # switch.value==False means datalogging mode:  allow circuitpython code to write to flash, while making USB read-only.
