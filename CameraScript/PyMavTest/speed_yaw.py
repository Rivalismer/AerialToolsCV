from pymavlink import mavutil

# Start connection listening to UDP port
con = mavutil.mavlink_connection('udpin:localhost:14551')

# Wait for first heartbeat
# This sets the system and component ID of remote systems for the link
con.wait_heartbeat()
print("Heartbeat from system %u component %u" %
    (con.target_system, con.target_component))

# Send a command long
# This sort of command takes in:
# (target_system, target_component, command, confirmation, param1, ..., param7)
# Target sys and component is automatically loaded from the heartbeat
# Command refers to the command number, all of which are declared in mavutil.mavlink
# Confirmation is either 0/1
# Rest of the params depends on the command you're trying to send
# For our command it takes in the params:
# deg, sec (rate of change deg/sec), CW/CCW (add/subtract the degrees), rel/abs (relative or absolute direction)
con.mav.command_long_send(con.target_system, con.target_component, mavutil.mavlink.MAV_CMD_CONDITION_YAW, 
    0, 45, 25, 0, 0, 0, 0)

# And to change the speed
# The only parameter that matters here is param 2 (counting from 0), which is the speed target, everything else is 0
con.mav.command_long_send(con.target_system, con.target_component, mavutil.mavlink.MAV_CMD_DO_CHANGE_SPEED, 
    0, 0, 5, 0, 0, 0, 0)