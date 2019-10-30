#!/usr/bin/env python3

from PIL import Image

name = XXX # remplace the XXX by your file

Image.open(name).split()[2].show()
blue = Image.open(name).split()[2]
blue.point(lambda x: (256-x)**2).show()
