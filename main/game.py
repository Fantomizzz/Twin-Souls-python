import pygame

run_bool = True


screen = pygame.display.set_mode() #initialise l'écran

space_bool = False
timer_event = pygame.event.custom_type()
pygame.time.set_timer(timer_event, 0)

#écran de démarrage
fond_démarrage = pygame.image.load("fond_démarrage.png").convert() #load le fond et un bouton (les autres sont load après car utilisés dans d'autres menu)
nouvelle_partie = pygame.image.load("nouvelle_partie.png").convert_alpha()
load_sauvegarde = pygame.image.load("load_sauvegarde.png").convert_alpha()

démarrage = True  #initialise l'écran de démarrage
démarrage_suite = False

démarrer_string = "Cliquer pour continuer"   #initialise le bouton "cliquer pour continuer" au démarrage 
pygame.font.init() 
démarrer_font = pygame.font.Font(None, 50) 
start_string = démarrer_font.render(démarrer_string, 1, (0, 0, 0)) 


#jeu

fond = pygame.image.load("fond.png").convert() #load le fond


perso = pygame.image.load("perso.png").convert_alpha() #load le perso (le _alpha permets d'éviter que l'image est un fond)
x = 1080  #coordonées du perso au début
y = 470

vie_1_perso = pygame.image.load("vie.png").convert_alpha() #load les vies
vie_2_perso = pygame.image.load("vie.png").convert_alpha()
vie_3_perso = pygame.image.load("vie.png").convert_alpha()

x_vie_1 = 0
x_vie_2 = 80
x_vie_3 = 160


argent_var = 0  #initialise l'argent 
pygame.font.init()  #initialize le font (pour afficher la variable argent)
argent_font = pygame.font.Font(None, 50) #caractéristique du fond (police et taille de ce qu'on veut afficher je cois)
argent = argent_font.render(str(argent_var), 1, (0, 0, 0)) #affiche notre variable (le (0,0,0) correspond à la couleur)


argent_image = pygame.image.load("argent.png").convert_alpha() #load l'icône qui symbolise notre argent (ici la pyramide violette)


menu_pause_bool = False #vérifie si le menu pause est ouvert
fond_menu = pygame.image.load("fond_noir.jpg").convert_alpha() #load le fond du menu pause
fond_menu.set_alpha(200)                                       # mets la transparence du fond à 200 
pygame.Surface.convert_alpha(fond_menu)                        # applique le changement de transparence 

reprendre = pygame.image.load("reprendre.png").convert_alpha() #load les images "exit" et "resume" du menu pause
exit_game = pygame.image.load("exit.png").convert_alpha() 
exit_menu = pygame.image.load("exit_menu.png").convert_alpha() 
save = pygame.image.load("save.png").convert_alpha()
confirmation = pygame.image.load("confirmation.png").convert_alpha()
confirmation_bool = True



menu_inventaire_bool = False #vérifie si le menu "inventaire" est ouvert
carte = pygame.image.load("carte.png").convert_alpha()  
inventaire = pygame.image.load("inventaire.png").convert_alpha()
nb_menu = 2 #nombre de menu
menu_actuel = 0


while run_bool : #boucle infini qui garde le jeu ouvert
    for event in pygame.event.get(): #gère les évènements
        if event.type == pygame.QUIT: #si on appuie sur quitter(la croix pour fermer la fenêtre), la boucle s'arrête 
                run_bool = False

#écran de démarrage
    if démarrage:
        screen.blit(fond_démarrage, (0,0))
        screen.blit(start_string, (800, 630))
        keys = pygame.key.get_pressed() #vérifie si un bouton est pressé

        if event.type == pygame.MOUSEBUTTONDOWN or démarrage_suite:       #lance le menu qui suit l'écran de démarrage
            screen.blit(fond_démarrage, (0,0))
            screen.blit(fond_menu, (0,0))
            screen.blit(nouvelle_partie, (820,400))
            screen.blit(load_sauvegarde, (820,500))
            screen.blit(exit_game, (820, 600))

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and démarrage_suite : 
                x_clic, y_clic = pygame.mouse.get_pos()

                if x_clic > 800 and x_clic < 1125 and y_clic > 380 and y_clic < 470:
                    démarrage = False

                if x_clic > 800 and x_clic < 1125 and y_clic > 500 and y_clic < 585:
                    print("load") 

                if x_clic > 800 and x_clic < 1125 and y_clic > 600 and y_clic < 685:
                    run_bool = False         

            
            pygame.time.wait(100)
            démarrage_suite = True

    else:

