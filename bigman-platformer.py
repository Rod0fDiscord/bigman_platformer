import pygame
import time
import os

pygame.init()

#create the screen
background_color = (195, 195, 0)
screen = pygame.display.set_mode((800, 600))

#load in the assets
assets_path = "assets"
def load_assets(assets_path):
    dir = os.scandir(assets_path,)
    print("Files and Directories in % s:" % assets_path)
    images = {}
    for dir_path, _, file_names in os.walk(assets_path):
        for file_name in file_names:
            if file_name.endswith(".png"):
                file_path = os.path.join(dir_path, file_name)
                images[file_name[:-4]] = pygame.image.load(file_path).convert_alpha()
    return images

load_assets(assets_path)

def refresh(background_color):
    #update the screen
    screen.fill(background_color)


running = True
while running:
    
    refresh(background_color)