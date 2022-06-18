import pyautogui
#pyautogui.press('winleft')
#pyautogui.sleep(3)
#pyautogui.write('paint')
#pyautogui.sleep(5)
#pyautogui.press('enter')

##pyautogui.moveTo(140, 379)
##pyautogui.dragTo(1092, 827, button='left')
##952, 448
##476, 224
##1,6180
def clicar():
    pyautogui.moveTo(1500,450)
    pyautogui.click(button='left')

f20 = 20*1.6180
f = 1.6180
x = 600
y = 600
t = 1
pyautogui.moveTo(x, y)
pyautogui.sleep(t)
pyautogui.dragTo(x+f20, y+20, button='left')
clicar()

pyautogui.moveTo(x, y+20)
pyautogui.sleep(t)
pyautogui.dragTo(x+f20, y+20+f20, button='left')
clicar()

pyautogui.moveTo(x+f20, y+20+f20)
pyautogui.sleep(t)
pyautogui.dragTo(x+20+2*f20, y, button='left')
clicar()

pyautogui.moveTo(x+20+2*f20, y)
pyautogui.sleep(t)
pyautogui.dragTo(x, y-20-2*f20, button='left')
clicar()

pyautogui.moveTo(x, y-20-2*f20)
pyautogui.sleep(t)
pyautogui.dragTo(x-70-2*f20, y+20+f20, button='left')
clicar()

pyautogui.moveTo(x-70-2*f20, y+20+f20)
pyautogui.sleep(t)
pyautogui.dragTo(x+20+2*f20, y+200+2*f20, button='left')
clicar()

pyautogui.moveTo(x+20+2*f20, y+200+2*f20)
pyautogui.sleep(t)
pyautogui.dragTo(x+320+2*f20, y-20-2*f20, button='left')
clicar()



