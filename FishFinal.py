# Ma. Lora Drizella Ong = Lab 8 -FishTank

import random, time


def addCircleFilled (Canvas, Xc, Yc, R, NewColor):
    addOvalFilled(Canvas, Xc-R, Yc-R, 2*R+1, 2*R+1, NewColor)
    return

def addEllipseFilled(Canvas,Xc,Yc,Xr,Yr,NewColor):
 addOvalFilled(Canvas,Xc-Xr,Yc-Yr,2*Xr+1,2*Yr+1,NewColor)
 return

def FishLeft (Canvas,Xc,Yc,NewColor):
 addEllipseFilled(Canvas,Xc+14,Yc,3,14,white) # Tail
 addEllipseFilled(Canvas,Xc,Yc,17,9,NewColor) # Body
 addCircleFilled(Canvas,Xc-10,Yc-2,3,white) # Eye
 addLine(Canvas,Xc-16,Yc+4,Xc-7,Yc+4,white) # Mouth
 return

def FishRight (Canvas,Xc,Yc,NewColor):
 addEllipseFilled(Canvas,Xc-14,Yc,3,14,white) # Tail
 addEllipseFilled(Canvas,Xc,Yc,17,9,NewColor) # Body
 addCircleFilled(Canvas,Xc+10,Yc-2,3,white) # Eye
 addLine(Canvas,Xc+16,Yc+4,Xc+7,Yc+4,white) # Mouth
 return 

def FishTank(Canvas):
     TotalFish = 20
     X=[getWidth (Canvas)/2 + random.randrange(-25, +26)for Fish2 in range (TotalFish)]
     Y=[getHeight(Canvas)/2+ random.randrange(-25, +26)for Fish2 in range (TotalFish)]
     Xd=[random.randrange(-1,+2)for Fish2 in range (TotalFish)]
     Yd=[random.randrange (-1, +2)for Fish2 in range (TotalFish)] 
     C= [random.choice([black, blue, green, cyan, red, magenta, yellow]) for Color in range (TotalFish)]
     
     
     while (True):
         setAllPixelsToAColor(Canvas,makeColor(0,0,128))
         show(Canvas)
         for Fish in range (TotalFish):
             
             if (Xd[Fish]== -1):
                 FishLeft(Canvas,X[Fish],Y[Fish],C[Fish])
                 X[Fish]=X[Fish]+Xd[Fish]
                 Y[Fish]=Y[Fish]+Yd[Fish]
             else:
                 FishRight(Canvas, X[Fish], Y[Fish], C[Fish])
                 X[Fish]=X[Fish]+Xd[Fish]
                 Y[Fish]=Y[Fish]+Yd[Fish]
         
             if (X[Fish]+Xd[Fish]<0) or (X[Fish]+Xd[Fish] > getWidth(Canvas)-1):
                 Xd[Fish]=-Xd[Fish]
             if (Y[Fish] +Yd[Fish]<0) or (Y[Fish]+Yd[Fish] > getHeight(Canvas)-1):
                 Yd[Fish]= -Yd[Fish]
                 
             DiffX=random.randrange(10)
             DiffY=random.randrange(20)
             if (DiffX==0): Xd[Fish]=random.randrange(-1,+2)
             if (DiffY==0): Yd[Fish]=random.randrange (-1,+2)
         
         repaint(Canvas)
         time.sleep(0.05)
         
     return    
         
             
def Run():
 FishTank(makeEmptyPicture(640,480))
 return 