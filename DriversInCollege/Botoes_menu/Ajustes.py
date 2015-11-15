import pygame
from Botoes_menu.Mouse import *
#from pygame.mixer import *


class Menu_ajustes(Mouse):
   
    

    def __init__(self):


        self.Conf = [(730, 535, 40, 40), pygame.image.load("Imagens/Conf_MON.png"), pygame.image.load("Imagens/Conf_MOFF.png")]

        self.Idioma = [(300,330, 150, 30), pygame.image.load("Imagens/Portugues_MOFF.png"), pygame.image.load("Imagens/Portugues_MON.png"), pygame.image.load("Imagens/English_MOFF.png"), pygame.image.load("Imagens/English_MON.png")]

        self.Tela_cheia = [(430, 330, 120, 30),  pygame.image.load("Imagens/Tela_cheia_off_MOFF.png"), pygame.image.load("Imagens/Tela_cheia_off_MON.png"), pygame.image.load("Imagens/Tela_cheia_on_MOFF.png"), pygame.image.load("Imagens/Tela_cheia_on_MON.png")]

        self.Volume_menos = [(215, 265, 20, 20), pygame.image.load("Imagens/Volume_menos_MOFF.png"), pygame.image.load("Imagens/Volume_menos_MON.png")]

        self.Volume_mais = [(565, 265, 20, 20), pygame.image.load("Imagens/Volume_mais_MOFF.png"), pygame.image.load("Imagens/Volume_mais_MON.png")]


        self.Volume_barra = [True, True, True, True, True, pygame.image.load("Imagens/Volume_barra.png")]

    def Imprime_tela(self, surface):
        self.surface = surface
        surface.blit(pygame.image.load("Imagens/Menu.png"), (0, 0)) 
        surface.blit(pygame.image.load("Imagens/Transparencia_menu.png"), (0, 0)) 
        surface.blit(pygame.image.load("Imagens/Nome_ajustes.png"), (300, 150))
        surface.blit(pygame.image.load("Imagens/Volume.png"), (310, 220))
        surface.blit(pygame.image.load("Imagens/Barra_volume.png"), (245, 260))
        #surface.blit(pygame.image.load("Imagens/Idioma.png"), (150, 330))
        surface.blit(pygame.image.load("Imagens/Tela_cheia.png"), (283, 330)) 

    def Altera_volume(self, event, Sons, i= None):
        reproduzir = [True]
        Som_mouse = [None, None]
        self.event = event
        Volume_menos = self.Volume_menos
        Volume_mais = self.Volume_mais
        Volume = 0.
        if self.seleciona_imagem(Volume_menos[0]).collidepoint(self.coordenadas_cursor()):
            self.surface.blit(Volume_menos[2], (Volume_menos[0][0], Volume_menos[0][1]))
            i = (4, 3, 2, 1, 0, 5)
            verific = True
            inverso = False 
            #Som_mouse[0] = False
        else:
            self.surface.blit(Volume_menos[1], (Volume_menos[0][0], Volume_menos[0][1]))
            Som_mouse[0] = None

        if self.seleciona_imagem(self.Volume_mais[0]).collidepoint(self.coordenadas_cursor()):
            self.surface.blit(self.Volume_mais[2], (self.Volume_mais[0][0], self.Volume_mais[0][1]))
            i = (0, 1, 2, 3, 4, 5)
            verific = False
            inverso = True
            #Som_mouse[1] = False
        else:
            self.surface.blit(self.Volume_mais[1], (self.Volume_mais[0][0], self.Volume_mais[0][1]))
            Som_mouse[1] = None 

        if i != None:
            if event.type == 5 and i[0] == 4:
                Som_mouse[0] = True
            elif event.type == 5 and i[0] == 0:
                Som_mouse[1]  = True
                
            #Verifica se esta clicando no botao volume 
            if event.type == 5 and self.Volume_barra[i[0]] == verific:
               self.Volume_barra[i[0]] = inverso
            elif event.type == 5 and self.Volume_barra[i[1]] == verific:
               self.Volume_barra[i[1]] = inverso
            elif event.type == 5 and self.Volume_barra[i[2]] == verific:
               self.Volume_barra[i[2]] = inverso
            elif event.type == 5 and self.Volume_barra[i[3]] == verific:
               self.Volume_barra[i[3]] = inverso
            elif event.type == 5 and self.Volume_barra[i[4]] == verific:
               self.Volume_barra[i[4]] = inverso

        #Imprime as imagens do volume de acordo com os parametros TRUE/FALSE
        if self.Volume_barra[0]:
            self.surface.blit(self.Volume_barra[5],(250, 265))
            Volume = .2
        if self.Volume_barra[1]:
            self.surface.blit(self.Volume_barra[5],(310, 265))
            Volume = .4
        if self.Volume_barra[2]:
            self.surface.blit(self.Volume_barra[5],(370, 265))
            Volume = .6
        if self.Volume_barra[3]:
            self.surface.blit(self.Volume_barra[5],(430, 265))
            Volume = .8
        if self.Volume_barra[4]:
            self.surface.blit(self.Volume_barra[5],(490, 265))
            Volume = 1.
        for som in range(len(Sons)):
            if som == 0:
                pygame.mixer.music.set_volume(Volume)
            else:
                Sons[som].set_volume(Volume)
        self.Possibilidade_click(Sons, Som_mouse, reproduzir, Volume) 
        return Volume


    def Altera_tela_cheia(self, surface, event, Tela_cheia_on, Tela_cheia_off):
        self.surface = surface 
        self.event = event
        Tela_cheia = self.Tela_cheia

        #Verifica se o mouse esta clicando no botao TELA CHEIA
        if self.seleciona_imagem(Tela_cheia[0]).collidepoint(self.coordenadas_cursor()):
            if Tela_cheia_on:
                surface.blit(Tela_cheia[4], (Tela_cheia[0][0], Tela_cheia[0][1]))
                if event.type == 5 and pygame.mouse.get_pressed()[0]:
                    Tela_cheia_on = False
                    tela_cheia_off = True
                    pygame.display.set_mode((800, 600))
            else:
                surface.blit(Tela_cheia[2], (Tela_cheia[0][0], Tela_cheia[0][1]))               
                if event.type == 5 and pygame.mouse.get_pressed()[0]:

                    Tela_cheia_off = False
                    Tela_cheia_on = True

                    pygame.display.set_mode((800, 600), FULLSCREEN)
        else:
            if Tela_cheia_on:
                surface.blit(Tela_cheia[3], (Tela_cheia[0][0], Tela_cheia[0][1]))   
            else:
                surface.blit(Tela_cheia[1], (Tela_cheia[0][0], Tela_cheia[0][1]))
        return Tela_cheia_on, Tela_cheia_off
