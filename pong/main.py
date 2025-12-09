import pygame
from pygame.locals import *
from OpenGL.GL import *

LARGURA_JANELA = 640 #640 padrão e 1036 cheio
ALTURA_JANELA = 480  #480 padrão e 777 cheio

xDaBola = 0
yDaBola = 0
tamanhoDaBola = 20
velocidadeDaBolaEmX = float(1/20)
velocidadeDaBolaEmY = float(1/20)

yDoJogador1 = 0
yDoJogador2 = 0

pontoazul = 0
pontovermelho = -1
modo = 2
bot = 0

def xDoJogador1():
    return -LARGURA_JANELA / 2 + larguraDosJogadores() / 2

def xDoJogador2():
    return LARGURA_JANELA / 2 - larguraDosJogadores() / 2

def larguraDosJogadores():
    return tamanhoDaBola

def alturaDosJogadores():
    return 4 * tamanhoDaBola

def atualizar():
    global xDaBola, yDaBola, velocidadeDaBolaEmX, velocidadeDaBolaEmY, yDoJogador1, yDoJogador2, pontovermelho, pontoazul, tamanhoDaBola, acel, tamanho, modo, bot

    xDaBola = xDaBola + velocidadeDaBolaEmX
    yDaBola = yDaBola + velocidadeDaBolaEmY

    if (xDaBola + tamanhoDaBola / 2 > xDoJogador2() - larguraDosJogadores() / 2
    and yDaBola - tamanhoDaBola / 2 < yDoJogador2 + alturaDosJogadores() / 2
    and yDaBola + tamanhoDaBola / 2 > yDoJogador2 - alturaDosJogadores() / 2):
        velocidadeDaBolaEmX = float(-velocidadeDaBolaEmX - acel)
        xDaBola = xDaBola - 5

    if (xDaBola - tamanhoDaBola / 2 < xDoJogador1() + larguraDosJogadores() / 2
    and yDaBola - tamanhoDaBola / 2 < yDoJogador1 + alturaDosJogadores() / 2
    and yDaBola + tamanhoDaBola / 2 > yDoJogador1 - alturaDosJogadores() / 2):
        velocidadeDaBolaEmX = -velocidadeDaBolaEmX
        tamanhoDaBola = float(tamanhoDaBola - tamanho)
        xDaBola = xDaBola + 5

    if yDaBola + tamanhoDaBola / 2 > ALTURA_JANELA / 2:
        velocidadeDaBolaEmY = -velocidadeDaBolaEmY

    if yDaBola - tamanhoDaBola / 2 < -ALTURA_JANELA / 2:
        velocidadeDaBolaEmY = -velocidadeDaBolaEmY

    if xDaBola < -LARGURA_JANELA / 2:
        xDaBola = 0
        yDaBola = 0
        pontoazul = pontoazul + 1
        velocidadeDaBolaEmX = float (1/20)
        tamanhoDaBola = 20

    if xDaBola > LARGURA_JANELA / 2:
        xDaBola = 0
        yDaBola = 0
        pontovermelho = pontovermelho + 1
        velocidadeDaBolaEmX = float (1/20)
        tamanhoDaBola = 20

    
    if modo == 1:
     acel = 1/140
     tamanho = 4/11
    else:
      if modo == 2:
        acel = 1/80
        tamanho = 7/10
      else:
        if modo ==3:
            acel = 1/50
            tamanho = 12/10
        else:
            if modo ==4:
                acel = 1/20
                tamanho = 2   

    if bot == 1:
        yDoJogador2 = yDaBola
        
    keys = pygame.key.get_pressed()

    if keys[K_w]:
        yDoJogador1 = float(yDoJogador1 + 1/6)

    if keys[K_s]:
        yDoJogador1 = float(yDoJogador1 - 1/6)

    if keys[K_UP]:
        yDoJogador2 = float(yDoJogador2 + 1/6)

    if keys[K_DOWN]:
        yDoJogador2 = float(yDoJogador2 - 1/6)

    if keys[K_e]:
        modo = 1    

    if keys[K_m]:
        modo = 2

    if keys[K_h]:
        modo = 3

    if keys[K_i]:
        modo = 4 

    if keys[K_b]:
        waws = 1           

def desenharRetangulo(x, y, largura, altura, r, g, b):
    glColor3f(r, g, b)

    glBegin(GL_QUADS)
    glVertex2f(-0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, 0.5 * altura + y)
    glVertex2f(-0.5 * largura + x, 0.5 * altura + y)
    glEnd()

def desenhar():
    glViewport(0, 0, LARGURA_JANELA, ALTURA_JANELA)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-LARGURA_JANELA / 2, LARGURA_JANELA / 2, -ALTURA_JANELA / 2, ALTURA_JANELA / 2, 0, 1)

    glClear(GL_COLOR_BUFFER_BIT)

    desenharRetangulo(xDaBola, yDaBola, tamanhoDaBola, tamanhoDaBola, 1, 1, 0)
    desenharRetangulo(xDoJogador1(), yDoJogador1, larguraDosJogadores(), alturaDosJogadores(), 1, 0, 0)
    desenharRetangulo(xDoJogador2(), yDoJogador2, larguraDosJogadores(), alturaDosJogadores(), 0, 0, 1)

    if pontoazul> pontovermelho:
        desenharRetangulo(40,140,20,20,0,0,1)
    else:
        if pontovermelho> pontoazul:
         desenharRetangulo(-40,140,20,20,1,0,0)

    pygame.display.flip()

pygame.init()
pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA), DOUBLEBUF | OPENGL)

while True:
    atualizar()
    desenhar()
    pygame.event.pump()
    