#imports
import pygame
import json
import os
from enum import Enum


#functions
def load_assets(assets_path):
    dir = os.scandir(assets_path,)
    images = {}
    for dir_path, _, file_names in os.walk(assets_path):
        for file_name in file_names:
            if file_name.endswith(".png"):
                file_path = os.path.join(dir_path, file_name)
                images[file_name[:-4]] = pygame.image.load(file_path).convert_alpha()
    return images

def check_for_quit():
    for event in pygame.event.get():
      
        if event.type == pygame.QUIT:
            running = False

def refresh(background_color):
    #update the screen
    #background
    screen.fill(background_color)
    screen.blit(background, (100, 100))
    #GUI
    #GUI objects
    screen.blit(pygame.transform.scale(assets['undo'], (50, 50)), (200, 25))
    screen.blit(pygame.transform.scale(assets['eraser'], (50, 50)), (300, 25))
    screen.blit(pygame.transform.scale(assets['wall'], (50, 50)), (400, 25))
    screen.blit(pygame.transform.scale(assets['spike'], (50, 50)), (500, 25))
    screen.blit(pygame.transform.scale(assets['spike_left'], (50, 50)), (600, 25))
    screen.blit(pygame.transform.scale(assets['spike_down'], (50, 50)), (700, 25))
    screen.blit(pygame.transform.scale(assets['spike_right'], (50, 50)), (800, 25))
    #GUI elements
    #GUI border
    if curr_object == current_object.undo:
        screen.blit(pygame.transform.scale(assets['border'], (65, 65)), (192.5, 17.5))
    if curr_object == current_object.erase:
        screen.blit(pygame.transform.scale(assets['border'], (65, 65)), (292.5, 17.5))
    if curr_object == current_object.wall:
        screen.blit(pygame.transform.scale(assets['border'], (65, 65)), (392.5, 17.5))
    if curr_object == current_object.spike:
        if Mouse.spike_rotation == 0:
            screen.blit(pygame.transform.scale(assets['border'], (65, 65)), (492.5, 17.5))
        if Mouse.spike_rotation == 1:
            screen.blit(pygame.transform.scale(assets['border'], (65, 65)), (592.5, 17.5))
        if Mouse.spike_rotation == 2:
            screen.blit(pygame.transform.scale(assets['border'], (65, 65)), (692.5, 17.5))
        if Mouse.spike_rotation == 3:
            screen.blit(pygame.transform.scale(assets['border'], (65, 65)), (792.5, 17.5))
    #GUI key notations
    screen.blit(pygame.transform.scale(assets['z_key'], (15, 15)), (200, 5))
    screen.blit(pygame.transform.scale(assets['backtick'], (15, 15)), (300, 5))
    screen.blit(pygame.transform.scale(assets['i1'], (15, 15)), (400, 5))
    screen.blit(pygame.transform.scale(assets['i2'], (15, 15)), (500, 5))
    screen.blit(pygame.transform.scale(assets['i3'], (15, 15)), (600, 5))
    screen.blit(pygame.transform.scale(assets['i4'], (15, 15)), (700, 5))
    screen.blit(pygame.transform.scale(assets['i5'], (15, 15)), (800, 5))
    #objects
    for i in walls:
        screen.blit(pygame.transform.scale(assets['wall'], (20, 20)), walls[i])
    for i in spikes:
        screen.blit(pygame.transform.scale(assets['spike'], (20, 20)), spikes[i])
    for i in spikes_left:
        screen.blit(pygame.transform.scale(assets['spike_left'], (20, 20)), spikes_left[i])
    for i in spikes_right:
        screen.blit(pygame.transform.scale(assets['spike_right'], (20, 20)), spikes_right[i])
    for i in spikes_down:
        screen.blit(pygame.transform.scale(assets['spike_down'], (20, 20)), spikes_down[i])
    #update the screen
    pygame.display.update()

