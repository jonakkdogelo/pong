import pygame
from pygame.locals import *
import numpy as np
from sys import exit
import os
import random

pygame.init()


largura_janela, altura_janela = 640, 480
FPS = 60
tamanhobola = 20
angulo = 0
tipo = []
d1 = 1
g4 = 0
e2 = []
numefeito = 1
xefeit,yefeit = 0,0
tiposs = 0
lag1,lag2 = 1,1
lentidao1,lentidao2 = 1,1
cego1,cego2 = 1,1
velmode1,velmode2 = 1,1
yjogador1,yjogador2 = altura_janela//2,altura_janela//2
xbola,ybola = largura_janela//2,altura_janela//2
velocidadex,velocidadey = 3,3
xefeito = []
yefeito = []
velefeitox = []
velefeitoy = []
for i in range(numefeito):
        xefeito.append(largura_janela//2)
        yefeito.append(altura_janela//2)
        velefeitox.append(velocidadex)
        velefeitoy.append(velocidadey)
        e2.append(0)
        tipo.append(0)

alturajogador1,alturajogador2 = 4,4
tela = pygame.display.set_mode((largura_janela, altura_janela))
clock = pygame.time.Clock()

pasta_principal = os.path.dirname(__file__)
effectshett = pygame.image.load(os.path.join(pasta_principal, 'effectshett.png')).convert_alpha()
class efeitos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = effectshett.subsurface((25*tiposs,0), (25,25))
        self.image = pygame.transform.scale(self.image, (25*1.5,25*1.5))
        self.image = pygame.transform.rotate(self.image,(angulo))
        self.rect = self.image.get_rect()
        self.rect.center = (xefeit,yefeit)

def atualizar():
    global xbola,ybola,yjogador1,yjogador2,velocidadex,velocidadey,numefeito,tamanhobola,angulo,xefeito,yefeito,velefeitox,velefeitoy,d1,tipo,e2,g4,alturajogador2,alturajogador1,lentidao1,lentidao2,lag1,lag2,cego1,cego2,velmode1,velmode2
    xbola += velocidadex
    if xbola >largura_janela//2:
        ybola += velocidadey*min(velmode2,3)
    else:
        ybola += velocidadey*min(velmode1,3)
    

    if (xbola > largura_janela-tamanhobola*2 and ybola < yjogador2+tamanhobola*alturajogador2 and ybola > yjogador2-tamanhobola*0.7) or (xbola < tamanhobola and ybola < yjogador1+tamanhobola*alturajogador1 and ybola > yjogador1-tamanhobola*0.7):
        velocidadex = -velocidadex
        if xbola <largura_janela//2:
            xbola += 5
        else:
            xbola -= 5

    if xbola>largura_janela or xbola+tamanhobola<0:
        xbola,ybola = largura_janela//2,altura_janela//2
        velocidadex = 3
        tamanhobola = 20
        cego1,cego2 = 1,1
        lentidao1,lentidao2 = 1,1
        lag1,lag2=1,1
        velmode1,velmode2 = 1,1
        d1 = 1
        g4 = 0
        e2 = []
        xefeito = []
        numefeito = 1
        for i in range(numefeito):
            e2.append(0)
            xefeito.append(largura_janela//2)
        alturajogador1,alturajogador2 = 4,4

    if ybola+tamanhobola>altura_janela or ybola<0:
        velocidadey = -velocidadey

    if random.randint(0,100) <=60:
        aleatorio = 1
    else:
        aleatorio = -1 
        

    if d1 == 400:
        for i in range(numefeito):
            xefeito[i] += velefeitox[i]
            yefeito[i] += velefeitoy[i]
            if xefeito[i]>largura_janela-tamanhobola or xefeito[i]-tamanhobola<0:
                velefeitox[i] = -velefeitox[i]
            if yefeito[i]>altura_janela-tamanhobola or yefeito[i]-tamanhobola<0:
                velefeitoy[i] = -velefeitoy[i]
            if xefeito[i] < 40 + largura_janela//2:
                if xefeito[i] >largura_janela//2:
                    e2[i] = 0
            else:
                if xefeito[i] <60 +largura_janela//2:
                    e2[i] = 0

            if (xefeito[i] > largura_janela-tamanhobola*2 and yefeito[i] < yjogador2+tamanhobola*alturajogador2 and yefeito[i] > yjogador2-tamanhobola*0.7) or (xefeito[i] < tamanhobola and yefeito[i] < yjogador1+tamanhobola*alturajogador1 and yefeito[i] > yjogador1-tamanhobola*0.7):
                    if tipo[i] == 0 and e2[i] == 0:
                        if xefeito[i] >largura_janela//2:
                            alturajogador2 += aleatorio
                        else:
                            alturajogador1 += aleatorio
                    elif tipo[i] == 1 and e2[i] == 0:
                        if xefeito[i] >largura_janela//2:
                            lag2 += 1
                        else:
                            lag1 += 1
                    elif tipo[i] == 2 and e2[i] == 0:
                        if xefeito[i] > largura_janela//2:
                            lentidao2 += aleatorio
                        else:
                            lentidao1 += aleatorio
                    elif tipo[i] == 3 and e2[i] == 0:
                        if xefeito[i] > largura_janela//2:
                            cego2 += 1
                        else:
                            cego1 += 1
                    elif tipo[i] ==4 and e2[i] == 0:
                        if xefeito[i] > largura_janela//2:
                            velmode2 += 1
                        else:
                            velmode1 += 1
                    if tipo[i] != 4 and e2[i] == 0:
                        tipo[i] += 1
                        e2[i] = 1
                    elif e2[i] == 0:
                        tipo[i] = 0
                        e2[i] = 1
    else:
        d1 += 1

    if angulo <= 360:
        angulo += 3
    else:
        angulo = 0

    if g4 == 800:
        numefeito += 1
        g4 = 0
        xefeito.append(largura_janela//2)
        yefeito.append(altura_janela//2)
        velefeitox.append(velocidadex)
        velefeitoy.append(velocidadey)
        e2.append(0)
        tipo.append(0)
    else:
        g4 += 1
    print(numefeito)
    if lentidao2 == -1:
        lentidao2 = 0
    if lentidao1 == -1:
        lentidao1 = 0
    if cego1 == 4:
        cego1 = 2
    if cego2 == 4:
        cego2 = 2
    f1 = random.randint(1,int(min((lag1**2)//lag1,5)))
    f2 = random.randint(1,int(min((lag2**2)//lag2,5)))
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        if f1 == 1 or f1 == 3:
            yjogador1 -= 10*(1/max(lentidao1,0.5))
    if keys[K_s]:
        if f1 == 1 or f1 ==2:
            yjogador1 += 10*(1/max(lentidao1,0.5))
    if keys[K_UP]:
        if f2 ==1 or f2 ==3:
            yjogador2 -= 10*(1/max(lentidao2,0.5))
    if keys[K_DOWN]:
        if f2 ==1 or f2 ==2:
            yjogador2 += 10*(1/max(lentidao2,0.5))

    


def desenhar(tela):
    global xefeit,yefeit,tiposs
    tela.fill((0,0,0))
    pygame.draw.rect(tela,(max(255/(cego1**3),1),0,0),(0,yjogador1,tamanhobola,tamanhobola*max(min(alturajogador1,6),1)))
    pygame.draw.rect(tela,(0,0,max(255/(cego2**3),1)),(largura_janela-tamanhobola,yjogador2,tamanhobola,tamanhobola*max(min(alturajogador2,6),1)))
    pygame.draw.rect(tela,(255,255,0),(xbola,ybola,tamanhobola,tamanhobola))
    if d1 == 400:
        allsrites = pygame.sprite.Group()
        for i in range(numefeito):
            xefeit = xefeito[i]
            yefeit = yefeito[i]
            tiposs = tipo[i]
            efeitoclass = efeitos()
            allsrites.add(efeitoclass)
        allsrites.draw(tela)
        allsrites.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    atualizar()
    desenhar(tela)
    clock.tick(FPS)
    pygame.display.flip()