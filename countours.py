import numpy as np 
import cv2

im1 = cv2.imread('formula_images/7536c9eef2.png')
def BoundingBoxes(im1, area_thresh = 20):
    boxes = []
    im = cv2.GaussianBlur(im1,(5,5),0)
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray,127,255,0)
    thresh = cv2.bitwise_not(thresh)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(im, contours, -1, (0,255,0), 1)
    for c in contours:
        # get the bounding rect
        x, y, w, h = cv2.boundingRect(c)
        area = w*h
        if area < area_thresh:
            continue
        boxes.append((x,y,w,h))
        # draw a green rectangle to visualize the bounding rect
        cv2.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0), 1)
    return im, boxes

while cv2.waitKey(1) != ord('q'):
    im, _ = BoundingBoxes(im1)
    cv2.imshow('img',im)
cv2.destroyAllWindows() 
