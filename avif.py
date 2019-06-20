#!/usr/bin/env python
import struct
import sys

def _parse_chunk(chunk):
    print(f"Chunk size: {len(chunk)}")
    box_type, *_ = struct.unpack("4s", chunk[:4])
    print(f"Box type: {box_type.decode()}")

def _parse_content(avif_content):
    """Parse an avif content."""
    offset = 0
    while (offset + 4) <= len(avif_content):
        chunksize, *_ = struct.unpack(">L", avif_content[offset:offset+4])
        print(f"Chunksize = {chunksize}")
        
        # For now we simply exit the loop if the 
        # file seems malformed
        if offset + chunksize > len(avif_content):
            break
        
        _parse_chunk(avif_content[offset+4:offset+chunksize])

        offset += chunksize
    if offset != len(avif_content):
        print("[!] avif file seems malformed.")


def parse(avif_file):
    """Parse an avif file."""
    with open(avif_file, "rb") as stream:
        content = stream.read()
        _parse_content(content)


def main(argv):
    if len(argv) < 2:
        print(f"Usage: {argv[0]} <avif_file>")
        raise SystemExit(-1)
    avif_filename = argv[1]
    parse(avif_filename)

if __name__ == "__main__":
        main(sys.argv)