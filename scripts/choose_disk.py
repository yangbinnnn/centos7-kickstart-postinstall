# -*- coding: utf-8 -*-
import os


# User Capacity:    63,023,063,040 bytes [63.0 GB]
# Device Model or Product and User Capacity
def get_disk_info(dev):
    model = ""
    size = 0
    for line in os.popen("smartctl -i %s" % dev).readlines():
        line = line.strip()
        if not line:
            continue
        if not size and line.startswith("User Capacity"):
            idx = line.index("[")
            if idx != -1:
                size = line[idx:].replace(" ", "")[1:-1]
        if not model and line.startswith("Device Model"):
            items = line.split(":")
            if len(items) != 2:
                continue
            model = items[1].strip()
        if not model and line.startswith("Product"):
            items = line.split(":")
            if len(items) != 2:
                continue
            model = items[1].strip()
    return "[%s - %s]" % (model, size)


disk_set = set()
_disks = os.popen("smartctl --scan").readlines()
for _disk in _disks:
    if not _disk:
        continue
    dev = _disk.strip().split()[0]
    disk_set.add(dev)

DISK = []
for dev in sorted(disk_set):
    info = get_disk_info(dev)
    idx = dev.rindex("/")
    if idx == -1:
        continue
    DISK.append((dev[idx+1:], info))


def whiptail_radio():
    cmd_start = 'whiptail --radiolist "Choose a disk" 25 50 8'
    options = []
    for n, disk in enumerate(DISK):
        is_on = "ON" if n == 0 else "OFF"
        option = '"%s" "%s" %s' % (disk[0], disk[1], is_on)
        options.append(option)
    cmd_end = '3>&1 1>&2 2>&3'
    return cmd_start + " " + " ".join(options) + " " + cmd_end


print os.popen(whiptail_radio()).read()
