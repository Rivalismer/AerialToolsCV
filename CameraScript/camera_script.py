from pymavlink import mavutil
import time
import serial.tools.list_ports
import numpy as np

# Define important messages not on mavutil
CAMERA_INFORMATION = 259
CAMERA_SETTINGS = 260
STORAGE_INFORMATION = 261
CAMERA_CAPTURE_STATUS = 262
VIDEO_STREAM_INFORMATION = 263

# Get a list of available COM ports
ports = list(serial.tools.list_ports.comports())
print(ports)

# # Start connection listening to serial port - This assumes direct connection through COMM PORT, antenna version needs a slight tweak
# for port in ports:
#     if "Mavlink" in port.description:
#         try:
#             con = mavutil.mavlink_connection(port.device, baud=57600)

#             # Wait for first heartbeat
#             # This sets the system and component ID of remote systems for the link
#             con.wait_heartbeat()
#             print("Heartbeat from system %u component %u" %
#                 (con.target_system, con.target_component))

#             print(f"Connected to {port.device}")
#             comport = port.device # save for later
#         except Exception as e:
#             print(f"Could not connect to device, error: {e}")

# Temp for antenna testing
try:
    comport = 'COM6'
    con = mavutil.mavlink_connection(comport, baud=57600)
    print("Heartbeat from system %u component %u" %
        (con.target_system, con.target_component))

    # CUBE Setup

    # Camera setup - might need CCP for this

    # Setup for a timer
    start_time = time.monotonic()

    # Loop indefinitely
    while True:
        try:
            # Request a message
            # msg = con.mav.command_long_send(
            #     con.target_system,        # target system
            #     con.target_component,        # target component
            #     mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,
            #     0, # Confirmation
            #     CAMERA_SETTINGS, # message ID
            #     0, 0, 0, 0, 0, 0)

            # Wait for a short time before seeing if the packet arrived
            time.sleep(1.0)

            # Receive & print message
            #settings = con.recv_match(type="CAMERA_INFORMATION")
            #settings = con.recv_match(type="CAMERA_SETTINGS")
            settings = con.recv_match()
            
            # Update timer
            elapsed_time = time.monotonic() - start_time

            # Print info
            if settings is not None:       
                print(f"Time: {elapsed_time}\n Settings: {settings}")

                # Attempt to take an image
                con.mav.command_long_send(con.target_system, 
                    con.target_component,
                    mavutil.mavlink.MAV_CMD_DO_TRIGGER_CONTROL, 
                    0, # Confirmation 
                    1, # Take only a single picture
                    0, 0, 0, 0, 0, 0)
            print(f"Time: {elapsed_time}")
            time.sleep(1)

        except Exception as e:

            # If it fails, restart connection(?)
            print(f"Error: {e}")

            try:
                con.close()
            except:
                pass
            
            try:
                con = mavutil.mavlink_connection(comport, baud=57600)
                con.wait_heartbeat(timeout=5)

            except Exception as e:
                print(f"Could not connect to device, error: {e}")
                exit()

except KeyboardInterrupt:
    con.close()