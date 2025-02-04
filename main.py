# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    asteroidfield = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    af = AsteroidField()

    shot = pygame.sprite.Group()
    Shot.containers = (shot, drawable, updatable)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for x in updatable:
            x.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()
            for s in shot:
                if asteroid.collide(s):
                    asteroid.split()
                    s.kill()

        pygame.Surface.fill(screen, "black")

        for x in drawable:
            x.draw(screen)
        
        pygame.display.flip()
        

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()