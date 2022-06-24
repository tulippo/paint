import pyautogui as pyt
import math as m

X=960
Y=540
n=0
r = 103
ang = 0


pyt.sleep(2)
pyt.moveTo(X,Y)
pyt.dragTo(X,Y+100,button='left')
pyt.sleep(2)
pyt.moveTo(X,Y)
pyt.dragTo(X+100,Y,button='left')
pyt.sleep(2)

#c1 = Circle(Point(X,Y),100)
#print(c1.equation())

while n <= 90:
    cx = X + r*m.cos(m.radians(ang))
    cy = Y + r*m.sin(m.radians(ang))
    pyt.dragTo(cx,cy,button='left')
    ang+=1
    n+=1
