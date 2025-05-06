import cv2
import numpy as np

# Load the image
image = cv2.imread(r'c:\Users\Dell\Pictures\Screenshots\colordetectionimg.jpg')

# Resize the image
image = cv2.resize(image, (500, 500))

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#Blue Color Detection
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])
blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
blue_result = cv2.bitwise_and(image, image, mask=blue_mask)

#Red Color Detection in both regions
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])
mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)
red_result = cv2.bitwise_and(image, image, mask=red_mask)

#Green Color Detection
lower_green = np.array([40, 70, 70])
upper_green = np.array([80, 255, 255])
green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
green_result = cv2.bitwise_and(image, image, mask=green_mask)

# Display all results
cv2.imshow("Original Image", image)
cv2.imshow("Blue Mask", blue_mask)
cv2.imshow("Detected Blue Color", blue_result)
cv2.imshow("Red Mask", red_mask)
cv2.imshow("Detected Red Color", red_result)
cv2.imshow("Green Mask", green_mask)
cv2.imshow("Detected Green Color", green_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
