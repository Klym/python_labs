# -*- coding: utf-8 -*-
import struct, os, getopt, sys

opts, args = getopt.getopt(sys.argv[1:], "d", [])
toDump = False

for key, val in opts:
    if key == "-d":
        toDump = True
        
for root, dirs, files in os.walk(ur'D:\2015 - Younger Dreams'):
    for filename in files:
        with open(root + '\\' + filename, "rb") as f:
            size = os.path.getsize(root + '\\' + filename)
            sound = f.read(size - 128)
            structure = "3s30s30s30s4s28sBBB"
            buff = f.read(struct.calcsize(structure))
            tag, name, artist, album, year, comment, zero, track, genre = struct.unpack(structure, buff)
            print artist
            print name
            print album
            print year
            if toDump:
                dump = [hex(byte) for byte in struct.unpack("128B", buff)]
                dump = map(lambda h: h[-2:] if h[-2:][0] != 'x' else '0' + h[-1:], dump)
                hexdump = ' '.join(dump)
                print(hexdump)
            print "\n"