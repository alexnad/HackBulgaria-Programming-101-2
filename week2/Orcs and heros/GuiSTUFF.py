import pygame
from pygame.locals import *
#from InputControl import Input
#just experimenting with pygame


pygame.init()
surface = pygame.display.set_mode((500, 500))
color = pygame.Color(0, 100, 0)
myfont = pygame.font.SysFont("monospace", 20)
enter_text = False
text = ''
clock = pygame.time.Clock()
while True:
    surface.fill((100, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                enter_text = not enter_text
                text = ''
            if enter_text:
                if event.key == K_a:
                    text += 'a'
                elif event.key == K_b:
                    text += 'b'
                elif event.key == K_c:
                    text += 'c'
                elif event.key == K_d:
                    text += 'd'
                elif event.key == K_e:
                    text += 'e'
                elif event.key == K_f:
                    text += 'f'
                elif event.key == K_g:
                    text += 'g'
                elif event.key == K_h:
                    text += 'h'
                elif event.key == K_i:
                    text += 'i'
                elif event.key == K_j:
                    text += 'j'
                elif event.key == K_k:
                    text += 'k'
                elif event.key == K_l:
                    text += 'l'
                elif event.key == K_m:
                    text += 'm'
                elif event.key == K_n:
                    text += 'n'
                elif event.key == K_o:
                    text += 'o'
                elif event.key == K_p:
                    text += 'p'
                elif event.key == K_q:
                    text += 'q'
                elif event.key == K_r:
                    text += 'r'
                elif event.key == K_s:
                    text += 's'
                elif event.key == K_t:
                    text += 't'
                elif event.key == K_u:
                    text += 'u'
                elif event.key == K_v:
                    text += 'v'
                elif event.key == K_w:
                    text += 'w'
                elif event.key == K_x:
                    text += 'x'
                elif event.key == K_y:
                    text += 'y'

    print_text = myfont.render(text, 1, (0, 100, 0))
    clock.tick(30)
    #text = ''
    surface.blit(print_text, (50, 50))
    pygame.display.update()

"""

    if event.type == KEYDOWN:
        if event.key == K_RETURN:
            for event in pygame.event.get():
                buff == []
                if event.key ==
"""
