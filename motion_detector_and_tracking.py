# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:09:20 2019

@author: user
"""

import cv2
import numpy as np


def main():
    w=800
    h=600
    
    cap=cv2.VideoCapture(0)
    
    cap.set(3,w)
    cap.set(4,h)
    
    print(cap.get(3))
    print(cap.get(4))
    
    if cap.isOpened():
       ret,frame = cap.read()
    else:
        ret=False
        
    ret,frame1 = cap.read()
    ret,frame2 = cap.read()
        
    while ret:
        d=cv2.absdiff(frame1,frame2)#motion is change in frame
        
        grey=cv2.cvtColor(d,cv2.COLOR_BGR2GRAY)
        
        blur = cv2.GaussianBlur(grey,(5,5),0)#applying gaussian blur which will blur the iamge and  secod parameter is
        #is kernel size (5*5) matrix
        
        ret,th=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)#thresholding needed to find contours

        dilated = cv2.dilate(th,np.ones((3,3),np.uint8),iterations=15)#morphological operation dilation
        #2nd arg is kernel
        eroded=cv2.erode(dilated,np.ones((3,3),np.uint8),iterations=15)
        contours,hierarchy=cv2.findContours(eroded,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        cv2.drawContours(frame1,contours,-1,(0,255,0),2)#on which frameto draw contour
        cv2.imshow("Original",frame2)
        cv2.imshow("Intermediate",frame1)
        if cv2.waitKey(1)==27: #exit on Esc
            break
        
        frame1=frame2
        ret,frame2  = cap.read()#frame2 is original frame
        
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ =="__main__":
    main()
    
    
    
    
    
    
    
    
    
    
   
