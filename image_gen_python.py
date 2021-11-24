import libjpeg
import numpy
import zlib
import PIL
import sys

from PIL import Image


img = Image.open(sys.argv[1])

img.thumbnail((115,115))


pixels = img.load()
print(pixels[0,0])
brightness_matrix = [[0 for h in range(0, img.size[1])] for w in range(0, img.size[0])]
for y in range(0,img.size[1]):
    for x in range(0, img.size[0]):
        r,g,b = pixels[x,y] 
        brightness = int((r*0.2126)+(g*0.7152)+(b*0.0722))
        
        brightness_matrix[x][y] = brightness


ascii_matrix = [['' for h in range(0, img.size[1])] for w in range(0, img.size[0])]
ascii_str = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
for y in range(0,img.size[1]):
    for x in range(0,img.size[0]):
        ascii_pos = int((brightness_matrix[x][y]/255)*len(ascii_str))
        ascii_matrix[x][y] = ascii_str[ascii_pos-1]

for y in range(0,img.size[1]):
    for x in range(0, img.size[0]):
        print ((ascii_matrix[x][y])*2, end='')
    print()

