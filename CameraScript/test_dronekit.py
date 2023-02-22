from pymavlink import mavutil
import time
import serial.tools.list_ports

# ports = list(serial.tools.list_ports.comports())

# # Extract just the port names as strings
# port_strings = [port.device for port in ports]
# print(port_strings)

try:
    connection_string = 'COM4'  # IP address and port of the remote device
    master = mavutil.mavlink_connection(connection_string, baud=57600)
    time_start = time.monotonic()

    # Wait for the heartbeat message from the remote device
    master.wait_heartbeat(timeout=15)
    print("Heartbeat from system %u component %u" %
    (master.target_system, master.target_component))

    while True:
        msg = master.recv_match(type='ATTITUDE')
        print(msg)
        time_elapsed = time.monotonic() - time_start
        print(time_elapsed)
        time.sleep(1)
except KeyboardInterrupt:   
    master.close()

# # Send the reboot command
# msg = master.mav.command_long_encode(
#     0,                     # system id
#     0,                     # component id
#     mavutil.mavlink.MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN,  # command
#     0,                     # confirmation
#     1,                     # reboot autopilot (0=reboot system, 1=reboot autopilot only)
#     0, 0, 0, 0, 0, 0)      # parameters 4-9 (not used)
# master.mav.send(msg)

# # Close the connection
# master.close()


# # Set the servo ID and PWM value
# SERVO_ID = 4  # change this to match the servo ID that you want to move
# PWM_VALUE = 1000  # change this to set the desired PWM value

# # Send the servo command
# msg = master.mav.command_long_encode(
#     0,                # system id
#     0,                # component id
#     mavutil.mavlink.MAV_CMD_DO_SET_SERVO,  # command
#     0,                # confirmation
#     SERVO_ID,         # servo ID
#     PWM_VALUE,        # PWM value
#     0, 0, 0, 0, 0)    # parameters 3-7 (not used)
# master.mav.send(msg)

# # Wait for a bit and then move the servo back to its initial position
# time.sleep(1.0)
# msg = master.mav.command_long_encode(
#     0,                # system id
#     0,                # component id
#     mavutil.mavlink.MAV_CMD_DO_SET_SERVO,  # command
#     0,                # confirmation
#     SERVO_ID,         # servo ID
#     1500,             # initial PWM value
#     0, 0, 0, 0, 0)    # parameters 3-7 (not used)
# master.mav.send(msg)

# # Close the connection
# master.close()