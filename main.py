import os
import imageio

try:    
    InputFile = str(input("File name: "))
    N = int(input("Number of slices: "))
    image = imageio.imread(InputFile)
    h = len(image)
    w = len(image[0])
except FileNotFoundError:
    print("ERROR: can't open file!")
    exit()

if N > w:
    print("ERROR: N is too big! It must be in range (1," + str(w) + ")")
    exit()

if N > 1:
    new_w = int(w/N)
elif N == 1:
    new_w = w
else:
    print("ERROR: N equals or smaller than zero!")
    exit()

print("Wait, this can take some time...")

for j in range(N-1):
    image2 = [0 for i in range(0, h)]
    for row in range(0, h):
        image2[row] = [0 for i in range(0, new_w)]
        for column in range(0, new_w):
            image2[row][column] = image[row][column + new_w * j]
    imageio.imwrite(str(j+1) + '.bmp', image2)

if (w - (N-1)*new_w) > 0:
    image2 = [0 for i in range(0, h)]
    for row in range(0, h):
        image2[row] = [0 for i in range(0, w - (N-1) * new_w)]
        for column in range(0, w - (N-1) * new_w):
            image2[row][column] = image[row][column + new_w * (N-1)]
    imageio.imwrite(str(N) + '.bmp', image2)

    print("All done :)")
