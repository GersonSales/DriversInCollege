import pygame, sys
from pygame import *
from pygame.mixer import Sound
pygame.init()
pygame.mixer.pre_init(44200)
class Mouse:
    def __init__(self):
        self.Sons_mouse = [pygame.mixer.Sound("Sons/Mouse_ON.wav"), pygame.mixer.Sound("Sons/Mouse_click.wav")]
    def coordenadas_cursor(self):
        return pygame.mouse.get_pos()

    def seleciona_imagem(self, (x, y, larg, alt)):
        area_imagem = Rect(x, y, larg, alt)
        return area_imagem

    def Verifica_click(self, surface,  event, imagem, Tela_menu = True, Tela_item = False, sair=None):
        self.surface = surface
        self.event = event
        self.imagem = imagem
        self.Tela_menu = Tela_menu
        self.Tela_item = Tela_item
        if self.seleciona_imagem(imagem[0]).collidepoint(self.coordenadas_cursor()):
            surface.blit(imagem[2], (imagem[0][0], imagem[0][1]))
            if event.type == 5 and pygame.mouse.get_pressed()[0]: 
                if sair != None:
                    pygame.quit()
                    sys.exit()
                else:
                    Tela_menu = False
                    Tela_item = True

                return Tela_menu, Tela_item, True 

            return Tela_menu, Tela_item, False
        else:
            surface.blit(imagem[1], (imagem[0][0], imagem[0][1]))

            return Tela_menu, Tela_item, None

    def Possibilidade_click(self, Sons_menu, Som_mouse, reproduzir, Volume):
        contador = 0
        Sons_menu[0].set_volume(Volume)
        Sons_menu[1].set_volume(Volume)
        for som in range(len(Som_mouse)):
            if Som_mouse[som] == False:
                if reproduzir[0]:
                    Sons_menu[0].play()
                    reproduzir[0] = False
            elif Som_mouse[som] and reproduzir[0]:
                Sons_menu[1].play()
                reproduzir[0] = False
                Som_mouse[som] = None
            else:
                contador += 1
        if contador == len(Som_mouse):
            reproduzir[0] = True
        else:
            reproduzir[0] = False

        contador = 0
    
