# Tempurpedic Control
<img src="https://github.com/Doug-Wyman/Tempurpedic_Control/blob/main/images/Capture.gif"
     alt="my screen"
     width="400"/>

Tempurpedic control is a set of python scripts. 
Each script sends the title command to a Tempurpedic adjustable bed frame.  

 - bedflat.py      --- <i>lowers both head and feet</i>
 - bedheaddown.py  --- <i>Lower the upper body</i>
 - bedheadup.py    --- <i>Raise the upper body</i>
 - bedlegsdown.py  --- <i>Lower the legs</i>
 - bedlegsup.py    --- <i>Raise the legs</i>
 - bedset1.py      --- <i>go to preset bed position 1</i>
 - bedset2.py      --- <i>go to preset bed position 2</i>
 - bedset3.py      --- <i>go to preset bed position 3</i>
 - bedset4.py      --- <i>go to preset bed position 4</i>
 - bedvibrate1.py  --- <i>go to preset vibration mode 1</i>
 - bedvibrate2.py  --- <i>go to preset vibration mode 2</i>
 - bedvibrate3.py  --- <i>go to preset vibration mode 3</i>
 - bedvibrate4.py  --- <i>go to preset vibration mode 4</i>
 - bedvibrateoff.py--- <i>Turn off all vibration</i>

These scripts can be called by either command_line platform cover entities
or command_line platform switch entities
created in Home Assistant configuration.yaml
 - covercontrols.yaml has the controls as a cover
 - switchcontrols.yaml creates the controls as switches

I've added two dashboards as yaml files. One has the controls as a
cover entity.  The other uses the command line switch.

 - coverdashboard.yaml  ---<i>The dashboard seen at the top of this readme.md
 - switchdashboard.yaml  ---<i>The dashboard seen at the top of this readme.md


The scripts use a hard coded IP address for the bed. Change the line in each file 
UDP_IP = "192.168.0.155"
to the UDP_IP = [your local address]

Tempurpedic has codes for 0 to 10 levels of vibration for each of the 
three zones (upper body, hips and legs).  If I can find an easy way of
implementing these 30 levels I will do so.  These codes are in the table of codes.

     A BIG caveat...  One would think There would be a way of controlling more than
     a single bed.  Thus the first few bytes may address a particular bed.  The program
     queries the web page at port 80 and that page may have a prefix code.  I would do 
     that if I were coding the program.  I only have one bed so I can't check it.

I wish there was a "command_line platform light" entity.

   Doug

I'll be 80 years old Nov 2022 and would love it if some young hacker (the good kind)
would fork off this into a good and more efficient set of scripts and entities.


 
