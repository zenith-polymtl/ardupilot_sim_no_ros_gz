from pymavlink import mavutil
import time

print("Started")
# Establish connection to MAVLink
connection = mavutil.mavlink_connection('tcp:127.0.0.1:5762')


# Wait for a heartbeat
print("Waiting for heartbeat...")
connection.wait_heartbeat()
print("Heartbeat received!")

# Set mode to GUIDED
def set_mode(mode):
    mode_id = connection.mode_mapping()[mode]
    connection.mav.set_mode_send(
        connection.target_system,
        mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
        mode_id
    )
    print(f"Setting mode to {mode}...")

set_mode("GUIDED")

# Arm the vehicle
print("Arming motors...")
connection.mav.command_long_send(
    connection.target_system,
    connection.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0
)

# Wait for arming confirmation
connection.motors_armed_wait()
print("Motors armed!")

# Takeoff
altitude = 20  # Target altitude in meters
print(f"Taking off to {altitude} meters...")
connection.mav.command_long_send(
    connection.target_system,
    connection.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    0,
    0, 0, 0, 0, 0, 0, altitude
)
time.sleep(30)  # Allow time for the drone to ascend

# Send a single waypoint (50 meters North, 50 meters East, maintaining altitude)
print("Sending waypoint...")
connection.mav.set_position_target_local_ned_send(
    0,  # Time in milliseconds
    connection.target_system,
    connection.target_component,
    mavutil.mavlink.MAV_FRAME_LOCAL_NED,
    0b110111111000,  # Position mask
    200, 200, -altitude,  # X (North), Y (East), Z (Down)
    0, 0, 0,  # No velocity
    0, 0, 0,  # No acceleration
    0, 0      # No yaw or yaw rate
)

# Wait for the waypoint to be reached
print("Waiting for waypoint to be reached...")
time.sleep(10)



# Land
print("Landing...")
connection.mav.command_long_send(
    connection.target_system,
    connection.target_component,
    mavutil.mavlink.MAV_CMD_NAV_LAND,
    0,
    0, 0, 0, 0, 0, 0, 0
)

# Wait for the drone to land
print("Waiting for landing...")
connection.motors_disarmed_wait()
print("Landed and motors disarmed!")

connection.close()
