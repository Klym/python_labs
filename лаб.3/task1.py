# -*- coding: utf-8 -*-
import struct, os

for root, dirs, files in os.walk(ur'D:\2015 - Younger Dreams'):
    for filename in files:
        with open(root + '\\' + filename, "rb") as f:
            size = os.path.getsize(root + '\\' + filename)
            f.seek(size - 128)
            structure = "3s30s30s30s4s28sbbb"
            dump = f.read(struct.calcsize(structure))
            tag, name, artist, album, year, comment, zero, track, genre = struct.unpack(structure, dump)
            print name.decode('cp1251')
            print artist.decode('cp1251')
            print album.decode('cp1251')
            print year
            print comment
            print zero
            print track
            print genre
            hexdump = ' '.join([hex(byte) for byte in struct.unpack("128b", dump)])
            print(hexdump + "\n")