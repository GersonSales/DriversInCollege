#coding: utf-8
import pygame
from pygame import *
from Botoes_menu.Mouse import *


class Menu_novo_jogo:
    
    def __init__(self):
        self.Continuar = [(430, 410, 110, 20), pygame.image.load("Imagens/Continuar_MOFF.png"), pygame.image.load("Imagens/Continuar_MON.png")]


    def Imprime_tela(self, surface):
        self.surface = surface
        surface.blit(pygame.image.load("Imagens/Menu.png"), (0, 0)) 
        surface.blit(pygame.image.load("Imagens/Transparencia_menu.png"), (0, 0))
        surface.blit(pygame.image.load("Imagens/Instrucoes.png"), (180, 200)) 
        surface.blit(pygame.image.load("Imagens/Nome_novo_jogo.png"), (300, 150))
#        surface.blit(pygame.image.load("Imagens/Vaga.png"),(420, 260))
#        surface.blit(pygame.image.load("Imagens/Arrows.png"), (200, 250))
	Fonte = pygame.font.Font("Font/AbyssinicaSIL-R.ttf", 20)
#	instrucoes_setas = Fonte.render("Movimentacao do carro", 1, (80, 80, 80))
#	instrucoes_vaga = Fonte.render("Objetivo", 1, (80, 80, 80))
#	surface.blit(instrucoes_setas, (175, 370))
#	surface.blit(instrucoes_vaga, (480, 370))
    
 


