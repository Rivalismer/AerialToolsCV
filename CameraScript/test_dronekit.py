# Import DroneKit-Python
import dronekit_sitl
from dronekit import connect

# Connect to the Vehicle.
vehicle = connect('COM4', wait_ready=True)

# Get some vehicle attributes (state)
print( "Get some vehicle attribute values:")
print( " GPS: %s" % vehicle.gps_0)
print( " Battery: %s" % vehicle.battery)
print( " Last Heartbeat: %s" % vehicle.last_heartbeat)
print( " Is Armable?: %s" % vehicle.is_armable)
print (" System status: %s" % vehicle.system_status.state)
print( " Mode: %s" % vehicle.mode.name )   # settable

# Close vehicle object before exiting script
vehicle.close()
