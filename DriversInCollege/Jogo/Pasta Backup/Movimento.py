import pygame
from pygame.locals import *
import math, sys, time 
Tamanho_tela_x = 800
Tamanho_tela_y = 600
 
Tamanho_mapa_x = 800
Tamanho_mapa_y = 600
contador_backup = 0
DIREITA = 0
ESQUERDA = 1
 
diretorio_imagens = "Jogo/Cenario/"
def clamp(x, minimo, maximo):
    return max(minimo, min(maximo, x))
 
class Camera:
    def __init__(self, min_x, min_y, max_x, max_y):
        self.min_x, self.min_y = min_x, min_y
        self.max_x, self.max_y = max_x, max_y
        self.x = min_x
        self.y = min_y

    def center_on(self, x, y):
        new_x = x - Tamanho_tela_x / 2
        new_y = y - Tamanho_tela_y / 2
        self.x = clamp(new_x, self.min_x, self.max_x)
        self.y = clamp(new_y, self.min_y, self.max_y)


class Carro:
    def __init__(self):
        self.image = pygame.image.load(diretorio_imagens + 'car.png')
        self.rect = self.image.get_rect()
        self.original = self.image

        self.x, self.y = Tamanho_tela_x/2, Tamanho_tela_y/2
        self.virtual_x, self.virtual_y = 567, 456
        self.backup_x, self.backup_y = 567, 456
        self.angle = 270
        self.velocidade = 68 
        self.offset_x, self.offset_y = self.virtual_x - Tamanho_tela_x/2, self.virtual_y - Tamanho_tela_y/2
        self.Dano_carro = 0
            
    def Mudar_direcao(self, direcao):
        if direcao == DIREITA:
                self.angle += (self.velocidade/9) * 0.5 
        elif direcao == ESQUERDA:
                self.angle -= (self.velocidade/9) * 0.5
        if self.angle >= 360:
            self.angle = self.angle - 360
        if self.angle < 0:
            self.angle = 360 + self.angle


    def Movimentacao(self,key):
        #Variavel para informar quado devera ser feito um backup da posicao 
        global contador_backup

        #Variaveis responsaveis pela angulacao do carro
        self.velocidadex = math.sin(self.angle * (math.pi/180)) * (self.velocidade/9)
        self.velocidadey = math.cos(self.angle * (math.pi/180)) * (self.velocidade/9) * -1
        



        #Verificar qual tecla esta sendo pressionada e mover o carro na direcao correta
        if key[K_UP]:
            if self.velocidade < 50:
                self.velocidade += 1
        if key[K_DOWN]:
            if self.velocidade > -50:
                self.velocidade -= 1

        if self.velocidade > 0:
            self.virtual_x += self.velocidadex
            self.virtual_y += self.velocidadey
            if self.velocidade >= 15:
                contador_backup += 1
            if key[K_RIGHT]:
                self.Mudar_direcao(DIREITA)
 
            elif key[K_LEFT]:
                self.Mudar_direcao(ESQUERDA)
            if key[K_UP] == False:
                self.velocidade -= 1
            if key[K_DOWN]:
                self.velocidade -= 1

        if self.velocidade < 0:
            self.virtual_x += self.velocidadex
            self.virtual_y += self.velocidadey
            if self.velocidade <= -3:
                contador_backup += 1
            if key[K_RIGHT]:
                self.Mudar_direcao(DIREITA)
            elif key[K_LEFT]:
                self.Mudar_direcao(ESQUERDA)
            if key[K_DOWN] == False:
                self.velocidade += 1
            if key[K_UP]:
                self.velocidade += 1

        #Reseta posicao do carro
        if key[K_SPACE]:
            self.virtual_x, self.virtual_y = 420, 456
            self.anlge = -90
            self.velocidade = 0

        #Girar a imagem do carro na angulacao correta e obter um retangulo da imagem do carro principal
        self.image =  pygame.transform.rotozoom(self.original, self.angle * -1 , 1.).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center = (self.virtual_x, self.virtual_y))

        #Faz um "backup" das variaveis de movimento pra quando o carro bater voltar pra tais posicoes
        if contador_backup == 10:
            self.backup_x = self.virtual_x
            self.backup_y = self.virtual_y
            contador_backup = 0



    def Colidir_carro(self):
        #Voltar o carro alguma posicoes para dar um efeito de batida e incrementar na variavel Dano
        global contador_backup
        self.velocidade = 0
        self.virtual_x, self.virtual_y = self.backup_x, self.backup_y
        self.Dano_carro += 5
        if self.Dano_carro >= 900:
            print "perdeu"
            self.Dano_carro = 0
        




    def draw(self, screen, camera, loop = True):
    
        if loop:
            branco, preto = (255, 255, 255), (0, 0, 0)
    
            #Desenha a imagem da vaga na tela
            Vaga = screen.blit(pygame.image.load(diretorio_imagens + "Vaga.png"), (-camera.x + 67, -camera.y + 180))
            self.Vaga = Rect(Vaga[0] -10, Vaga[1] - 10, Vaga[2] + 10, Vaga[3] + 20)
    
            #Desenha a imagem do carro na tela
            self.rect = screen.blit(self.image, self.rect.move(-camera.x + 255 , -camera.y - 126))
    
    
            #Dicionario com as coordenadas do local dos carros da fase 
            Dic_fases = {"Fase_1": [ [64, 80], [71, 270], [78, 464], [339, 426],  [545, 122] ]}
    
    
            
    
    
            #Carrega imagens dos carros e define os retangulo do mesmos
            Lista_carros = [pygame.image.load(diretorio_imagens + "carro_objeto_" + str(img) + ".png").convert() for img in range(19)]
            Lista_colorkey = [imagem.set_colorkey(preto) for imagem in Lista_carros]
            Lista_rect_carros = [retangulo.get_rect() for retangulo in Lista_carros]
            Lista_mask_carros = [pygame.mask.from_surface(carro) for carro in Lista_carros]
    
    
    
            #Armazena os pontos principais dos carros
            for Fase in Dic_fases:
    
                for Coord in range(len(Dic_fases[Fase])):
    
                    if Coord >= len(Lista_carros):
                        Coord -= (Coord / 2)
                    
                    pos_1 = Dic_fases[Fase][Coord][0]
                    pos_2 = Dic_fases[Fase][Coord][1]
                    self.image_mask = pygame.mask.from_surface(self.image)
                    self.rect.topleft = (self.rect[0], self.rect[1])
        
                    
                    Lista_rect_carros[Coord] = screen.blit(Lista_carros[Coord],                                                                                                                     (-camera.x + pos_1, -camera.y + pos_2))
    
    
                    Lista_rect_carros[Coord].topleft = (-camera.x + pos_1, -camera.y + pos_2)
                    carros_mask = Lista_mask_carros[Coord]
                    ofset_x, ofset_y = (Lista_rect_carros[Coord].left - self.rect.left),                                                                                         (Lista_rect_carros[Coord].top - self.rect.top)
    
                    if (self.image_mask.overlap(Lista_mask_carros[Coord], (ofset_x, ofset_y)) != None):
                        self.Colidir_carro()   
    
            
    
          
    
            #Quando o carro estiver sobre a vaga: passa de fase
            if self.Vaga.contains(self.rect):
                self.velocidade = 0
                loop = self.Finalizar_nivel(screen, camera)

            return not(loop), loop
        
    

    def Limites_bordas(self, camera):
        #Verificar se o carro esta saindo dos limites da Tela
        if self.velocidade <= 40: 
            #Cria o rect da parede
            Parede = Rect(-camera.x + 37, -camera.y + 71, -camera.x + 735, -camera.y + 490)

            #Detecta se o carro esta sobre a parede
            if not(Parede.contains(self.rect)):
                self.Colidir_carro() 



    def Botoes_jogo(self, screen, camera):
        Dano = screen.blit(pygame.image.load(diretorio_imagens + "Botoes/Dano.png").convert_alpha(), (-camera.x + 535, -camera.y + 542))
        Barra_dano = screen.blit(pygame.image.load(diretorio_imagens + "Botoes/Barra_dano.png"), (-camera.x + 600, -camera.y + 550))
        self.Lista_preenchimendo = [not(bool(x)) for x in range(1, 31)]
        x = 605
        for barra in range(1, 31):
            if barra <= self.Dano_carro/30:
                Preenchimento_barra = screen.blit(pygame.image.load(diretorio_imagens + "Botoes/Preenchimento_barra.png"),                                                                                   (-camera.x + x, -camera.y + 550))
                x += 5

    def Finalizar_nivel(self, screen, camera):
        
        Transparencia = screen.blit(pygame.image.load(diretorio_imagens + "Interacao/Transparencia_menu.png"), (-camera.x , -camera.y))
        Nivel_finalizado = screen.blit(pygame.image.load(diretorio_imagens + "Interacao/Nivel_finalizado.png"),                                                                                   (-camera.x + 300, -camera.y + 150))
        Tempo = screen.blit(pygame.image.load(diretorio_imagens + "Interacao/Tempo.png"), (-camera.x + 200, -camera.y + 200))
        Dano_sofrido = screen.blit(pygame.image.load(diretorio_imagens + "Interacao/Dano_sofrido.png"), (-camera.x + 200, -camera.y + 250))
        Pontos = screen.blit(pygame.image.load(diretorio_imagens + "Interacao/Pontos.png"), (-camera.x + 200, -camera.y + 300))
        Proximo = [(470, 400, 163, 30), pygame.image.load(diretorio_imagens + "Interacao/Proximo_MOFF.png"),                                                                      pygame.image.load(diretorio_imagens + "Interacao/Proximo_MON.png")]

        if Rect(Proximo[0]).collidepoint(pygame.mouse.get_pos()):
            
            screen.blit(Proximo[2], (Proximo[0][0], Proximo[0][1]))
            if pygame.mouse.get_pressed()[0]: 
                return False
            return True    
        else:
            
            screen.blit(Proximo[1], (Proximo[0][0], Proximo[0][1]))
            return True