# config touche
        keys = pygame.key.get_pressed() #vérifie si un bouton est pressé
        
        if menu_pause_bool == False and menu_inventaire_bool == False:
            pygame.mouse.set_visible(False)

        if keys[pygame.K_ESCAPE]:  # si échap est pressé, ouvre le menu de pause
            pygame.time.wait(200)   # permets d'éviter que pygame considère qu'on a appuyé 2 fois alors qu'on appuie juste assez longtemps pour que la boucle s'éxécute 2 fois
            if menu_pause_bool == False: #ouvre le menu si il était fermé (active la boucle du menu)
                menu_pause_bool = True
                menu_inventaire_bool = False      #ferme le menu si il était ouvert (désactive la boucle)
               
            else:
                menu_pause_bool = False      #ferme le menu si il était ouvert (désactive la boucle)
                

        if menu_pause_bool == False:
            
            if keys[pygame.K_e]:        #touche e pour ouvrir le menu inventaire, carte...
                pygame.time.wait(200)   # permets d'éviter que pygame considère qu'on a appuyé 2 fois alors qu'on appuie juste assez longtemps pour que la boucle s'éxécute 2 fois
                if menu_inventaire_bool == False:     #ouvre le menu si il était fermé (active la boucle du menu)
                    menu_inventaire_bool = True
                else:
                    menu_inventaire_bool = False      #ferme le menu si il était ouvert (désactive la boucle)
                    screen.blit(carte, (-8000,300))         #déplace les images du menu pour qu'elle ne soit plus visible
                    screen.blit(inventaire, (-8000,300))

            if menu_inventaire_bool == False:
                
                 
                if keys[pygame.K_SPACE] and not(space_bool):               #bouton saut (à fix)
                    pygame.time.wait(200) 
                    y -= 300
                    screen.blit(fond, (-470, -80))#réinitialise le fond
                    screen.blit(vie_1_perso, (0,0)) # affiche les vies aux coordonnées demandées
                    screen.blit(vie_2_perso, (80,0))
                    screen.blit(vie_3_perso, (160,0))
                    argent = argent_font.render(str(argent_var), 1, (255, 255, 255)) #affiche la variable argent
                    screen.blit(argent, (1820, 50))  # affiche aux coordonnées demandées
                    screen.blit(argent_image, (1700,15))

                    screen.blit(perso, (x,y))  #place le personnage à ses nouvelles coordonnées
                    pygame.display.flip() #mets l'écran à jour 
                    
                    space_bool = True
                    pygame.time.set_timer(timer_event, 600)


                if event.type == timer_event and space_bool:
                    y += 300
                    screen.blit(fond, (-470, -80))#réinitialise le fond
                    screen.blit(vie_1_perso, (0,0)) # affiche les vies aux coordonnées demandées
                    screen.blit(vie_2_perso, (80,0))
                    screen.blit(vie_3_perso, (160,0))
                    argent = argent_font.render(str(argent_var), 1, (255, 255, 255)) #affiche la variable argent_var
                    screen.blit(argent, (1820, 50))  # affiche aux coordonnées demandées
                    screen.blit(argent_image, (1700,15))

                    screen.blit(perso, (x,y))  #place le personnage à ses nouvelles coordonnées
                    pygame.display.flip() #mets l'écran à jour 

                    pygame.time.set_timer(timer_event, 0)
                    space_bool = False
                    pygame.time.wait(200)
                                        

                if keys[pygame.K_LEFT]:  #si flèche gauche pressé alors on déplace le joueur
                    x += -5
                elif keys[pygame.K_RIGHT]: #si flèche droite pressé
                    x += 5
                                    
                if keys[pygame.K_i]:         #simule ce que fait le compteur (dans le futur détecter quand le joueur ramasse l'objet où le dépense)
                    argent_var += 1
                    pygame.time.wait(200)

                if keys[pygame.K_v]:        #simule le retrait / ajout de vie (dans le futur créer un système de colision avec les monstres et de régénération)
                    if x_vie_3 == 160:
                        x_vie_3 = -1000
                    elif x_vie_2 == 80:
                        x_vie_2 = -1000
                    else:
                        x_vie_1 = -1000
                    pygame.time.wait(200)

                if keys[pygame.K_b]:        #simule le retrait / ajout de vie (dans le futur créer un système de colision avec les monstres et de régénération)
                    if x_vie_1 != 0:
                        x_vie_1 = 0
                    elif x_vie_2 != 80:
                        x_vie_2 = 80
                    else:
                        x_vie_3 = 160
                    pygame.time.wait(200)


