import sys
import random
import pygame



class Jeu: 
    # contenir toutes les variables et aussi toutes les fonctions utiles pour le bon déroulement du jeu.

    def __init__(self): 

        self.ecran = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Jeu Snake')
        self.jeu_encours = True
        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0
        self.serpent_dimension = 10
        
        #créer la position pour la pomme
        self.pomme_position_x = random.randrange(110,690,10)
        self.pomme_position_y = random.randrange(110,590,10)
        self.pomme = 10
        
        #fixer les fps
        
        self.clock = pygame.time.Clock()
        
        #Créer une liste qui rescense toutes les positions du serpent
        self.position_serpent = []
        
        # Créer la variable en rapport avec la taille du serpent
        self.taille_serpent = 1
        
    def fonction_principale(self):
            #permet de gerer les evenements, permet d'afficher certains composants du jeu

            while self.jeu_encours:
                for evenement in pygame.event.get():
                    if evenement.type ==  pygame.QUIT:
                        sys.exit()
                        
                #Creer les évenements qui permettent de faire bouger le serpent          
                    if evenement.type == pygame.KEYDOWN:
                        if evenement.key == pygame.K_RIGHT:
                            self.serpent_direction_x = 1
                            self.serpent_direction_y = 0
                            
                        if evenement.key == pygame.K_LEFT:
                             self.serpent_direction_x = -1
                             self.serpent_direction_y = 0
                             
                        if evenement.key == pygame.K_DOWN:
                            self.serpent_direction_x = 0
                            self.serpent_direction_y = 1 
                            
                        if evenement.key == pygame.K_UP:
                            self.serpent_direction_x = 0
                            self.serpent_direction_y = -1   
                           
                           
                           
                     #  Empecher le serpent de sortir des limites       
                    if self.serpent_position_x <= 100 or self.serpent_position_x >= 700\
                        or self.serpent_position_y <= 100 or self.serpent_position_y >= 600:
                            sys.exit()
                  
                  
                             
                    # faire bouger le serpent     
                self.serpent_position_x += self.serpent_direction_x
                self.serpent_position_y += self.serpent_direction_y
                
                
                #condition si le serpent mange la pomme
                if self.pomme_position_y == self.serpent_position_y and self.pomme_position_x == self.serpent_position_x:
                 

                    self.pomme_position_x == random.randrange(110,690,10)
                    self.pomme_position_y == random.randrange(110,590,10)
                
                 #Augmenter la taille du serpent
                    self.taille_serpent += 1
           
                
                #Créer une liste qui stocke la position de la tête du serpent
                
                la_tete_du_serpent = []
                la_tete_du_serpent.append(self.serpent_position_x)
                la_tete_du_serpent.append(self.serpent_position_y)
                
                #append dans la liste de la tête du serpent
                
                self.position_serpent.append(la_tete_du_serpent)
                
                #condition  pour résoudre le problème des positions du serpent  avec la taille du serpent
                
                if len(self.position_serpent) > self.taille_serpent:
                    self.position_serpent.pop(0)
                    print(self.position_serpent)
                
                
                self.ecran.fill((0,0,0))
                
                #Afficher les autres parties du serpent
                pygame.draw.rect(self.ecran,(0,255,0),(self.serpent_position_x,self.serpent_position_y,self.serpent_dimension,self.serpent_dimension))
                
                #Afficher la pomme
                pygame.draw.rect(self.ecran,(255,0,0),(self.pomme_position_x,self.pomme_position_y,self.pomme,self.pomme))
                
                #Afficher le serpent
                
                for partie_du_serpent in self.position_serpent:
                    pygame.draw.rect(self.ecran,(0,255,0),(partie_du_serpent[0],partie_du_serpent[1],self.serpent_dimension,self.serpent_dimension))
            
            
                # Si le serpent se "mord" la queue 
                
                for partie_du_serpent  in self.position_serpent[:-1]:
                    if la_tete_du_serpent == partie_du_serpent:
                        sys.exit()
            
                #afficher les limites
                self.creer_limites()
                #Fixer les fps à 120
                self.clock.tick(120)
                
                pygame.display.flip()
                
                
    def creer_limites(self):
        pygame.draw.rect(self.ecran,(255,255,255),(100,100,600,500),3)


if __name__ == '__main__':
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit() 


  