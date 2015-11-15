import pygame
from pygame.locals import *
 
import math, sys
Tamanho_tela_x = 800
Tamanho_tela_y = 600
 
Tamanho_mapa_x = 800
Tamanho_mapa_y = 600
 
DIREITA = 0
ESQUERDA = 1
 

def clamp(x, minimo, maximo):
    return max(minimo, min(maximo, x))
 
class Camera:
        def __init__(self, min_x, min_y, max_x, max_y):
                self.min_x, self.min_y = min_x, min_y
                self.max_x, self.max_y = max_x, max_y
                self.x = min_x
                self.y = min_y
                print self.x, self.y
        def center_on(self, x, y):
                new_x = x - Tamanho_tela_x / 2
                new_y = y - Tamanho_tela_y / 2
                self.x = clamp(new_x, self.min_x, self.max_x)
                self.y = clamp(new_y, self.min_y, self.max_y)

class Carro:
        def __init__(self):
                self.image = pygame.image.load('car.png')#.convert_alpha()
                #self.image.set_colorkey((255, 255, 255))
                self.rect = self.image.get_rect()
 
                self.original = self.image
 
                self.x, self.y = Tamanho_tela_x/2, Tamanho_tela_y/2
                self.virtual_x, self.virtual_y = 567, 456
 
                self.angle = -90
                self.velocidade = 60 
                self.offset_x, self.offset_y = self.virtual_x - Tamanho_tela_x/2, self.virtual_y - Tamanho_tela_y/2
                
                
        def Mudar_direcao(self, direcao):
                if direcao == DIREITA:
                        self.angle += (self.velocidade/10) * 0.5 
                elif direcao == ESQUERDA:
                        self.angle -= (self.velocidade/10) * 0.5
 
        def Movimentacao(self,key):
                velocidadex = math.sin(self.angle * (math.pi/180)) * (self.velocidade/10)
                velocidadey = math.cos(self.angle * (math.pi/180)) * (self.velocidade/10) * -1

                if key[K_UP]:
                    if self.velocidade < 40:
                        self.velocidade += 1
                if key[K_DOWN]:
                    if self.velocidade > -40:
                        self.velocidade -= 1

                if self.velocidade > 0:
                    self.virtual_x += velocidadex
                    self.virtual_y += velocidadey
                    if key[K_RIGHT]:
                        self.Mudar_direcao(DIREITA)
 
                    elif key[K_LEFT]:
                        self.Mudar_direcao(ESQUERDA)
                    if key[K_UP] == False:
                        self.velocidade -= 1
                    if key[K_DOWN]:
                        self.velocidade -= 1

                if self.velocidade < 0:
                    self.virtual_x += velocidadex
                    self.virtual_y += velocidadey
                    if key[K_RIGHT]:
                        self.Mudar_direcao(DIREITA)
                    elif key[K_LEFT]:
                        self.Mudar_direcao(ESQUERDA)
                    if key[K_DOWN] == False:
                        self.velocidade += 1
                    if key[K_UP]:
                        self.velocidade += 1
               
                self.image = pygame.transform.rotozoom(self.original, self.angle * -1, 1)
                self.rect = self.image.get_rect(center = (self.virtual_x , self.virtual_y ))
        def draw(self, screen, camera):
            screen.blit(self.image, self.rect.move(-camera.x + 258, -camera.y - 126))
            

    

        def Blita_carro_colisao(self,Tela, camera):
            #Carrega as imagens dos carros:

            self.Lista_carros = [pygame.image.load("carro_objeto_" + str(img) + ".png") for img in range(5)]
            self.Lista_rect_carros = []


            indice = 0
            for coord in range(10, 850, 190):
                Imagem = self.Lista_carros[indice]#Imagem = pygame.transform.rotozoom(self.Lista_carros[indice], 90, 1)
                obter_rect_carro = self.Lista_carros[indice].get_rect()
                rect_carro = Rect(coord, 80, 170, 80)
                self.Lista_rect_carros.append(rect_carro)
                Tela.blit(Imagem, (-camera.x, -camera.y))
                indice += 1

            for colisao in range(len(self.Lista_rect_carros)):
                if self.rect.colliderect(-camera.x, -camera.y):
                    pass
                    
                    
        def Colide_vaga(self,vaga):
            vaga_tst =  self.image

            b = pygame.sprite.Sprite()
            c = pygame.sprite.Sprite()
            b.image = self.image.convert()
            c.image = vaga
            if pygame.sprite.collide_mask(b.image, c.image):
                print "ok"

            #im_tst = Rect(self.image)
                       #if im_tst.contains(vaga_tst):
             #   print "Parabens"
                #Tela_menu = True
                #Tela_jogo = False
                #return Tela_menu, Tela_jogo
class Jogo: 


    def Iniciar(self, Tela_menu, Tela_jogo):
        pygame.init()

        screen = pygame.display.set_mode((Tamanho_tela_x, Tamanho_tela_y), HWSURFACE|DOUBLEBUF)
        screen.fill(0)
        background = pygame.image.load('Fase_1.png').convert()
        vaga = pygame.image.load('Vaga.png')
        carro = Carro() 
        clock = pygame.time.Clock()
        camera = Camera(0, 0, Tamanho_mapa_x - Tamanho_tela_x, Tamanho_mapa_y - Tamanho_tela_y)
     
        
        while True:
            Tela_menu = False
            Tela_jogo = True
            clock.tick(60)
            for event in pygame.event.get():
                    if event.type == QUIT:
                        sys.exit()
                                 
                    if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                    Tela_menu = True
                                    Tela_jogo = False
                                    return Tela_menu, Tela_jogo
            pygame.event.pump()
            key = pygame.key.get_pressed()
            carro.Movimentacao(key)
            camera.center_on(carro.virtual_x, carro.virtual_y)
            #screen.fill((0, 0, 0))
            screen.blit(background, (-camera.x, -camera.y))
            screen.blit(vaga, (-camera.x + 62, -camera.y + 267))

            print -camera.x, -camera.y
            carro.draw(screen, camera)
            #Tela_menu, Tela_jogo = carro.Colide_vaga(Tela_menu, Tela_jogo)
            carro.Colide_vaga(vaga)
            carro.draw(screen, camera)
            pygame.display.flip()
            print camera.x, camera.y


        return Tela_menu, Tela_jogo

Tela_menu = True
Tela_jogo = False
jogo = Jogo()
jogo.Iniciar(Tela_menu, Tela_jogo)
#Tela_menu, Tela_jogo = jogo.Iniciar(1,2)#Tela_menu, Tela_jogo)
#Tela_menu,Tela_jogo = jogo.Iniciar(Tela_menu, Tela_jogo)
