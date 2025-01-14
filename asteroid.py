from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (dt * self.velocity)

    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        exitAngle = random.uniform(20, 50)
        v1 = pygame.math.Vector2.rotate(self.velocity, exitAngle)
        v2 = pygame.math.Vector2.rotate(self.velocity, -exitAngle)

        newRad = self.radius- ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, newRad)
        a2 = Asteroid(self.position.x, self.position.y, newRad)

        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2


