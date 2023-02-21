# import time

# from beacontools import BeaconScanner, EddystoneTLMFrame, EddystoneUIDFrame

# def callback(bt_addr, rssi, packet, additional_info):
#     print("<%s, %d> %s %s %s" % (bt_addr, rssi, packet, additional_info, rssi * 1.0/packet.tx_power))

# scanner = BeaconScanner(callback,
# # remove following parameter to read all beacons.
#     packet_filter=EddystoneUIDFrame,
#     scan_parameters={"interval_ms": 100, "window_ms": 10}
# )
# scanner.start()
# time.sleep(10)
# scanner.stop()

from beacon_scanner import BeaconScanner, Beacon

scanner = BeaconScanner()

def callback(bt_addr, rssi, packet, additional_info):
    beacon = Beacon(bt_addr, rssi, packet, additional_info)
    print("Beacon: {}".format(beacon))

scanner.start_scan(callback)