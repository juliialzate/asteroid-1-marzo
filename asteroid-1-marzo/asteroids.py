import pygame
from pygame.locals import *
import sys
from ship import *

size = width, height = 800, 600

screen = pygame.display.set_mode(size)

def main():

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("sonidos/viento.mp3")
    pygame.mixer.music.play(1)

  
    background_image = pygame.image.load ("imagenes/space.png")
    background_rect = background_image.get_rect ()
        
    pygame.display.set_caption("Asteroids")

    ship = Ship(size)
        
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        ship.update()   
        screen.blit(background_image, background_rect)
        screen.blit(ship.imagen, ship.rect)
    
        for bullet in ship.bullets: 
            bullet.update()
            if bullet.alcance == 0:
                ship.bullets.remove(bullet)
            screen.blit(bullet.image, bullet.rect)
        screen.blit(ship.image, ship.rect)
        
        pygame.display.update()
        pygame.time.delay(10)
            
if __name__ == "__main__":
    main()
        