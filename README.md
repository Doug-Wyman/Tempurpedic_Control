# Tempurpedic Control
<img src="images/capture.jpg"
     alt="my screen"
     width="400"/>

Tempurpedic control is a set of python scripts. 
Each script sends the title command to a Tempurpedic adjustable bed frame.  


These scripts are called
by command line entities created in Home Assistant.
 - bedflat.py
 - bedheaddown.py
 - bedheadup.py
 - bedlegsdown.py
 - bedlegsup.py
 - bedset1.py
 - bedset2.py
 - bedset3.py
 - bedset4.py
 - bedvibrate1.py
 - bedvibrate2.py
 - bedvibrate3.py
 - bedvibrate4.py
 - bedvibrateoff.py

The scripts use a hard coded IP address for the bed.
Change the line in each file UDP_IP = "192.168.0.155"
to the UDP_IP = <your local address>

 
