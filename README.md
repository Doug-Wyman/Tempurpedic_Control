# Tempurpedic Control
<img src="https://github.com/Doug-Wyman/Tempurpedic_Control/blob/main/images/Capture.GIF"
     alt="my screen"
     width="400"/>

As of June 2025 I have changed Tempurpedic control to use the HACS component pyscript
The file send_packet.py is a set of one line python scripts. 
Each script becomes an Action (service) called by:
   action: call-service
   service: pyscript <dot> <script> i.e. service: pyscript.bed_head_up
   pyscript sends the UDP packet command to a Tempurpedic adjustable bed frame.  

 - @bed_flat      --- <i>lowers both head and feet</i>
 - @bed_head_down.py  --- <i>Lower the upper body</i>
 - @bed_head_up.py    --- <i>Raise the upper body</i>
 - @bed_legs_down.py  --- <i>Lower the legs</i>
 - @bed_legs_up.py    --- <i>Raise the legs</i>
 - @bed_preset1.py      --- <i>go to preset bed position 1</i>
 - @bed_preset2.py      --- <i>go to preset bed position 2</i>
 - @bed_preset3.py      --- <i>go to preset bed position 3</i>
 - @bed_preset4.py      --- <i>go to preset bed position 4</i>
 - @bed_vibrate1.py  --- <i>go to preset vibration mode 1</i>
 - @bed_vibrate2.py  --- <i>go to preset vibration mode 2</i>
 - @bed_vibrate3.py  --- <i>go to preset vibration mode 3</i>
 - @bed_vibrate4.py  --- <i>go to preset vibration mode 4</i>
 - @bed_vibrateoff.py--- <i>Turn off all vibration</i>


I've added a dashboard as yaml file. 

 - bed_dashboard.yaml  ---<i>The dashboard seen at the top of this readme.md

The scripts use a hard coded IP address for the bed. Change the line in each file 
UDP_IP = "192.168.0.155"
to the UDP_IP = [your local address]

Tempurpedic has codes for 0 to 10 levels of vibration for each of the 
three zones (upper body, hips and legs).  If I can find an easy way of
implementing these 30 levels I will do so.  These codes are in the table of codes.


   Doug

I'll be 83 years old Nov 2025 and would love it if some young hacker (the good kind)
would fork off this into a good and more efficient set of scripts and entities.


 
