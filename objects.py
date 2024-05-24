import pygame
from game_setup import *
pygame.init()

class Planet:
    def __init__(self, position, radius, mass, color, vel_vect, SCREEN, is_Human):
        self.position = pygame.math.Vector2(position)
        self.velocity = pygame.math.Vector2(vel_vect)
        self.radius = radius
        self.mass = mass
        self.color = color
        self.screen = SCREEN
        self.is_Human = is_Human
        
    # Outputs a force vector between 2 bodies
    def attraction(self, other):
        dist_vect = other.position - self.position
        distance = dist_vect.length()
        if distance == 0:
            return pygame.math.Vector2(0, 0)
        force = (G * self.mass * other.mass) / distance**2
        force_vector = force * dist_vect.normalize()
        return force_vector

    # Calculates the total force due to each planet on each planet, one at a time
    # and updates the position
    def update(self, planets):
        total_force = pygame.math.Vector2(0, 0)
        for planet in planets:
            if planet != self:
                total_force += self.attraction(planet)
        acceleration = total_force / self.mass
        self.velocity += acceleration * TIMESTEP
        self.position += self.velocity * TIMESTEP
        self.draw()

    # Drawing method
    def draw(self):
        # x and y are adjusted to the center of the screen

        x = (self.position.x * SCALE + WIDTH / 2 - self.radius)
        y = (self.position.y * SCALE + HEIGHT / 2 - self.radius)
        
        pygame.draw.ellipse(self.screen, self.color, (x, y, self.radius * 2, self.radius * 2))

