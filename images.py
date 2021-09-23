from myimage import *


def fillImage(oImg, fImg, onChannel):
    for x in range(fImg.size[0]):
        for y in range(fImg.size[1]):
            r, g, b, a = oImg.getpixel((x, y))
            if onChannel == (0, 0, 0):
                fImg.putpixel(
                    (x, y), (255 - r, 255 - g, 255 - b, a))
            else:
                fImg.putpixel(
                    (x, y), (r*onChannel[0], g*onChannel[1], b*onChannel[2], a))
    fImg.show()


def blow(path):
    originalImage = MyImage.open(path)
    fImg = MyImage((originalImage.size[0], originalImage.size[1]), 1, 2)
    fillImage(originalImage, fImg, (1, 1, 1))
    fillImage(originalImage, fImg, (1, 0, 0))
    fillImage(originalImage, fImg, (0, 1, 0))
    fillImage(originalImage, fImg, (0, 0, 1))
    fillImage(originalImage, fImg, (0, 0, 0))


def resize(path):
    originalImage = MyImage.open(path)
    resizedImage = MyImage(
        (originalImage.size[0] * 2, originalImage.size[1] * 2), 0, 1)

    for x in range(originalImage.size[0]):
        for y in range(originalImage.size[1]):
            resizedImage.putpixel(
                (x * 2, y * 2), originalImage.getpixel((x, y)))

    for x in range(resizedImage.size[0]):
        for y in range(resizedImage.size[1]):
            if x % 2 != 0 and x != resizedImage.size[0] - 1:
                a = resizedImage.getpixel((x - 1, y))
                b = resizedImage.getpixel((x + 1, y))
                resizedImage.putpixel(
                    (x, y), ((a[0] + b[0])//2, (a[1] + b[1])//2, (a[2] + b[2])//2, (a[3] + b[3])//2))

            if y % 2 != 0 and y != resizedImage.size[1] - 1:
                a = resizedImage.getpixel((x, y-1))
                b = resizedImage.getpixel((x, y+1))
                resizedImage.putpixel(
                    (x, y), ((a[0] + b[0])//2, (a[1] + b[1])//2, (a[2] + b[2])//2, (a[3] + b[3])//2))

            if x % 2 != 0 and x == resizedImage.size[0] - 1:
                a = resizedImage.getpixel((x-1, y))
                resizedImage.putpixel(
                    (x, y), (a[0]//2, a[1]//2, a[2]//2, a[3]//2))

            if y % 2 != 0 and y == resizedImage.size[1] - 1:
                a = resizedImage.getpixel((x, y-1))
                resizedImage.putpixel(
                    (x, y), (a[0]//2, a[1]//2, a[2]//2, a[3]//2))

    for x in range(resizedImage.size[0]):
        for y in range(resizedImage.size[1]):
            if x % 2 != 0 and y % 2 != 0 and x != resizedImage.size[0] - 1 and y != resizedImage.size[1] - 1:
                a = resizedImage.getpixel((x, y-1))
                b = resizedImage.getpixel((x, y+1))
                resizedImage.putpixel(
                    (x, y), ((a[0] + b[0])//2, (a[1] + b[1])//2, (a[2] + b[2])//2, (a[3] + b[3])//2))

    originalImage.show()
    resizedImage.show()


# xres, yres = 4, 3
# grid_width = 0
# pixel_size = 100
# mode = 'RGBA'
# img = MyImage((xres, yres), grid_width, pixel_size, mode)
# # Fill image pixels: black at origin, increasing red in x-direction and
# # increasing green in y- direction.
# for x in range(img.size[0]):
#     for y in range(img.size[1]):
#         img.putpixel((x, y), (255 * x // xres, 255 * y // yres, 0, 255))
# img.img.save("save.png")

# blow("images/logo.png")
# resize("images/logo.png")
