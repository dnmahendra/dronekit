from dronekit import connect, Vehicle, VehicleMode, LocationGlobalRelative, APIException

import time
import exceptions
import socket
import math
import argparse


def connectMyCopter():
    parser = argparse.ArgumentParser(description="commands")
    parser.add_argument("--connect")
    args = parser.parse_args()

    connection_string = args.connect

    if not connection_string:
        import dronekit_sitl
        sitl = dronekit_sitl.start_default()
        connection_string = sitl.connection_string()

    vehicle = connect(connection_string, wait_ready=True)

    return vehicle

# >> python connection_template.py --connect 127.0.0.1:14550


vehicle = connectMyCopter()

while vehicle.is_armable != True:
    print('Waiting for vehicle to become armable')
    time.sleep(1)
print('Vehicle is now armable')

vehicle.mode = VehicleMode('GUIDED')

while vehicle.mode != 'GUIDED':
    print('Waiting for the drone to enter GUIDED flight mode.')
    time.sleep(1)
print('Drone is in GUIDED mode now!')

vehicle.armed = True
while vehicle.armed == False:
    print('Waiting for the drone to become armed.')
    time.sleep(1)
print('props are spinning!')
