from myimage import *


def fillImage(oImg, fImg, onChannel):  # helper funct to fill image according to onChannel
    for x in range(fImg.size[0]):  # for row in image
        for y in range(fImg.size[1]):  # for column in image
            r, g, b, a = oImg.getpixel((x, y))  # get the current pixel
            if onChannel == (0, 0, 0):  # for CMYK
                fImg.putpixel(
                    (x, y), (255 - r, 255 - g, 255 - b, a))
            else:  # for R, G and B
                fImg.putpixel(
                    (x, y), (r*onChannel[0], g*onChannel[1], b*onChannel[2], a))
    fImg.show()  # show the result


def blow(path):
    originalImage = MyImage.open(path)  # open original image
    # create new instance with twice pixel size
    fImg = MyImage((originalImage.size[0], originalImage.size[1]), 1, 2)
    fillImage(originalImage, fImg, (1, 1, 1))  # 1,1,1 = keep all coolors same
    fillImage(originalImage, fImg, (1, 0, 0))  # 1,0,0 = keep red channel only
    # 0,1,0 = keep green channel only
    fillImage(originalImage, fImg, (0, 1, 0))
    fillImage(originalImage, fImg, (0, 0, 1))  # 0,0,1 = keep blue channel only
    fillImage(originalImage, fImg, (0, 0, 0))  # 0,0,0 = convert to CMYK


def resize(path):
    originalImage = MyImage.open(path)  # open original image
    resizedImage = MyImage(  # generate new image with twice the original size
        (originalImage.size[0] * 2, originalImage.size[1] * 2), 0, 1)

    # put all the known pixels from original image
    for x in range(originalImage.size[0]):
        for y in range(originalImage.size[1]):
            resizedImage.putpixel(
                (x * 2, y * 2), originalImage.getpixel((x, y)))

    # fill the remaining ones using provided formulae
    for x in range(resizedImage.size[0]):
        for y in range(resizedImage.size[1]):
            # if not filled in x-axis and not border pixel
            if x % 2 != 0 and x != resizedImage.size[0] - 1:
                a = resizedImage.getpixel((x - 1, y))  # get left pixel
                b = resizedImage.getpixel((x + 1, y))  # get right pixel
                resizedImage.putpixel(  # put average into the new pixel
                    (x, y), ((a[0] + b[0])//2, (a[1] + b[1])//2, (a[2] + b[2])//2, (a[3] + b[3])//2))

            # if not filled in y-axis and not border pixel
            if y % 2 != 0 and y != resizedImage.size[1] - 1:
                a = resizedImage.getpixel((x, y-1))  # get top pixel
                b = resizedImage.getpixel((x, y+1))  # get bottom pixel
                resizedImage.putpixel(  # put average into the new pixel
                    (x, y), ((a[0] + b[0])//2, (a[1] + b[1])//2, (a[2] + b[2])//2, (a[3] + b[3])//2))

            # if border x-pixel
            if x % 2 != 0 and x == resizedImage.size[0] - 1:
                resizedImage.putpixel(  # take the left pixel and put in as new pixel
                    (x, y), resizedImage.getpixel((x-1, y)))

            # if border y-pixel
            if y % 2 != 0 and y == resizedImage.size[1] - 1:
                resizedImage.putpixel(  # take the top pixel and put in as new pixel
                    (x, y), resizedImage.getpixel((x, y-1)))

    # fill the remaining centered pixels using provided formulae
    for x in range(resizedImage.size[0]):
        for y in range(resizedImage.size[1]):
            # if center pixel
            if x % 2 != 0 and y % 2 != 0 and x != resizedImage.size[0] - 1 and y != resizedImage.size[1] - 1:
                a = resizedImage.getpixel((x, y-1))  # take top pixel
                b = resizedImage.getpixel((x, y+1))  # take bottom pixel
                resizedImage.putpixel(  # put average
                    (x, y), ((a[0] + b[0])//2, (a[1] + b[1])//2, (a[2] + b[2])//2, (a[3] + b[3])//2))

    originalImage.show()  # show original image
    resizedImage.show()  # show resized image


def images_test():  # test images.py functions
    blow("images/logo.png")
    resize("images/logo.png")


images_test()
