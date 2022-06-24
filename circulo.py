import numpy as np
import pyautogui as pyt
import math as m
X=960
Y=540
M = 1000

pyt.sleep(2)
pyt.moveTo(X,Y)
pyt.dragTo(X,Y+100)
pyt.sleep(2)
pyt.moveTo(X,Y)
pyt.dragTo(X+100,Y)
pyt.sleep(2)

angle = np.exp(1j *2 *np.pi/M)
angles = np.cumprod(np.ones(M+1)*angle)
x = np.real(angles)
y = np.imag(angles)
pyt.dragTo(X+ 30*x, Y + 30*y)

count = 1
somax = 0
somay = 0


#while count <= 90:
#    xf = 90+somax
#    yf = 0+somay
#    xf = xi + xf
#    yf = yi + yf
#    pyt.moveTo(xi,yi)
#    pyt.dragTo(xf,yf, button='left')
#    count+=1
#    somax+=-2
#    somay+=1.15
    