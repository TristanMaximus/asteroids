import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rotation_angle = random.uniform(20, 50)
        new_velocity_first = self.velocity.rotate(rotation_angle)
        new_velocity_second = self.velocity.rotate(-rotation_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_first = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_second = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_first.velocity = new_velocity_first * ASTEROID_CHUNK_VELOCITY_MULTIPLIER
        new_asteroid_second.velocity = new_velocity_second * ASTEROID_CHUNK_VELOCITY_MULTIPLIER
