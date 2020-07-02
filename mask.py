import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import openpyxl
image = mpimg.imread('C:\\Users\\becke\OneDrive\Desktop\Documents\Intro Autonomous Driving\Image Mask\car_green_screen.jpg')
background_image = mpimg.imread('C:\\Users\\becke\OneDrive\Desktop\Documents\Intro Autonomous Driving\Image Mask\sky.jpg')
lower_green = np.array([0,180,0]) #green filter lower boundry using RGB
upper_green = np.array([100,255,100]) #green filter upper boundry using RGB
mask = cv2.inRange(image, lower_green, upper_green) #inRange function reduces each color pixel from three values [r,g,b] down to a single value-if in the filter range then value set to 255(white) otherwise set to 0(black)
#after the inRange function a green pixel is set to 255 and all other pixels (i.e., the car) are set to 0
masked_image = np.copy(image) #makes a copy of car_green_screen.jpg
masked_image[mask != 0] = [0, 0, 0] #if the pixel value in mask is 255, then change that pixel to [0,0,0]-black. The masked image will now be the car on a black background
completed_image = np.copy(background_image) #makes a copy of sky.jpg
completed_image = completed_image[0:450, 0:660] #crops completed_image to 450x660
for row in range (1, 450):
    for column in range (1, 660):
        if masked_image[row][column][0] == 0 and masked_image[row][column][1] == 0 and masked_image[row][column][2] == 0: #checks if each rgb pixel is black, i.e. [0,0,0]
            completed_image[row][column] = background_image[row][column] #if the pixel from masked_image is black then change pixel value to the value from sky.jpg
        else:
            completed_image[row][column] = masked_image[row][column] #if the masked image is not black then change the pixel value to the value of the red car
plt.imshow(completed_image)
plt.show()

"""
Helpful commands:
plt.imshow(mask, cmap='gray') #set cmap to grey to view image in b&w
print('Car image dimensions:', image.shape,'Image type is',image.dtype)
print('Masked image dimensions:', masked_image.shape,'Image type is',masked_image.dtype
print(masked_image[250][400][2]) #this allows you to see the r,g,b values for a particular pixel
"""