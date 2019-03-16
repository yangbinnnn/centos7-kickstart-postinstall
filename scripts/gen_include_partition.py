import sys


# Partition clearing information
# Using only primary disk, ignoring others

dev = sys.argv[1]
include_path = sys.argv[2]

include = """bootloader --location=mbr --boot-drive=%s
ignoredisk --only-use=%s
clearpart --all  --drives=%s --initlabel
# Disk partitioning information
part / --fstype="ext4" --grow --size=1
part swap --fstype="swap" --size=2048\n""" % (dev, dev, dev)

open(include_path, "wb").write(include)
