import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import openpyxl
#wb1 = openpyxl.load_workbook('mask.xlsx')
#sheet1 = wb1.get_sheet_by_name('masked_image')
image = mpimg.imread('C:\\Users\\becke\OneDrive\Desktop\Documents\Intro Autonomous Driving\Image Mask\car_green_screen.jpg')
background_image = mpimg.imread('C:\\Users\\becke\OneDrive\Desktop\Documents\Intro Autonomous Driving\Image Mask\sky.jpg')
lower_green = np.array([0,180,0])
upper_green = np.array([100,255,100])
mask = cv2.inRange(image, lower_green, upper_green)
masked_image = np.copy(image)
masked_image[mask != 0] = [0, 0, 0]
"""
for a in range (1, 450):
    for b in range (1, 660):
        sheet1.cell(row=a, column=b).value=str(masked_image[a][b])
wb1.save('mask.xlsx')
"""
#print('Car image dimensions:', image.shape,'Image type is',image.dtype)
#print('Masked image dimensions:', masked_image.shape,'Image type is',masked_image.dtype)
#plt.imshow(mask, cmap='gray')
#plt.imshow(masked_image)
## TODO: Crop it or resize the background to be the right size (450x660)
# Hint: Make sure the dimensions are in the correct order!

## TODO: Mask the cropped background so that the car area is blocked
# Hint: mask the opposite area of the previous image
completed_image = np.copy(background_image)
completed_image = completed_image[0:450, 0:660]
#plt.imshow(background_image)
#plt.show()
#crop_background[mask == 0] = [0, 0, 0]
## TODO: Display the background and make sure 

## TODO: Add the two images together to create a complete image!

zero_count = 0
not_zero_count = 0

for row in range (1, 450):
    for column in range (1, 660):
        if masked_image[row][column][0] == 0 and masked_image[row][column][1] == 0 and masked_image[row][column][2] == 0:
            zero_count = zero_count + 1
            completed_image[row][column] = background_image[row][column]
        else:
            not_zero_count = not_zero_count + 1
            completed_image[row][column] = masked_image[row][column]

print('zero count is',zero_count)
print('not zero count is',not_zero_count)
plt.imshow(completed_image)
plt.show()
#wb1.save('mask.xlsx')
#print(masked_image[250][400][2])
"""
for a in range (1, 450):
    for b in range (1, 660):
        if masked_image[a][b][0] + masked_image[a][b][1] + masked_image[a][b][2] == 0:
            zero_count = zero_count + 1
        if masked_image[a][b][0] + masked_image[a][b][1] + masked_image[a][b][2] != 0:
            not_zero_count = not_zero_count + 1
print('There were',zero_count,'zero pixels and',not_zero_count,'not zero pixels out of a total of',zero_count + not_zero_count,'pixels')
"""
#plt.show()