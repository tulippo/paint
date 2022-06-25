# importando as bibliotecas a serem trabalhadas conjunto ao código.
import pyautogui
import math as m

# 1ªfunção: clique fora do desenho para tirar a seleção do desenho, se for no paint.
def clicar():
    pyautogui.moveTo(600,900)
    pyautogui.click(button='left')

# 2ªfunção: move o mouse para o ponto inicial a ser desenhado, de acordo com a escala (em pixel)
## e cria os novos valores de x e y conforme a sequência de fibonacci.
def posicao_inicial(s1,s2):
    global x,y,escala
    pyautogui.moveTo(x,y)

    print(termo1)
    x = x + termo1*escala*s1
    y = y + termo1*escala*s2
    return x,y

# 3ªfunção: move o mouse para os novos valores de x e y.
def move():
    global x,y
    pyautogui.sleep(1)
    pyautogui.dragTo(x, y, button='left')
    clicar()

# 4ªfunção: calcula os termos da sequência de fibonacci e usa na posicao_inicial().
def fibonacci():
    global termo1, termo2, termo3
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    return termo1,termo2,termo3

# 5ªfunção: simplifica todas as funções anteriores em uma.
def quadrado(s1,s2):
    posicao_inicial(s1,s2)
    move()
    fibonacci()

# 6ªfunção: desenhará os circulos da espiral
def circulo(termo1,kx,ky):
    global escala,ang
    n=0
    raio = termo1
    while n <= 90:
        cx = (600 - escala*kx + raio*escala*m.cos(m.radians(ang)))
        cy = (600 - escala*ky + raio*escala*m.sin(m.radians(ang)))
        pyautogui.dragTo(cx,cy,button='left')
        ang+=-1
        n+=1

# declaração das variavéis.
x = 600
y = 600
termo1 = 1
termo2 = 1
termo3 = 0
count = 1
ang = 180

# interação com o código.
n = int(input('Digite quantas vezes quer fazer os quadrados (4 por vez): '))
escala = int(input('e qual a escala que deseja trabalhar (pixels)? '))
pyautogui.sleep(5)

# automatização para abrir o paint
pyautogui.press('winleft')
pyautogui.sleep(3)
pyautogui.write('paint')
pyautogui.sleep(5)
pyautogui.press('enter')
pyautogui.sleep(5)

# seleciona a ferramenta de retângulo
pyautogui.moveTo(723,119)
pyautogui.leftClick()

# geração dos retângulos aureos, em um ciclo de 4 quadrados por vez.
while count <= n:
    quadrado(1,1)
    quadrado(1,-1)
    quadrado(-1,-1)
    quadrado(-1,1)
    count+=1

# seleciona o lápis para desenhar as espirais.
pyautogui.moveTo(723,119)
pyautogui.leftClick()
tab = 0
while tab <= 20:
    pyautogui.press('tab')
    tab+=1
pyautogui.press('enter')
pyautogui.sleep(3)

# enfim as espirais, limitadas até n == 2, são desenhadas
if n == 1:
    pyautogui.sleep(2)
    pyautogui.moveTo(600,600) #posição inicial da espiral
    pyautogui.sleep(2)
    circulo(1,-1,0)
    circulo(1,-1,0)
    circulo(2,0,0)
    circulo(3,0,-1)
elif n > 1:
    pyautogui.sleep(2)
    pyautogui.moveTo(600,600) #posição inicial da espiral
    pyautogui.sleep(2)
    circulo(1,-1,0)
    circulo(1,-1,0)
    circulo(2,0,0)
    circulo(3,0,-1)

    circulo(5,-2,-1)
    circulo(8,-2,2)
    circulo(13,3,2)
    circulo(21,3,-6)
else: 
    print('Digite um valor válido')
# fim

