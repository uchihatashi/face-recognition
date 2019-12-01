import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)
Count,n=1,0
print("press c to capture and press q to quit")
try:
    while(True):
        k = cv2.waitKey(20)
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # Display the resulting frame
        cv2.imshow('frame',frame)
        
        if k == 99:
            print()
            if n==0:
                n = int(input("how many photo you wanna take? minimum should be * 15 *"))
                name = input("enter your name")
                path = "./images/" + name + "/"
                print(path)
                if not os.path.exists(path):
                    os.makedirs(path)
                else:
                    continues = int(input("!!!WARNING!!! \n folder already exist wanna continue yes = 1(it will replace file already exist) and No = 0(default is 0 won't cause problem)"))
                    if(continues != 0 or continues != 1):
                        continues = 0
                    if(continues != 1):
                        path = "./images/"
                        spe_letter=input("enter special letter for safety default is _") + "_"
                        name= name + spe_letter
            print(path)
            if Count <= n:
                cv2.imwrite(path + name + str(Count) +".jpg", frame)
                print("Picture " + name + str(Count) + " taken!")
                Count += 1            
            else:
                k = 0
                n = 0
                print("done thank you! press q to quit")
                
        if k & 0xFF == ord('q'):
            break

except Exception as e:
    print(str(e))

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
