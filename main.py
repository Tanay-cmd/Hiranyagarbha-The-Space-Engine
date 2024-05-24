import pygame
<<<<<<< HEAD
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

=======
#pygame initlalizatio
pygame.init()

#game setup
WIDTH, HEIGHT = 1000, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FrameRate = 60

#constants
AU = 149.6e9*1000
SCALE = 250/AU
G = 6.67428e-11  
TIMESTEP = 3600*640000

#blue print for the planets
class planets:
    def __init__(self, position,  radius, mass, color, intial_vel):
        self.position = pygame.math.Vector2(position)
        self.velocity = pygame.math.Vector2(intial_vel)
        self.radius = radius
        self.mass = mass
        self.color = color

    #outputs a force vector between 2 bodies
    def attraction(self, other):
        dist_vect = other.position - self.position
        distance = dist_vect.length()
        if distance == 0:
            return pygame.math.Vector2(0, 0)
        force = (G * self.mass * other.mass)/distance**2
        force_vector = force * dist_vect.normalize()
        return force_vector
    
    #calculats the total force due to each planet on each planet, one at a time 
    #and updates the position
    def update(self):
        total_force = pygame.math.Vector2(0, 0)
        for planet in planets:
            total_force += self.attraction(planet)
        self.accleration = total_force/self.mass
        self.velocity += self.accleration * TIMESTEP 
        self.position += self.velocity * TIMESTEP
        self.draw()
 
  #drawing method
    def draw(self):
        # x and y are adjusted to the center of the screen
        x = (self.position.x * SCALE + WIDTH / 2 - self.radius)
        y = (self.position.y * SCALE + HEIGHT / 2 - self.radius)
        pygame.draw.ellipse(SCREEN, self.color, (x, y, self.radius * 2, self.radius * 2))


#intializing the objects
sun = planets((0, 0), 50, 1.989e30, 'YELLOW', (0, 0))
earth = planets((AU, 0), 10, 5.972e24, 'BLUE', (0, 800))
planets = [sun, earth]

#basic game loop begins here./
run = True
while run:

    #below is event handler
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

    #filling the screen with black color
    SCREEN.fill('black')

    for planet in planets:
        planet.update()


    pygame.display.update()

    #clocking the framerate, loop can run only 60 times per seconds
    clock.tick(FrameRate)
>>>>>>> 0dd0b288af48a82e92eb225fa969faf5017bdff1
pygame.quit()
