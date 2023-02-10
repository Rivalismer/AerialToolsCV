from pymavlink import mavutil
import time

# Start connection listening to serial port
con = mavutil.mavlink_connection('COM4')

# Wait for first heartbeat
# This sets the system and component ID of remote systems for the link
con.wait_heartbeat()
print("Heartbeat from system %u component %u" %
    (con.target_system, con.target_component))

# Setup for camera command
#component_id = 100
con.mav.command_long_send(con.target_system, con.target_component, 
mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE, 0, 260, 0, 0, 0, 0, 0, 0)

# Receive message
msg = con.recv_match("COMMAND_ACK", blocking=True)
msg_out = con.recv_match(type = "CAMERA_SETTINGS", blocking=True)
print(msg_out)

#Take a picture
con.mav.command_long_send(con.target_system, con.target_component,
    mavutil.mavlink.MAV_CMD_IMAGE_START_CAPTURE, 0, 1, 1, 1, 0, 0, 0, 0)

time.sleep(1)
con.mav.command_long_send(con.target_system, con.target_component,
    mavutil.mavlink.MAV_CMD_IMAGE_STOP_CAPTURE, 0, 0, 0, 0, 0, 0, 0, 0)

# Alternative way to just take a singular picture
# con.mav.command_long_send(con.target_system, con.target_component,
#     mavutil.mavlink.MAV_CMD_DO_TRIGGER_CONTROL, 0, 1, 0, 0, 0, 0, 0, 0)

# # Take video
# con.mav.command_long_send(con.target_system, con.target_component,
#     mavutil.mavlink.MAV_CMD_VIDEO_START_CAPTURE, 0, 1, 0, 0, 0, 0, 0, 0)

# time.sleep(5)

# con.mav.command_long_send(con.target_system, con.target_component,
#     mavutil.mavlink.MAV_CMD_VIDEO_STOP_CAPTURE, 0, 0, 0, 0, 0, 0, 0, 0)