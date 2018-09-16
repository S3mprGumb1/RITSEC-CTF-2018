from PIL import Image






def openImage(filename):
    return Image.open(filename)

def saveImage(image, path):
    image.save(path, 'png')

def createImage(width, height):
    return Image.new("RGB", (width, height), "white")



# Returns a pixel array, which is
# [0] - R
# [1] - G
# [2] - B
def getPixel(image, x, y):

    w, h = image.size
    
    # Check boundaries 
    if x > w or y > h or x < 0 or y < 0:
        return None
    
    return image.getpixel(x,y)


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



bitstring = convertToBitString('Test String')
print('Encoding bitstring ' + bitstring)

image = openImage('stegorex.jpg')
print('Image Loaded')

newImage = encodeBitString(bitstring,image)
saveImage(newImage, 'stegorex.jpg')

