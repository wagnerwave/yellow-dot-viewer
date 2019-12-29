#!/usr/bin/env python3

from PIL import Image
import sys

if len(sys.argv) < 2:
    print("Error:")
    print("./main.py image.png")
    exit()
    
name = sys.argv[1]

Image.open(name).split()[2].show()
blue = Image.open(name).split()[2]
blue.point(lambda x: (256-x)**2).show()
