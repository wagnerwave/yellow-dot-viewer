#!/usr/bin/env python3

from PIL import Image

Image.open("ch18.png").split()[2].show()
blue = Image.open("ch18.png").split()[2]
blue.point(lambda x: (256-x)**2).show()
