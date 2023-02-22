from pymavlink import mavutil

# Start connection listening to UDP port
con = mavutil.mavlink_connection('udpin:localhost:14551')

# Wait for first heartbeat
# This sets the system and component ID of remote systems for the link
con.wait_heartbeat()
print("Heartbeat from system %u component %u" %
    (con.target_system, con.target_component))

# NED refers to a reference coordinate system, to which multiple are supported
# NED specifically is the position compared to the origin of the EKF; that is, the
# first good reading the EKF got
# The magic numbers refer to: x, y, z (positive down), vx, vy, vz, ax, ay, az, yaw, yaw_rate

# The type mask refers to which of the fields to be ignored. Thus, if you want to keep values the bit in position
# should be 0. NB: It counts from right -> left, so the same as binary numbers.
# fx. if I want x,y,z and nothing else, my mask will be:
# 0b110111111000
# Bit 10 is always 0 (unused) - use force instead of acceleration, not implemented.
type_mask = int(0b110111111000)
con.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10, con.target_system, 
    con.target_component, mavutil.mavlink.MAV_FRAME_LOCAL_NED, type_mask, 10, 0, -10, 0, 0, 0, 0, 0, 0, 0, 0))

# We can also use a global frame target
# This command does not use the EKF, but rather uses a global coordinate frame
# There are many options for which altitude to use, here relative_alt is relative to our "home" (start) altitude
# Note that in this reference frame, the altitude needs to be positive
# Magic numbers here are:
# lat_int, lon_int, alt, vx, vy, vz, ax, ay, az, yaw, yaw_rate
# lat and lon are multiplied by 1e7 to make them ints.

lat_int = int(-35.362948 * 10 ** 7) # Change for your coordinates
lon_int = int(149.164985 * 10 ** 7)
con.mav.send(mavutil.mavlink.MAVLink_set_position_target_global_int_message(10, con.target_system, 
    con.target_component, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, type_mask, lat_int, lon_int, 10, 0, 0, 0, 0, 0, 0, 0, 0))

# Receive updates as to how the drone is doing
while 1:
    # Two different messages, the controler output gives for example target distance
    msg_out = con.recv_match(type = 'MAV_CONTROLLER_OUTPUT', blocking = True)
    print(msg_out)

    # Local position NED on the other hand gives the position of the drone in relation to
    # EKF origin. Its outputs are (almost) the same as the command we sent earlier:
    # x, y, z, vx, vy, vz
    msg_local = con.recv_match(type = 'LOCAL_POSITION_NED', blocking = True)
    print(msg_local)