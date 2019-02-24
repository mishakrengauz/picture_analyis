import argparse
from PIL import Image, ImageDraw
def main():
    parser = argparse.ArgumentParser(description='Image processing.')
    parser.add_argument('-b','--brightness', help='Minimal brightness', required = True)
    args = parser.parse_args()
    image = Image.open("test.jpg")
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    pixels = []

    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a*0.3 + b*0.59 + c*0.11)
            if S > int(args.brightness):

                pixels.append(S)
    with open("pixels.txt", 'w+') as f:
        f.write(str(pixels))
        f.write('Image size: ')
        f.write(str(width))
        f.write(' ')
        f.write(str(height))

if __name__ == '__main__':
    main()