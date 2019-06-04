
'''Driver Alertness System
EDD C1 Group 4
Archit Harsh Piyush Rewa Pratiksha Hushar
'''

import numpy as np
import cv2
import pygame

fc=0
ec=0
#0 is camera index
cap = cv2.VideoCapture(0)     
#Special feature of cv2 library        
while(True):                          
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    
    
    #It return true if camera is functioning properly
    ret, frame = cap.read()
    
    
    

    
    
    #Detects the face
    face = face_cascade.detectMultiScale(frame, 1.3, 5)  
    # dimensions for box
    for (x,y,w,h) in face:                               
        cv2.rectangle(frame,(x,y),(x+w,y+h),(120,120,0),2)
        fc=fc+1
        roi_gray = frame[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        f2=frame[y:y+h,x:x+w]
        cv2.imshow('arc',f2)
        
        
        
        
        
        # dimensions for box for eyes
        for (ex,ey,ew,eh) in eyes:                    
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            ec=ec+0.5
            f3=f2[ey:ey+eh,ex:ex+ew]
           

            cv2.imshow('archit',f3)
            
        
            
            
            
        


    cv2.imshow('frame',frame)
    
    
     #quitting button 'q'
    if cv2.waitKey(20) & 0xFF == ord('q'):           
        break
    print('Face time',fc,'eyes time',ec,'\n','difference',fc-ec)
    if(fc-ec)>7 and fc!=ec:
        pygame.init()
        
        print(fc-ec,"Wake Up")
        s = pygame.mixer.Sound('beep-02.wav')  
        s.play()
        s.play()
        fc=0
        ec=0
        
        
        
        
#Releases the capture
cap.release()                                          
cv2.destroyAllWindows()

    
