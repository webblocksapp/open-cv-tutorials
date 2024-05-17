import cv2


img = cv2.imread('assets/logo.png')

#Image is represented in a numpy array when it's read
print(img)

#Prints number of rows (height), columns (width) and color channels channels of the image
print(img.shape)

'''
[
    [
        [0,0,0], [255,255,255], [0,0,0] //Column (The column contains the color channels)
    ], // Row
    [   
        [0,0,0], [255,255,255], [0,0,0]
    ]
]
'''

# How to red color channels in cv2
'''
blue, green, red (BGR)
[0,   0,     0]
'''

# Manipulate colors of an image: