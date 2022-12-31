import pygame
import time
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
    screen.fill(background_color)
    screen.blit(background, (0, 0))
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
        self.gravity = 0

class Player():
    def __init__(self):
        self.velocity = pygame.Vector2(0,0)
        self.x_position = 720
        self.y_position = 400
        


#variables
background_color = (195, 195, 0)
screen = pygame.display.set_mode((800, 600))
screen.fill(background_color)

assets = load_assets(assets_path)
background = assets['brick']

running = True
#actually starting the loop
while running:
    
    refresh(background_color)

    check_for_quit()