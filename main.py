from bluepy import btle

# Tx power of the beacon measured at 1 meter away (in dBm)
BEACON_TX_POWER = -59

# Path-loss exponent (usually between 2 and 4)
PATH_LOSS_EXPONENT = 2.5

scanner = btle.Scanner()

devices = scanner.scan(2)
for device in devices:
    for (adtype, desc, value) in device.getScanData():
        if value.startswith("4c000215"):  # check for iBeacon prefix
            uuid_hex = value[8:40]
            uuid_str = uuid_hex[:8] + "-" + uuid_hex[8:12] + "-" + uuid_hex[12:16] + "-" + uuid_hex[16:20] + "-" + uuid_hex[20:]
            major_hex = value[40:44]
            minor_hex = value[44:48]
            major = int(major_hex, 16)
            minor = int(minor_hex, 16)

            distance = 10 ** ((BEACON_TX_POWER - device.rssi) / (10 * PATH_LOSS_EXPONENT))
            
            print("iBeacon found: UUID={}, major={}, minor={}, RSSI={} dB, distance={}".format(uuid_str, major, minor, device.rssi, distance))