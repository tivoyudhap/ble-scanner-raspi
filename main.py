from bluepy import btle

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
            
            print("iBeacon found: UUID={}, major={}, minor={}, RSSI={} dB".format(uuid_str, major, minor, device.rssi))

            # should submit create transaction