class Jogo: 

    def Iniciar(self,Tela_menu, Tela_jogo, Tela_cheia_on):

        pygame.init()

        if Tela_cheia_on:
            
            screen= pygame.display.set_mode((Tamanho_tela_x, Tamanho_tela_y), FULLSCREEN|HWSURFACE|DOUBLEBUF)
        else:
            screen= pygame.display.set_mode((Tamanho_tela_x, Tamanho_tela_y), HWSURFACE|DOUBLEBUF)

        screen.fill(0)
        camera = Camera(0, 0, Tamanho_mapa_x - Tamanho_tela_x, Tamanho_mapa_y - Tamanho_tela_y)
     
        background = pygame.image.load(diretorio_imagens + 'Fase_1.png').convert()
     
        carro = Carro() 
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            pygame.display.set_caption("FPS: " + str(clock.get_fps()))
            for event in pygame.event.get():
                    if event.type == QUIT:
                        sys.exit()
                                 
                    if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                    Tela_menu = True
                                    Tela_jogo = False
            pygame.event.pump()
            key = pygame.key.get_pressed()
            carro.Movimentacao(key)
            camera.center_on(carro.virtual_x, carro.virtual_y)
            screen.blit(background, (-camera.x, -camera.y))
            carro.Botoes_jogo(screen, camera)
            Tela_menu, Tela_jogo = carro.draw(screen, camera)
            carro.Limites_bordas(camera)
            pygame.display.flip()
            if Tela_menu:
                return Tela_menu, Tela_jogo

#jogo = Jogo()
#jogo.Iniciar(False, True, False)
