from pymavlink import mavutil

# Start connection listening to UDP port
con = mavutil.mavlink_connection('udpin:localhost:14551')

# Wait for first heartbeat
# This sets the system and component ID of remote systems for the link
con.wait_heartbeat()
print("Heartbeat from system %u component %u" %
    (con.target_system, con.target_component))

# Get the rest of the telemetry
while 1:
    # Filter for only the ATTITUDE part of the message (can be changed to anything)
    msg = con.recv_match(type='ATTITUDE', blocking=True)
    print(msg)