import board
import digitalio
import storage
import usb_cdc
import usb_hid
import usb_midi

# boot.py
# If the top-left key (D13 on this board) is held during boot it enables USB storage, serial, etc. 
# This allows for updating and debugging the code.
# Otherwise it will boot with only keyboard & mouse enabled
button = digitalio.DigitalInOut(board.D13)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

if button.value:
    storage.disable_usb_drive() # Hides device storage
    usb_cdc.disable() # Disables serial comms
    usb_midi.disable() # Disables midi
    usb_hid.enable(boot_device=1) # Enables keyboard before OS boot
    
button.deinit()
