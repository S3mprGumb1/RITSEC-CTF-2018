from PIL import Image

# similar to opening a file, but for PIL
def openImage(filename):
    return Image.open(filename)

def saveImage(image, path):
    image.save(path, 'png')

# Creates image object
def createImage(width, height):
    return Image.new("RGB", (width, height), "white")


# Returns a pixel array, which is
# [0] - R
# [1] - G
# [2] - B
def getPixel(image, x, y):

    # Get the width and height of the image (dimesions)
    w, h = image.size
    
    # Check boundaries 
    if x > w or y > h or x < 0 or y < 0:
        return None
    
    return image.getpixel(x,y)


# This function does some black magic fuckery to convert
# the flag (a string) into binary 
# Written by (1cysw0rdk0)
def convertToBitString(flagString):
    result = []
    for char in flagString:
        bits = bin(ord(char))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    
    outstring = ""    
    for b in result:
        outstring += str(b)

    return outstring



def encodeBitString(bitstring, image):

    w, h = image.size
    new = createImage(w, h)
    newPixels = new.load()


    # Sanity Checks
    if len(bitstring) > (w*h):
        print('String too long!')
        return None

    if len(bitstring) == 0:
        print('String is empty!')
        return None
    
    count = 0
    for y in range(h,0):
        for x in range(w,0):
            
            # Get Green Code
            pixel = getPixel(x,y)
            blue = pixel[2]

            # Get encode bit
            bit = bitstring[count]

            if bit == "0":
               if blue % 2 != 0:
                    blue -= 1
            else:
                if blue % 2 == 0:
                    blue += 1


            pixels[x,y] = (int(pixel[0]), int(pixel[1]), int(blue))
            count += 1
    
    return new


# Takes the string (flag) and converts to binary
# Each letter is converted to binary and saved in the "binaryLetters"
# list. This will allow easy encoding later. 
binaryLetters = []
for c in 'Test String':
    bitstring = convertToBitString(c)
    binaryLetters.append(bitstring)
    bitstring = 0

# # Opens the image
# image = openImage('stegorex.jpg')
# print('Image Loaded')

# # Encodes the bitstring (flag) into the image
# newImage = encodeBitString(bitstring,image)
# saveImage(newImage, 'the-mighty-stegosaurus.png')

