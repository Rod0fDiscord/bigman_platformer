import pygame
import time
import json
import os

pygame.init()

#functions

#load in the assets
assets_path = "assets"
def load_assets(assets_path):
    dir = os.scandir(assets_path,)
    images = {}
    for dir_path, _, file_names in os.walk(assets_path):
        for file_name in file_names:
            if file_name.endswith(".png"):
                file_path = os.path.join(dir_path, file_name)
                images[file_name[:-4]] = pygame.image.load(file_path).convert_alpha()
    return images

def refresh(background_color):
    #update the screen
    #background
    screen.fill(background_color)
    screen.blit(background, (0, 0))

    #objects
    for i in walls:
        screen.blit(pygame.transform.scale(assets['wall'], (20, 20)), walls[i])
    for i in platforms:
        screen.blit(pygame.transform.scale(assets['platform'], (20, 5)), platforms[i])
    for i in spikes:
        screen.blit(pygame.transform.scale(assets['spike'], (20, 20)), spikes[i])
    for i in spikes_left:
        screen.blit(pygame.transform.scale(assets['spike_left'], (20, 20)), spikes_left[i])
    for i in spikes_right:
        screen.blit(pygame.transform.scale(assets['spike_right'], (20, 20)), spikes_right[i])
    for i in spikes_down:
        screen.blit(pygame.transform.scale(assets['spike_down'], (20, 20)), spikes_down[i])
    
    #player
    screen.blit(pygame.transform.scale(assets['neutral'], (30, 60)), (Player.position))

    #display changes
    pygame.display.update()

def check_for_quit():
    for event in pygame.event.get():
      
        if event.type == pygame.QUIT:
            running = False

#classes
class Levels():
    def __init__(self):
        self.walls = 0
        self.spikes = 0
        self.gravity = pygame.Vector2(0,5)
    
    def load(self):
        global spikes
        global walls
        global spikes_left
        global spikes_right
        global spikes_down
        global platforms
        with open(r"levels\level_1\level.json") as file:
            level_data = json.load(file)
            spikes = level_data['spikes']
            spikes_left = level_data['spikes_left']
            spikes_right = level_data['spikes_right']
            spikes_down = level_data['spikes_down']
            walls = level_data['walls']
            platforms = level_data['platforms']
        for i in spikes:
            x, y = spikes[i]
            x -= 100
            y -= 100
            spikes[i] = (x, y)
        for i in spikes_left:
            x, y = spikes_left[i]
            x -= 100
            y -= 100
            spikes_left[i] = (x, y)
        for i in spikes_right:
            x, y = spikes_right[i]
            x -= 100
            y -= 100
            spikes_right[i] = (x, y)
        for i in spikes_down:
            x, y = spikes_down[i]
            x -= 100
            y -= 100
            spikes_down[i] = (x, y)
        for i in walls:
            x, y = walls[i]
            x -= 100
            y -= 100
            walls[i] = (x, y)
        for i in platforms:
            x, y = platforms[i]
            x -= 100
            y -= 100
            platforms[i] = (x, y)

class Player():
    def __init__(self):
        self.velocity = pygame.Vector2(0,0)
        self.position = (720, 460)
        self.on_floor = True
    
    def movement(self):
        if keys[pygame.K_SPACE]:
            if self.on_floor:
                self.velocity += (0, - 800)
                self.on_floor = False
            #elif self.y_velocity > 0:
                #self.velocity += (0, -3)
            #else:
                #self.velocity += (0, -4.5)
        self.velocity += Levels.gravity
        print(self.position, " ", self.velocity)
        self.position += self.velocity * dt
    
    def collision(self):
        self.x, self.y = self.position
        self.x_velocity, self.y_velocity = self.velocity
        for i in walls:
            self.wall_x, self.wall_y = walls[i]
            if self.y + 60 > self.wall_y:
                self.y = walls[i][1]
                print(walls[i][1])
                self.on_floor = True
        if self.on_floor:
            self.y_velocity -= self.y_velocity
        self.position = (self.x, self.y)
        self.velocity = pygame.Vector2(self.x_velocity, self.y_velocity)



#variables
background_color = (195, 195, 0)
screen = pygame.display.set_mode((800, 600))
screen.fill(background_color)
assets = load_assets(assets_path)
background = assets['brick']


#variables
Player.__init__(Player)
Levels.__init__(Levels)
Levels.load(Levels)
clock = pygame.time.Clock()
running = True
previous_time = time.time()
#actually starting the loop
while running:
    clock.tick(600)
    dt = time.time() - previous_time
    previous_time = time.time()
    keys = pygame.key.get_pressed()
    Player.movement(Player)
    Player.collision(Player)
    
    refresh(background_color)

    check_for_quit()