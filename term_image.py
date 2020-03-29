from __future__ import print_function
import cv2 
image = cv2.imread('ironman.jpg') 
#cv2.imshow('Original', image) 
#cv2.waitKey() 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
#cv2.imshow('Grayscale', gray_image) 
#cv2.waitKey(0)   
(thresh, bw_image) = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#cv2.imshow('Black-and-White', bw_image) 
#cv2.waitKey(0) 
resized_dimension=(100,46)
resized_bw_image = cv2.resize(bw_image, resized_dimension, interpolation = cv2.INTER_AREA)

cv2.imshow('Black-and-White-Resized', resized_bw_image) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 


#thresh=127
#im_bw = cv2.threshold(gray_image, thresh, 255, cv2.THRESH_BINARY)[1]
#cv2.imshow('Black-and-White', im_bw) 
#cv2.waitKey(0)

#for i in range(100):
#	for j in range(100): 

#printing the final image using 0 and 1
for i in range(resized_dimension[1]):
	for j in range(resized_dimension[0]):
		if(j<(resized_dimension[0]-1)):
			if (resized_bw_image[i][j]<128):
				print("1",end="")
			elif(resized_bw_image[i][j]>127):
				print(" ",end="")
		if(j==(resized_dimension[0]-1)):
			if (resized_bw_image[i][j]<128):
				print("1",end="\n")
			elif(resized_bw_image[i][j]>127):
				print(" ",end="\n")


