# DoorPhone info

We have a doorphone with the followibg abilities:

1. Recieve an door-bell-ring signal
2. Carry out a two-way-full duplex sound communication
3. Open door
4. Other functions (i.e mute)

The doorphone has three pins which carry power and a communication-signal to the phone.
The three pins connect to a PCB circuit board which controls various IOs:
* Microphone: In-Sound
* Speaker: Out-sound
* Button: Signal to unlock door

## Implementation

The PCB connection behind the button to open the door can be "short-circuited" to emulate a button press.

The short circuiting can be done using a relay (to avoid damaging anyhardware b/c of voltage difference).
The Raspberry Pi's GPIO pins can be used to control the relay.

## TODO list
* [ ] Check that soldering connections behind PCB board are accessible
* [ ] Check if bridging gap with wires / paperclips triggers the unlocking signal
* [ ] Bridge gap with relay + battery
* [ ] Set up SSH to raspberry pi
* [ ] Unlock door via SSH -> Bash Script -> Raspberry Pi
* [ ] Set Raspberry-Pi up with telegram
* [ ] Unlock door via Telegram

## Useful links
https://www.instructables.com/id/Controlling-Any-Device-Using-a-Raspberry-Pi-and-a-/
https://howchoo.com/g/m2qwmte5nzk/how-to-use-a-relay-with-a-raspberry-pi
https://tutorials-raspberrypi.com/raspberry-pi-control-relay-switch-via-gpio/
https://www.allaboutcircuits.com/projects/build-a-raspberry-pi-pushbutton-switch/
https://raspberrypi.stackexchange.com/questions/71246/use-gpio-to-trigger-button-press-in-software/71264#71264u