#classes
class Mouse:

    #initiates the class
    def __init__(self):
        self.position = pygame.mouse.get_pos()
        self.clicking = pygame.mouse.get_pressed()
        self.left_click, self.middle_click, self.right_click = self.clicking
        self.wall_count = 0
        self.spike_count = 0
        self.object_count = 0
        self.spike_rotation = 0
        self.rect_dict = {}
    
    #gets info regarding the mouse
    def mouse_info(self):
        self.position = pygame.mouse.get_pos()
        self.clicking = pygame.mouse.get_pressed()
        self.left_click, self.middle_click, self.right_click = self.clicking
        self.x, self.y = self.position
        self.mouse_rect = pygame.Rect((self.x, self.y), (1, 1))
    
    #checks for collision of tiles
    def rectscollide(self):
        self.x = (self.x // 20) * 20
        self.y = (self.y // 20) * 20
        self.currentrect = pygame.Rect((self.x, self.y), (20, 20))
        return self.currentrect.collidedict(self.rect_dict, True)
    
    #placing and erasing tiles
    def place_object(self):
        global curr_object
        #checks if the cursor is inside the borders of the screen
        if 900 > self.x >= 100 and 700 > self.y >= 100:
            #checks if the user is clicking
            if self.left_click == True:
                #places objects
                if self.currentrect.collidedict(self.rect_dict, True) == None:
                    #places walls
                    if curr_object == current_object.wall:
                        walls[self.object_count] = self.x, self.y
                        self.rect_dict[self.object_count] = self.currentrect
                        self.wall_count += 1
                        self.object_count += 1
                    #places spikes that point up
                    if curr_object == current_object.spike and self.spike_rotation == 0:
                        spikes[self.object_count] = self.x, self.y
                        self.rect_dict[self.object_count] = self.currentrect
                        self.spike_count += 1
                        self.object_count += 1
                    #places spikes that point left
                    if curr_object == current_object.spike and self.spike_rotation == 1:
                        spikes_left[self.object_count] = self.x, self.y
                        self.rect_dict[self.object_count] = self.currentrect
                        self.spike_count += 1
                        self.object_count += 1
                    #places spikes that point down
                    if curr_object == current_object.spike and self.spike_rotation == 2:
                        spikes_down[self.object_count] = self.x, self.y
                        self.rect_dict[self.object_count] = self.currentrect
                        self.spike_count += 1
                        self.object_count += 1
                    #places spikes that point right
                    if curr_object == current_object.spike and self.spike_rotation == 3:
                        spikes_right[self.object_count] = self.x, self.y
                        self.rect_dict[self.object_count] = self.currentrect
                        self.spike_count += 1
                        self.object_count += 1
                # e r a s e
                elif curr_object == current_object.erase:
                    collision, ignore = self.currentrect.collidedict(self.rect_dict, True)
                    if collision in spikes:
                        spikes.pop(collision)
                        self.rect_dict.pop(collision)
                    if collision in spikes_left:
                        spikes_left.pop(collision)
                        self.rect_dict.pop(collision)
                    if collision in spikes_right:
                        spikes_right.pop(collision)
                        self.rect_dict.pop(collision)
                    if collision in spikes_down:
                        spikes_down.pop(collision)
                        self.rect_dict.pop(collision)
                    elif collision in walls:
                        walls.pop(collision)
                        self.rect_dict.pop(collision)
    #undo and clear
    def clear_and_undo(self):
        global curr_object
        #undo
        if curr_object == current_object.undo and len(self.rect_dict) != 0:
            #spikes that point up
            if max(k for k, v in self.rect_dict.items() if v != 0) in spikes:
                spikes.pop(max(k for k, v in self.rect_dict.items() if v != 0))
                self.rect_dict.pop(max(k for k, v in self.rect_dict.items() if v != 0))
            #spikes that point left
            if max(k for k, v in self.rect_dict.items() if v != 0) in spikes_left:
                spikes_left.pop(max(k for k, v in self.rect_dict.items() if v != 0))
                self.rect_dict.pop(max(k for k, v in self.rect_dict.items() if v != 0))
            #spikes that point right
            if max(k for k, v in self.rect_dict.items() if v != 0) in spikes_right:
                spikes_right.pop(max(k for k, v in self.rect_dict.items() if v != 0))
                self.rect_dict.pop(max(k for k, v in self.rect_dict.items() if v != 0))
            #spikes that point down
            if max(k for k, v in self.rect_dict.items() if v != 0) in spikes_down:
                spikes_down.pop(max(k for k, v in self.rect_dict.items() if v != 0))
                self.rect_dict.pop(max(k for k, v in self.rect_dict.items() if v != 0))
            #walls
            if max(k for k, v in self.rect_dict.items() if v != 0) in walls:
                walls.pop(max(k for k, v in self.rect_dict.items() if v != 0))
                self.rect_dict.pop(max(k for k, v in self.rect_dict.items() if v != 0))
            #do cooldown
            curr_object = current_object.blank
            pygame.time.wait(90)
        #clear
        if curr_object == current_object.clear:
            self.rect_dict.clear()
            spikes.clear()
            spikes_left.clear()
            spikes_right.clear()
            spikes_down.clear()
            walls.clear()
            curr_object = current_object.blank


                    
#Enums and stuff
class current_object(Enum):
    erase = 0
    wall = 1
    spike = 2
    undo = 10
    clear = 11
    blank = 2147483647
    def objects():
        erase = 0
        wall = 1
        spike = 2
        undo = 10
        clear = 11
        blank = 2147483647
        return wall, spike, erase, undo, clear, blank

#GUI and hotkeys
class GUI:
    def __init__(self):
        pass
    def hotkeys (self, keys):
        global curr_object
        if keys[pygame.K_BACKQUOTE]:
            curr_object = current_object.erase
        if keys[pygame.K_1]:
            curr_object = current_object.wall
        if keys[pygame.K_2]:
            curr_object = current_object.spike
            Mouse.spike_rotation = 0
        if keys[pygame.K_3]:
            curr_object = current_object.spike
            Mouse.spike_rotation =  1
        if keys[pygame.K_4]:
            curr_object = current_object.spike
            Mouse.spike_rotation =  2
        if keys[pygame.K_5]:
            curr_object = current_object.spike
            Mouse.spike_rotation =  3
        if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
            if keys[pygame.K_BACKSPACE]:
                curr_object = current_object.clear
            if keys[pygame.K_z]:
                curr_object = current_object.undo
        if keys[pygame.K_r]:
            Mouse.spike_rotation += 1
            if Mouse.spike_rotation >= 4:
                Mouse.spike_rotation = 0
            pygame.time.wait(100)
        if keys[pygame.K_t]:
            Mouse.spike_rotation -= 1
            if Mouse.spike_rotation <= -1:
                Mouse.spike_rotation = 3
                pygame.time.wait(100)
        #click on objects
        if Mouse.left_click:
            if 250 > Mouse.x > 200 and Mouse.y < 80:
                curr_object = current_object.undo
            if 350 > Mouse.x > 300 and Mouse.y < 80:
                curr_object = current_object.erase
            if 450 > Mouse.x > 400 and Mouse.y < 80:
                curr_object = current_object.wall
            if 550 > Mouse.x > 500 and Mouse.y < 80:
                curr_object = current_object.spike
                Mouse.spike_rotation = 0
            if 650 > Mouse.x > 600 and Mouse.y < 80:
                curr_object = current_object.spike
                Mouse.spike_rotation = 1
            if 750 > Mouse.x > 700 and Mouse.y < 80:
                curr_object = current_object.spike
                Mouse.spike_rotation = 2
            if 850 > Mouse.x > 800 and Mouse.y < 80:
                curr_object = current_object.spike
                Mouse.spike_rotation = 3
            return curr_object



#variables
assets_path = "assets"
background_color = (100, 120, 180)
screen = pygame.display.set_mode((1000, 800))
screen.fill(background_color)
assets = load_assets(assets_path)
background = assets['brick']
walls = {}
spikes = {}
spikes_left = {}
spikes_right = {}
spikes_down = {}
curr_object = current_object.wall
Mouse.__init__(Mouse)
running = True

#loop
while running:
    keys = pygame.key.get_pressed()
    Mouse.mouse_info(Mouse)
    Mouse.rectscollide(Mouse)
    Mouse.place_object(Mouse)
    Mouse.clear_and_undo(Mouse)
    GUI.hotkeys(GUI, keys)
    refresh(background_color)
    check_for_quit()