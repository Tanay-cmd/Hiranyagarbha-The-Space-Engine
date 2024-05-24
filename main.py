import pygame
from game_setup import *
from objects import *
# Pygame initialization
pygame.init()




SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# Blueprint for the planets


# Initialize the objects
sun = Planet((0, 0), 50, 1.989e30, (255, 255, 0), (0, 0), SCREEN, False)
venus = Planet((0.5 * AU, 0), 10, 4.867e24, (0, 0, 255), (0, 35_020), SCREEN, False)
earth = Planet((AU, 0), 10, 5.972e24, (0, 0, 255), (0, 29_780), SCREEN, False)
planet_list = [earth, sun, venus]
initial_pos = None

# Basic game loop begins here
run = True
clock = pygame.time.Clock()
while run:
    mouse_pos = pygame.mouse.get_pos()
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Adds the object with mouse input, first click as initial position of vector and second click to set velocity
        if event.type == pygame.MOUSEBUTTONDOWN:
            if initial_pos:
                vel_vector = pygame.math.Vector2(mouse_pos) - pygame.math.Vector2(initial_pos)
                if vel_vector.length() > 0:
                    vel_vector = vel_vector * 90  # Scale the velocity as needed
                    new_planet = Planet(((initial_pos[0] - WIDTH/2) * (1/SCALE) , (initial_pos[1] - HEIGHT/2) * (1/SCALE)), 13, 5.972e20, (255, 0, 0), (vel_vector.x, vel_vector.y), SCREEN, True)
                    planet_list.append(new_planet)
                initial_pos = None
            else:
                initial_pos = (mouse_pos) 


    # Filling the screen with black color
    SCREEN.fill((0, 0, 0))

    for planet in planet_list:
        planet.update(planet_list)

    # Draw a circle to show where the new planet will be placed
    if initial_pos:
        pygame.draw.circle(SCREEN, (255, 0, 0), initial_pos, 13)
        pygame.draw.line(SCREEN, (255, 255, 255), initial_pos, mouse_pos, 2)

    pygame.display.update()

    # Clocking the framerate, loop can run only 60 times per second
    clock.tick(FrameRate)

pygame.quit()
