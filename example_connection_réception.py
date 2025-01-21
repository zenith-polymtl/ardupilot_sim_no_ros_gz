from pymavlink import mavutil

connection = mavutil.mavlink_connection('tcp:127.0.0.1:5762')
print('Waiting for heartbeat')
connection.wait_heartbeat()
print("Heartbeat received!")

# Request a specific message type (e.g., GLOBAL_POSITION_INT) at 2 Hz (500 ms interval)
message_type = mavutil.mavlink.MAVLINK_MSG_ID_GLOBAL_POSITION_INT  # Replace with desired message type ID
frequency_hz = 2  # Frequency in Hz
interval_us = int(1e6 / frequency_hz)  # Interval in microseconds

connection.mav.command_long_send(
    connection.target_system,  # Target system ID
    connection.target_component,  # Target component ID
    mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,  # Command to set message interval
    0,  # Confirmation
    message_type,  # Message ID
    interval_us,  # Interval in microseconds
    0, 0, 0, 0, 0  # Unused parameters
)

print("Requested GLOBAL_POSITION_INT messages at 2 Hz.")



while True:
    msg = connection.recv_match( blocking=True)
    # Example: Extract data from a GLOBAL_POSITION_INT message
    if msg.get_type() == "GLOBAL_POSITION_INT":
        print(f"Latitude: {msg.lat / 1e7}°")
        print(f"Longitude: {msg.lon / 1e7}°")
        print(f"Altitude: {msg.alt / 1000} m")
        print(f"Relative Altitude: {msg.relative_alt / 1000} m")
        print(f"Velocity: {msg.vx / 100} m/s, {msg.vy / 100} m/s, {msg.vz / 100} m/s")