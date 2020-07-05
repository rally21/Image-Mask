#in this program the green background (car_green_screen2.jpg) is not a consistent shade of green
#this program looks at the h value and builds a mask, h=[0,0,0], if h is between 35 and 65
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import openpyxl
image = mpimg.imread('C:\\Users\\becke\OneDrive\Desktop\Documents\Intro Autonomous Driving\Image Mask\car_green_screen2.jpg')
background_image = mpimg.imread('C:\\Users\\becke\OneDrive\Desktop\Documents\Intro Autonomous Driving\Image Mask\sky.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]
masked_image = np.copy(image)
completed_image = np.copy(background_image) #makes a copy of sky.jpg
completed_image = completed_image[0:450, 0:660] #crops completed_image to 450x660
for a in range (0, len(h)):
    for b in range (0, len(h[:][0])):
        if h[a][b] <= 65 and h[a][b] >= 35:
            masked_image[a][b] = [0,0,0]
for row in range (1, len(h)):
    for column in range (1, len(h[:][0])):
        if masked_image[row][column][0] == 0 and masked_image[row][column][1] == 0 and masked_image[row][column][2] == 0: #checks if each rgb pixel is black, i.e. [0,0,0]
            completed_image[row][column] = background_image[row][column] #if the pixel from masked_image is black then change pixel value to the value from sky.jpg
        else:
            completed_image[row][column] = masked_image[row][column] #if the masked image is not black then change the pixel value to the value of the red car
plt.imshow(completed_image)
plt.show()
#Helpful commands:
#plt.imshow(mask, cmap='gray') #set cmap to grey to view image in b&w
#print('Car image dimensions:', image.shape,'Image type is',image.dtype)
#print('Masked image dimensions:', masked_image.shape,'Image type is',masked_image.dtype
#print(masked_image[250][400][2]) #this allows you to see the r,g,b values for a particular pixel