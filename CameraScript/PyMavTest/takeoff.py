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
con.mav.command_long_send(con.target_system, con.target_component, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 
    0, 1, 0, 0, 0, 0, 0)
# Our params 1 and 2 are; 1 - arm, 0 for force.

# Listen to see whether our command failed or succeeded
msg = con.recv_match('COMMAND_ACK', blocking = True)
print(msg)

# Pass takeoff command - 0,0 as lat/lon params means it uses the current lat/lon
con.mav.command_long_send(con.target_system, con.target_component, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    0, 0, 0, 0, 0, 0, 10)

# Listen to see whether our command failed or succeeded
msg = con.recv_match('COMMAND_ACK', blocking = True)
print(msg)