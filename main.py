from bluepy import btle
import numpy as np

# Tx power of the beacon measured at 1 meter away (in dBm)
BEACON_TX_POWER = -59

# Path-loss exponent (usually between 2 and 4)
PATH_LOSS_EXPONENT = 3

scanner = btle.Scanner()

while (True):
    devices = scanner.scan(1)
    for device in devices:
        for (adtype, desc, value) in device.getScanData():
            if value.startswith("4c000215"):  # check for iBeacon prefix
                uuid_hex = value[8:40]
                uuid_str = uuid_hex[:8] + "-" + uuid_hex[8:12] + "-" + uuid_hex[12:16] + "-" + uuid_hex[16:20] + "-" + uuid_hex[20:]
                major_hex = value[40:44]
                minor_hex = value[44:48]
                major = int(major_hex, 16)
                minor = int(minor_hex, 16)
                tx_power = int(value[38:40], 16) - 256

                distance = 10 ** ((tx_power - device.rssi - (53)) / (10 * PATH_LOSS_EXPONENT))

                d = np.array([0.15, 0.30, 0.40, 0.71, 0.51, 0.94, 1.00, 1.33, 1.80, 2.10])
                r = np.array([-32, -37, -38, -51, -47, -53, -53, -55, -55, -58])

                p = np.polyfit(d, r, 1)

                # Extract the slope and intercept of the line
                slope = p[0]
                intercept = p[1]

                # Print the slope and intercept
                # print('Slope:', slope)
                # print('Intercept:', intercept)

                # print(distance)

                if major == 41564 && minor == 24860:
                    # Android
                    if device.rssi <= 50:
                        # Inside parking range
                elif major == 48201 && minor == 25382:
                    # iOS
                    if device.rssi <= 40:
                        # Inside parking range
                else:
                    # Undefined

                print("iBeacon found: UUID={}, major={}, minor={}, RSSI={} dB, distance={:.6f}\n".format(uuid_str, major, minor, device.rssi, distance))