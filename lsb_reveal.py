#!/usr/bin/env python
from typing import List
import sys

from PIL import Image


def _reveal(picture_file: str) -> None:
    """Private."""
    image = Image.open(picture_file)
    width, height = image.size
    new_image = Image.new("RGBA", (width, height))
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            new_pixel = (
                (pixel[0] & 1) * 255,
                (pixel[1] & 1) * 255,
                (pixel[2] & 1) * 255,
                pixel[3]  # alpha channel, leave as is
            )
            new_image.putpixel((x, y), new_pixel)
    new_image.save(f"{picture_file}.out.png", "PNG")


def main(argv: List[str]) -> None:
    """Reveal least significant bytes from a picture file."""
    if len(argv) < 2:
        print(f"Usage: {argv[0]} <picture file>")
        raise SystemExit(-1)
    picture_file = argv[1]
    _reveal(picture_file)

if __name__ == "__main__":
    main(sys.argv)