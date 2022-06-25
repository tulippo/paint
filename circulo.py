import pyautogui as pyt
import math as m

X=600
Y=600
escala = 50
ang = 180


pyt.sleep(2)
pyt.moveTo(X,Y) #posição inicial da espiral
pyt.sleep(2)

def circulo(raio1,kx,ky):
    global X,Y,escala,ang
    n=0
    while n <= 90:
        cx = (X - escala*kx + raio1*escala*m.cos(m.radians(ang)))
        cy = (Y - escala*ky + raio1*escala*m.sin(m.radians(ang)))
        pyt.dragTo(cx,cy,button='left')
        ang+=-1
        n+=1

'''def circulodobra(raio1,kx,ky):
    global X,Y,r,ang
    n=0
    while n <= 90:
        cx = (X - 100*kx + raio1*r*m.cos(m.radians(ang)))
        cy = (Y - 100*ky + raio1*r*m.sin(m.radians(ang)))
        pyt.dragTo(cx,cy,button='left')
        ang+=-1
        n+=1
    return cx, cy'''

circulo(1,-1,0)
circulo(1,-1,0)
circulo(2,0,0)
circulo(3,0,-1)

circulo(5,-2,-1)
circulo(8,-2,2)
circulo(13,3,2)
circulo(21,3,-6)