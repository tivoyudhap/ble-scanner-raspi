import time

from beacontools import BeaconScanner, EddystoneTLMFrame, EddystoneUIDFrame

testingList = []

def callback(bt_addr, rssi, packet, additional_info):
    testingList.append("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))
    print("<%s, %d> %s %s %s" % (bt_addr, rssi, packet, additional_info, rssi * 1.0/packet.tx_power))

# scan for all TLM frames of beacons in the namespace "12345678901234678901"
scanner = BeaconScanner(callback,
    # remove the following line to see packets from all beacons
    # device_filter=EddystoneFilter(namespace="12345678901234678901"),
    packet_filter=EddystoneUIDFrame,
    scan_parameters={"interval_ms": 100, "window_ms": 10}
)
scanner.start()
# time.sleep(10)
# print("beacon scanned : " + testingList.count)
# scanner.stop()