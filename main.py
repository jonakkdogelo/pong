import pygame
from pygame.locals import *
import random



LARGURA_JANELA = 640
ALTURA_JANELA = 480
tamanhodojogador = 20
tamanhodabola = random.randint(7,20)
xdojogador = LARGURA_JANELA//2
ydojogador = ALTURA_JANELA - tamanhodojogador
xdabola = LARGURA_JANELA//2
ydabola = ALTURA_JANELA//2 -40
acelbolax = 2.5
acelbolay = 0.5
gravity = float(1/10)
dificuldade = 1
num1 = 1
num2 = 2
inimigos = []
acelinimigos = 1.5
pontos = 0


relogio = pygame.time.Clock()

def atualizar():
    global xdabola,ydabola,acelbolay,acelbolax,gravity,xdojogador,ydojogador,tamanhodabola,tamanhodojogador,dificuldade,num1,num2,inimigos,acelinimigos,pontos
    xdabola += acelbolax
    ydabola += acelbolay
    acelbolay += gravity
    acelinimigos += float(gravity/10)
    ydojogador = ALTURA_JANELA - tamanhodojogador

    if ydabola +tamanhodabola >= ydojogador-3 and xdabola+tamanhodabola >= xdojogador and xdabola-tamanhodabola <= xdojogador+tamanhodojogador*4:
        acelbolay = min(max(-5*dificuldade//2,-8),-4)
        pontos +=1
        if acelbolax > 0:
            acelbolax = random.randint(2,min(3+dificuldade,8))
        else:
            acelbolax = random.randint(max(-3-dificuldade,-8),-2)
        if num1 == 3:
            dificuldade += 1
            num1 = 1
            gravity = min(gravity*min(max(dificuldade*9/10,0.5),1),0.5)
        else:
            num1 += 1
        

    if xdabola <= 0 or xdabola+tamanhodabola >= LARGURA_JANELA:
        acelbolax = -acelbolax

    if ydabola > ALTURA_JANELA+tamanhodabola+2:
        xdabola = LARGURA_JANELA//2
        ydabola = ALTURA_JANELA//2 -40
        tamanhodabola = random.randint(7,20)
        acelbolay = 2.5
        acelbolax = 0.5
        gravity = float(1/10)
        dificuldade = 1
        inimigos = []
        num1,num2 = 1,2
        tamanhodojogador,pontos = 20,0

    if num2 == dificuldade:
        for x in range(1):
            inimigos.append(random.randint(10,LARGURA_JANELA-10))
            inimigos.append(-50)
        num2 += 1

    for y in range(1, len(inimigos), 2):
        inimigos[y] = inimigos[y] + acelinimigos
        if inimigos[y] > ALTURA_JANELA+15:
            inimigos[y] = -50
            inimigos[y-1] = random.randint(10,LARGURA_JANELA-10)
        if inimigos[y] +14 >= ydojogador and inimigos[y-1]+7 >= xdojogador and inimigos[y-1]-7 <= xdojogador + tamanhodojogador*4:
            inimigos[y] = -50
            inimigos[y-1] = random.randint(10,LARGURA_JANELA-10)
            tamanhodojogador = tamanhodojogador -2


    if acelinimigos > 3 +max(min(dificuldade-5,3),0):
        acelinimigos = 1 + max(min(dificuldade-5,1),0)

    keys = pygame.key.get_pressed()

    if keys[K_d]:
        xdojogador += 7.5
    if keys[K_a]:
        xdojogador -= 7.5
    if keys[K_h]:
        dificuldade += 1



def desenhar(tela):
    tela.fill((0,0,0))   
    pygame.draw.rect(tela, (200,200,0),(xdabola,ydabola,tamanhodabola,tamanhodabola))
    pygame.draw.rect(tela, (0,0,200),(xdojogador,ydojogador,tamanhodojogador*4,tamanhodojogador))
    for x in range(1,len(inimigos),2):
        pygame.draw.rect(tela, (200,0,0),(inimigos[x-1],inimigos[x],7,14))
    #pygame.draw.rect(tela, (255,0,0),(xdojogador + tamanhodojogador*2,ydojogador,10,10))


pygame.init()
tela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
fonte = pygame.font.SysFont('Arial', 20, True, True)
#musica = pygame.mixer.music.load('1-05. Dry Out (mp3cut.net).wav')
#pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #print(inimigos)
    atualizar()
    desenhar(tela)
    relogio.tick(40)
    mensagem = f'pontos:{pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    tela.blit(texto_formatado, (290,10))
    pygame.display.flip()