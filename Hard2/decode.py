from PIL import Image

def decodeImage():

    image = Image.open('test.jpg')
    for color in image.getdata(2):
        print(chr(color))


if __name__ == '__main__':
    decodeImage()