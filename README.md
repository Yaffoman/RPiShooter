# RPiShooter
## Description
I built this completely from scratch, though I used several sources as inspiration along the way.
I used a detection script from EdjeElectronics as a jumping off point for my own.
I also modeled parts of my design after HackerShack's motion tracking airsoft gun.
Links to their youtube videos are listed below in 'References'
## Getting Started
### Software
First, run the get_pi_requirements script. Ensure the correct versions of opencv and tensorflow are installed as defined in the script, if not, uninstall and reinstall manually the correct version.
That should be all for the setup, navigate to the src directory to run
sudo python3 Main.py --modeldir ../TFLite-Sample
### Hardware
#### Things you'll need:
* 2 aluminum squares at least 1/10" thick (6" x 6" should be enough)
* aluminum L shape for the turret
* thin brake line for the barrel
* 2 valves, air and water tight respectively
* 2L bottle for air tank, small waterbottle for water tank
* hot glue gun
* tubing
* tubeless tire valve
* 2 motor drivers (12v, stepper motor capable)
* 2 relays (one for each valve)
* many wires (preferably of many different colors)
* castor balls, low profile
* Tools: drill and assortment of bits, a screwdriver, pliers, soldering iron, wrenches, wire cutters/strippers, air compressor
* nuts and bolts, maybe some spacers
* a raspberry pi 3+ with a camera
* a LiDAR sensor
#### Directions
Building this will take some ingenuity to put the parts together with what you have available to you. I used spare parts so I had to buy many adapters and extenders to get everything how I wanted but try to buy everything so that it will all just fit together. 
Look to the images for guidance, but the exact specifications don't really matter. 
First, plan it all out. I suggest drawing a scale model, or drawing directly on the steel so you can orient everything. 
The vertical piece should be slightly off center as the barrel will be about an inch away from the beam. The barrel should be exactly centered if possible. 
Drill all the holes and start putting it all together. Order isn't vital except for the base plates which I wouldn't connect until the end since it makes it much harder to bolt down everything else.
## Manual
It will first ask to choose a mode:
* i - interacactive, wasd to move, k to fire, l to measure distance, h to display commands, q to quit
* a - autonomous, will detect people and fire at them
## Troubleshooting
### Errors with tensorflow or opencv
Incorrect versions, uninstall and install the correct specific version
### Cannot access shared file libfds.h
Ignore, seems to be some issue with tensorflow that doesn't affect performance.
### Motors make sounds, but don't move
Ensure voltage is at least 9V across each motor, sometimes it drops when both run off the same supply.
### Motors turn on, work for a bit, then turn off
Still investigating, I believe the motor drivers overheat and an internal heat fault circuit kills the driver to protect it. Similarly it may be an incorrect wiring causing a short circuit. 
Check all the wiring, monitor the voltages, and add an extra big heat sync.
## References
https://www.youtube.com/watch?v=npZ-8Nj1YwY&ab_channel=EdjeElectronics   
https://www.youtube.com/watch?v=HoRPWUl_sF8&ab_channel=HackerShack   
https://www.youtube.com/watch?v=r3D5FAPwqj8&ab_channel=ChrisNotap  
