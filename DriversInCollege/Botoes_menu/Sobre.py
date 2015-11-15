import pygame
from pygame import *

class Menu_sobre:
    
    def Imprime_tela(self, surface):
        self.surface = surface
        surface.blit(pygame.image.load("Imagens/Menu.png"), (0, 0)) 
        surface.blit(pygame.image.load("Imagens/Transparencia_menu.png"), (0, 0)) 
        surface.blit(pygame.image.load("Imagens/Nome_sobre.png"), (300, 150))
             
        #Abre e imprime na tela o arquivo de texto
        Fonte =  pygame.font.Font("Font/AbyssinicaSIL-R.ttf", 17) 
        Sobre_arquivo = open("Sobre/Sobre.dat", "r")
        Cord_y = 200 
        for Sobre_texto in Sobre_arquivo:
            Sobre_print = Fonte.render(Sobre_texto, 1, (80, 80, 80))
            surface.blit(Sobre_print, (220, Cord_y))
            Cord_y += 20

