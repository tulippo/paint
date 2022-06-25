import pyautogui
def clicar():
    pyautogui.moveTo(1500,450)
    pyautogui.click(button='left')
'''x = 616
y = 603

n = int(input("valor de n: "))
t1 = 0
t2 = 1
t3 = 0
count = 1
pyautogui.sleep(0)

while count <= n:
    pyautogui.moveTo(x, y)
    print(t1)
    x = x + t3*10
    y = y + t3*10
    pyautogui.sleep(2)
    pyautogui.dragTo(x, y, button='left')
    clicar()

    t3 = t1 + t2
    t1 = t2
    t2 = t3
    count+= 1'''

pyautogui.sleep(5)
print(pyautogui.position())
clicar()

