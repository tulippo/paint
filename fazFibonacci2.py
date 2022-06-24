# importando a biblioteca a ser trabalhada conjunto ao código.
import pyautogui

# 1ªfunção: clique fora do desenho para tirar a seleção do desenho, se for no paint.
def clicar():
    pyautogui.moveTo(1500,450)
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

# declaração das variavéis.
x = 600
y = 600
termo1 = 1
termo2 = 1
termo3 = 0
count = 1

# interação com o código.
n = int(input('Digite quantas vezes quer fazer os quadrados (4 por vez): '))
escala = int(input('e qual a escala que deseja trabalhar (pixels)? '))
pyautogui.sleep(3)

# geração dos retângulos aureos, em um ciclo de 4 quadrados por vez.
while count <= n:
    quadrado(1,1)
    quadrado(1,-1)
    quadrado(-1,-1)
    quadrado(-1,1)
    count+=1

