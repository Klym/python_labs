# -*- coding: utf-8 -*-
import struct, os, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--source', '-s')
parser.add_argument('--dump', '-d', action = 'store_true')
parser.add_argument('--genre', '-g')

args = parser.parse_args()
        
files = os.listdir(args.source)
i = 0
for filename in files:
    if filename[-3:] != 'mp3': continue
    with open(args.source + '\\' + filename, "rb+") as f:
        i += 1
        f.seek(-128, 2)
        structure = "3s30s30s30s4s28sBBB"
        buff = f.read(struct.calcsize(structure))
        tag, name, artist, album, year, comment, zero, track, genre = struct.unpack(structure, buff)
        print artist
        print name
        print album
        print year
        print track
        print genre
        f.seek(-2, 2)
        if track == 0:
            f.write(struct.pack("B", i))
        if args.genre and genre == 255:
            f.seek(-1, 2)
            f.write(struct.pack("B", int(args.genre)))
        if args.dump:
            dump = [hex(byte) for byte in struct.unpack("128B", buff)]
            dump = map(lambda h: h[-2:] if h[-2:][0] != 'x' else '0' + h[-1:], dump)
            hexdump = ' '.join(dump)
            print(hexdump)
        print "\n"