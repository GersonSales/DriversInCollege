import pygame, random

#Iniciar Pygame
pygame.init()

#Diretorio das imagens
diretorio_imagens = "Jogo/Cenario/"

#Classe que designa as imagens de cada Fase
class Cenario:

    def __init__(self):
        
        self.Lista_carros = [pygame.image.load(diretorio_imagens + "Carros/carro_objeto_" + str(x) + ".png") for x in range(17)]
        random.shuffle(self.Lista_carros)
        self.Fases = {
        "Fase_1": 
        {"Imagem_fase": pygame.image.load(diretorio_imagens + "Fases/Fase_1.png"),
        "Imagem_barreira": [pygame.image.load(diretorio_imagens + "Fases/Borda_fase1.png")],
        "Posicao_barreira": [(0, 0, 0)],
        "Tamanho_tela": (800, 600),
        "Tamanho_mapa": (800, 600),
        "Virtual_x": 567,
        "Virtual_y": 456,
        "Angulo_inicial": 270,
        "Velocidade_inicial": 65,
        "Posicao_vaga": (63, 170, 0),
        "Posicao_carros": [(64, 80, 3), (71, 270, 5), (78, 464, 0), (339, 426, 6),  (545, 122, 3)] },


        "Fase_2": 
        {"Imagem_fase": pygame.image.load(diretorio_imagens + "Fases/Fase_2.png"),
        "Imagem_barreira": [pygame.image.load(diretorio_imagens + "Fases/Barreira_fase2.png"),
                            pygame.image.load(diretorio_imagens + "Fases/Borda_fase2.png")],
        "Posicao_barreira": [(0, 330, 0), (0, 0, 0)],
        "Tamanho_tela": (800, 600),
        "Tamanho_mapa": (800, 600),
        "Virtual_x": -300,
        "Virtual_y": 640,
        "Angulo_inicial": 90,
        "Velocidade_inicial": 55,
        "Posicao_vaga": (435, 40, 90),
        "Posicao_carros": [(57, 33, -95), (153, 41, 82), (257, 32, -90), (335, 30, 98),  (540, 40, 90), (650, 28, -87)] },

        "Fase_3": 
        {"Imagem_fase": pygame.image.load(diretorio_imagens + "Fases/Fase_3.png"),
        "Imagem_barreira": [pygame.image.load(diretorio_imagens + "Fases/Barreira_fase3.png"),
                            pygame.image.load(diretorio_imagens + "Fases/Borda_fase3.png")],
        "Posicao_barreira": [(0, 130, 0), (0, 0, 0)],
        "Ambientacao": [pygame.image.load(diretorio_imagens + "Ambientacao/Arvore_1.png"),
                        pygame.image.load(diretorio_imagens + "Ambientacao/Arvore_1.png")],
        "Posicao_ambientacao": [(0, 50, 0), (330, 20, -45)],
        "Tamanho_tela": (800, 600),
        "Tamanho_mapa": (800, 600),
        "Virtual_x": -300,
        "Virtual_y": 200,
        "Angulo_inicial": 90,
        "Velocidade_inicial": 55,
        "Posicao_vaga": (363, 232, 90),
        "Posicao_carros": [(44, 227, 95), (157, 233, 82), (274, 239, 90)] },

        "Fase_4": 
        {"Imagem_fase": pygame.image.load(diretorio_imagens + "Fases/Fase_4.png"),
        "Imagem_barreira":[pygame.image.load(diretorio_imagens + "Fases/Barreira_fase4.png")],
        "Posicao_barreira": [(0, 0, 0)],
        "Ambientacao": [],
        "Posicao_ambientacao": [],
        "Tamanho_tela": (800, 600),
        "Tamanho_mapa": (800, 600),
        "Virtual_x": 167,
        "Virtual_y": 792,
        "Angulo_inicial": 0,
        "Velocidade_inicial": 40,
        "Posicao_vaga": (410,142, 0),
        "Posicao_carros": [[0, 270, 0, False], [900, 400, 180, True], (30, 150, 0), (230, 150, 0), (600, 150, 0)] },

        "Fase_5": 
        {"Imagem_fase": pygame.image.load(diretorio_imagens + "Fases/Fase_5.png"),
        "Imagem_barreira":[pygame.image.load(diretorio_imagens + "Fases/Barreira_fase5.png")],
        "Posicao_barreira": [(0, 0, 0)],
        "Ambientacao": [pygame.image.load(diretorio_imagens + "Ambientacao/Arvore_2.png")],
        "Posicao_ambientacao": [],
        "Tamanho_tela": (800, 600),
        "Tamanho_mapa": (800, 600),
        "Virtual_x": -300,
        "Virtual_y": 630,
        "Angulo_inicial": 90,
        "Velocidade_inicial": 55,
        "Posicao_vaga": (215, 19, 0),
        "Posicao_carros": [[0, 130, 0, False],[900, 230, 180, True], (30, 30, 0), (430, 30, 0), (630, 30, 0)] },



        "Fase_6": 
        {"Imagem_fase": pygame.image.load(diretorio_imagens + "Fases/Fase_6.png"),
        "Imagem_barreira": [pygame.image.load(diretorio_imagens + "Fases/Barreira_fase6.png")],
        "Posicao_barreira": [(0, 0, 0)],
        "Ambientacao": [],
        "Posicao_ambientacao": [],
        "Tamanho_tela": (800, 600),
        "Tamanho_mapa": (800, 600),
        "Virtual_x": -220,
        "Virtual_y": 711,
        "Angulo_inicial": 45,
        "Velocidade_inicial": 40,
        "Posicao_vaga": (11, 189, 0),
        "Posicao_carros": [(650, 328, 0), (650, 227, 0), (650, 129, 0), (450, -110, 55), (330, -110, 55), (220, -110, 55), (120, -110, 55), (0, -110, 55)] },



        "Fase_7": 
        {"Imagem_fase": pygame.image.load(diretorio_imagens + "Fases/Fase_7.png"),
        "Imagem_barreira": [pygame.image.load(diretorio_imagens + "Fases/Barreira_fase7.png")],
        "Posicao_barreira": [(0, 0, 0)],
        "Ambientacao": [pygame.image.load(diretorio_imagens + "Ambientacao/Loja.png")],
        "Posicao_ambientacao": [(0, 30, 0)],
        "Tamanho_tela": (800, 600),
        "Tamanho_mapa": (800, 1100),
        "Virtual_x": -170,
        "Virtual_y": 1163,
        "Angulo_inicial": 90,
        "Velocidade_inicial": 5,
        "Posicao_vaga": (583, 232, -90),
        "Posicao_carros": [(31, 240, 90), (136, 240, 90), (695, 240, 90), (490, 240, 90), 
                           [-200, 740, 180, True], [-600, 720, 180, True],  [1000, 630, 0, False], [1600, 620, 0, False]] },

        "Fase_8": 
        {"Imagem_fase": pygame.image.load(diretorio_imagens + "Fases/Fase_8.png"),
        "Imagem_barreira": [pygame.image.load(diretorio_imagens + "Fases/Barreira_fase8.png")],
        "Posicao_barreira": [(0, 0, 0)],
        "Ambientacao": [],
        "Posicao_ambientacao": [],
        "Tamanho_tela": (800, 600),
        "Tamanho_mapa": (1000, 1000),
        "Virtual_x": 756,#140,
        "Virtual_y": 757,#163,
        "Angulo_inicial": -120,
        "Velocidade_inicial": 45,
        "Posicao_vaga": (898, 0, -90),
        "Posicao_carros": [(281, 200, 125), (297, 2, 85), (394, 30, 95), (505, 4, 90), (595, 45, 85), (750, 135, 230)] },

       "Fase_9": 
        {"Imagem_fase": pygame.image.load(diretorio_imagens + "Fases/Fase_9.png"),
        "Imagem_barreira": [pygame.image.load(diretorio_imagens + "Fases/Barreira_fase9.png")],
        "Posicao_barreira": [(0, 0, 0)],
        "Ambientacao": [],
        "Posicao_ambientacao": [],
        "Tamanho_tela": (800, 600),
        "Tamanho_mapa": (1000, 1000),
        "Virtual_x": -300,
        "Virtual_y": 257,
        "Angulo_inicial": 90,
        "Velocidade_inicial": 0,#55,
        "Posicao_vaga": (528, 717, 0),
        "Posicao_carros": [(-40, 215, 5), (-80, 310, 2), (-70, 400, -10), (-75, 500, 9), (450, 200, 20), (610, 310, -3), 
                           (560, 410, 9), (610, 510, 4), (610, 630, -7)] },

        "Fase_10": 
        {"Imagem_fase": pygame.image.load(diretorio_imagens + "Interacao/Game_over.png"),
        "Tamanho_tela": (800, 600),
        "Tamanho_mapa": (500, 600),
        "Virtual_x": 5800,
        "Virtual_y": 7700,
        "Angulo_inicial": 0,
        "Velocidade_inicial": 50,
        "Posicao_vaga": (7305, 75, 0),
        "Posicao_carros": []} 

        }

