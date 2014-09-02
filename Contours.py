import cv2
import numpy as np

def find_contour(x):

    # Find the edges
    edges = cv2.Canny(blur,x,x*2)

    # Image to draw the contours
    drawing = np.zeros(img.shape,np.uint8) 
    
    # Detect and store the contours
    contours,hierarchy = cv2.findContours   (edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    # Display the contours using different colors
    for cnt in contours:
        color = np.random.randint(0,255,(3)).tolist() # Select a random color
        cv2.drawContours(drawing,[cnt],0,color,2)
        cv2.imshow('output',drawing)
    cv2.imshow('input',img)
    
# Enter the input image file
img_name = raw_input("Enter the filename:")
img = cv2.imread(img_name)

# Apply gaussian blur to the grayscale image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
cv2.namedWindow('input',cv2.WINDOW_NORMAL)

# Set the default and max threshold value
x = 100
max_x = 255
cv2.createTrackbar('canny threshold:','input',x,max_x,find_contour)
find_contour(x)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
