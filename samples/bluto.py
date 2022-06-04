# simple inquiry example
import bluetooth_mesh

nearby_devices = bluetooth_mesh.discover(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))