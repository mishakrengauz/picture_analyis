import argparse
from PIL import Image, ImageDraw

brightness = int(input('brightness:'))
image = Image.open("test.jpg")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

for i in range(width):
    for j in range(height):
        a = pix[i, j][0]
        b = pix[i, j][1]
        c = pix[i, j][2]
        S = (a + b + c)
        if S > brightness:
            print(S)
print(width, height)
