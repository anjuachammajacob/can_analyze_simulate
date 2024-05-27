import can
import cantools

# Path to your DBC file
dbc_file = '/home/anjujacob/python/dbc/CVM3_CAN02.dbc'

# Load DBC file
db = cantools.database.load_file(dbc_file)

# Example message name to send
message_name = 'diagVehState_BASE'

# Find the message in the DBC file
message = db.get_message_by_name(message_name)

# Example data to encode into the message
data_to_send = {
    'diagCondVehSpd_BASE': 1,
    'diagCondEngSpd_BASE': 1,
    'diagCondGearNeutral_BASE': 1,
    'diagCondParkingBrake_BASE': 1,
    'diagCondC1_BASE': 1,
    'drvSysActv_BASE': 1,
    'clamp15netw_BASE': 1,
    'StartUpInProgress_BASE': 1,
    'diagCondHighVoltage_BASE': 1,
    'highResolutionTotalVehDistance_BASE': 1
}

# Encode the data into a CAN message
data = message.encode(data_to_send)

# Create a CAN message object
print(message.frame_id)
can_message = can.Message(arbitration_id=message.frame_id, data=data, is_extended_id=True)

# Setup CAN interface (PCAN-USB)
can_interface = 'PCAN_USBBUS1'  # or 'PCAN_USBBUS1' or similar, depending on your system

# CAN bus configuration
bus = can.interface.Bus(channel=can_interface, bitrate=500000, bustype = 'pcan')

# Send the message
try:
    bus.send(can_message)
    print(f'Message sent on {can_interface}')
except can.CanError as e:
    print(f'Failed to send message: {e}')

# Cleanup
bus.shutdown()
