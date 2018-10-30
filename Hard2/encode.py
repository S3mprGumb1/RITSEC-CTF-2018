# Authors:  Shadow5229  1cysw0rdk0
# File: encode.py
# 
# This file takes a string and will encode it into an RGB formatted image.
# It does this by taking the ORD value of each character and setting them
# as one of the RGB values (code replaces BLUE value) with the new value.
#
# Created for RITSEC CTF2018

from PIL import Image



def changeImage():
    # open the image you want to encode data to
    image = Image.open('spielberg_dino_c.jpg')
    
    # This the string that will be encoded into the image
    flag = 'This_wilL_be_the_flag'

    # a list to hold the tuples of pixels for the new image
    newImageData = []

    # count for looping around 
    count = 0

    # COLOR is a tuple of RGB value data for each pixel
    for color in image.getdata():

        # creates a new RGB tuple with the ord value of the char from the flag string
        newPixel = (color[0], color[1], ord(flag[count]))
        
        # Appends the tuple to the list
        newImageData.append(newPixel)

        # used for wrapping back around the flag
        count += 1
        if count == len(flag):
            count = 0

    # creates a new IMAGE object with the same mode and size as the original
    newImage = Image.new(image.mode, image.size)
    
    # Copies pixel data to the image
    newImage.putdata(newImageData)

    # Writes new image to disk
    newImage.save('test.jpg')

changeImage()