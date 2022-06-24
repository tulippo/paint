import pyautogui as pyt
import math as m

X=600
Y=600
r = 100
ang = 180
cx = 0
cy = 0


pyt.sleep(2)
pyt.moveTo(X,Y)
pyt.dragTo(X,Y+100,button='left')
pyt.sleep(2)
pyt.moveTo(X+100,Y)
pyt.sleep(2)

def circulo(raio1):
    global X,Y,r,ang
    n=0
    while n <= 90:
        cx = (X+100 + raio1*r*m.cos(m.radians(ang)))
        cy = (Y + raio1*r*m.sin(m.radians(ang)))
        pyt.dragTo(cx,cy,button='left')
        ang+=-1
        n+=1
    return cx, cy, ang

def circulodobra(raio1,ang,angulagem):
    global X,Y,r
    n=0
    while n <= 90:
        cx = (X + raio1*r*m.cos(m.radians(ang)))
        cy = (Y - 100+ raio1*r*m.sin(m.radians(ang)))
        pyt.dragTo(cx,cy,button='left')
        ang+=1*angulagem
        n+=1
    return cx, cy, ang

circulo(1)
circulo(1)
circulodobra(2,0,-1)
circulodobra(3,90,1)