#config image
        screen.blit(fond, (-470, -80))#réinitialise le fond
    
        screen.blit(vie_1_perso, (x_vie_1,0)) # affiche les vies aux coordonnées demandées
        screen.blit(vie_2_perso, (x_vie_2,0))
        screen.blit(vie_3_perso, (x_vie_3,0))


        argent = argent_font.render(str(argent_var), 1, (255, 255, 255)) #affiche la variable argent
        screen.blit(argent, (1820, 50))  # affiche aux coordonnées demandées
        screen.blit(argent_image, (1700,15))

        screen.blit(perso, (x,y))  #place le personnage à ses nouvelles coordonées
        
        if keys[pygame.K_TAB]:              #carte qui s'ouvre quand on reste appuyer sur tab
            screen.blit(carte, (450, 100))

#config menu
        if menu_pause_bool:
            pygame.mouse.set_visible(True)
            if confirmation_bool:
                screen.blit(fond_menu, (0, 0))   #affiche le fond et les images des boutons du menu
                screen.blit(reprendre, (865, 300))
                screen.blit(save, (890, 400))
                screen.blit(exit_menu, (890, 500))
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and menu_pause_bool) or not(confirmation_bool): 
                x_clic, y_clic = pygame.mouse.get_pos()
                
                if confirmation_bool :
                    if x_clic > 860 and x_clic < 1105 and y_clic > 295 and y_clic < 375:
                        menu_pause_bool = False

                    if x_clic > 890 and x_clic < 1075 and y_clic > 395 and y_clic < 475:
                        print("save") 

                    if (x_clic > 890 and x_clic < 1075 and y_clic > 495 and y_clic < 575) or not(confirmation_bool):
                        screen.blit(fond_menu, (0, 0)) 
                        screen.blit(confirmation, (820, 257))
                        confirmation_bool = False
                        pygame.time.wait(200)

                else:   
                    screen.blit(fond_menu, (0, 0)) 
                    screen.blit(confirmation, (820, 257))

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and x_clic > 840 and x_clic < 955 and y_clic > 510 and y_clic < 560:
                        run_bool = False

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and x_clic > 980 and x_clic < 1100 and y_clic > 510 and y_clic < 560:
                        confirmation_bool = True
                        screen.blit(fond_menu, (0, 0))   #affiche le fond et les images des boutons du menu
                        screen.blit(reprendre, (865, 300))
                        screen.blit(save, (890, 400))
                        screen.blit(exit_menu, (890, 500))

                        pygame.time.wait(200)


           

        if menu_inventaire_bool:
            pygame.mouse.set_visible(True)

            if menu_actuel % nb_menu == 0:      #affiche le menu 0 et prend en compte le cas où on dépasse le nombre de menu existant 
                screen.blit(fond_menu, (0, 0))
                screen.blit(carte, (450,100))

            if menu_actuel % nb_menu == 1:
                screen.blit(fond_menu, (0, 0))
                screen.blit(inventaire, (440,200))
           
            if keys[pygame.K_RIGHT]:           # permets de changer de menu (avec un minuteur pour éviter que pygame croit qu'on appuie plusieurs fois)
                menu_actuel += 1
                pygame.time.wait(250)

            if keys[pygame.K_LEFT]: 
                menu_actuel -= 1
                pygame.time.wait(250)


        
       
    pygame.display.flip() #mets l'écran à jour 







