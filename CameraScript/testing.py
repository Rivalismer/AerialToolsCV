from pymavlink import mavutil
import time
import serial.tools.list_ports

# Get a list of available COM ports
#ports = list(serial.tools.list_ports.comports())

# Extract just the port names as strings
port_strings = [port.device for port in ports]

# Print the list of port names
print(port_strings)

# Start connection listening to serial port
for port in ports:
    try:
        con = mavutil.mavlink_connection(port.device)
    except:
        pass

# Wait for first heartbeat
# This sets the system and component ID of remote systems for the link
con = mavutil.mavlink_connection('/dev/ttyUSB0')
con.wait_heartbeat()
print("Heartbeat from system %u component %u" %
    (con.target_system, con.target_component))

# Setup for camera command
#component_id = 100
# con.mav.command_long_send(con.target_system, con.target_component, 
# mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE, 0, 260, 0, 0, 0, 0, 0, 0)

# # Receive message
# msg = con.recv_match("COMMAND_ACK", blocking=True)
# msg_out = con.recv_match(type = "CAMERA_SETTINGS", blocking=True)
# print(msg_out)

# #Take a picture
# con.mav.command_long_send(con.target_system, con.target_component,
#     mavutil.mavlink.MAV_CMD_IMAGE_START_CAPTURE, 0, 1, 1, 1, 0, 0, 0, 0)

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

############# RUN UNTIL MISSION IS OVER ##################################
# Define the message IDs for receiving mission status and mission item reached
# MISSION_ITEM_REACHED_ID = 46 # Double check these
# MISSION_CURRENT_ID = 42

# # Wait for the mission to start
# while True:
#     msg = con.recv_match(type=MISSION_CURRENT_ID) # Change to name, this takes a string
#     if msg is not None:
#         if msg.seq > 0:
#             print("Mission started")
#             break

# # Loop until the mission is over
# while True:
#     # Wait for a mission item to be reached
#     msg = con.recv_match(type=MISSION_ITEM_REACHED_ID)
#     if msg is not None:
#         print(f"Reached mission item {msg.seq}")

#         # Check if the last mission item has been reached
#         if msg.seq == msg.seqtotal - 1:
#             print("Mission over")
#             break