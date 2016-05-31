# -*- coding: utf-8 -*-
import struct, os

f = open(ur"D:\WebServers\home\flame-zona.ru\www\bs_pleer\Clear_Skies.mp3", "rb")
size = os.path.getsize(ur"D:\WebServers\home\flame-zona.ru\www\bs_pleer\Clear_Skies.mp3")
f.seek(size - 128)

structure = "3s30s30s30s4s28sbbb"
dump = f.read(struct.calcsize(structure))
tag, name, artist, album, year, comment, zero, track, genre = struct.unpack(structure, dump)
print tag
print name.decode('cp1251')
print artist.decode('cp1251')
print album.decode('cp1251')
print year
print comment
print zero
print track
print genre

hexdump = ' '.join([hex(byte) for byte in struct.unpack("128b", dump)])
print(hexdump)

f.close()