from csv import reader
from os import walk
import pygame
from Assets.Settings import *

def importanimation(path):
    animation = []
    for a, b, file in walk(path):
        for image in file:
            full_path = path + '/' + image
            img_list = pygame.image.load(full_path).convert_alpha()
            animation.append(img_list)
    return animation


def read_csv(path):
    list_map = []
    with open(path) as file:
        csv_reader = reader(file, delimiter = ',')
        for row in csv_reader:
            list_map.append(list(row))
        return list_map

def slice_img(path):
    img = pygame.image.load(path).convert_alpha()
    img_list = []
    img_x = int(img.get_size()[0] / BLOCKSIZE)
    img_y = int(img.get_size()[1] / BLOCKSIZE)

    for row in range(img_y):
        for col in range(img_x):
            x = col * BLOCKSIZE
            y = row * BLOCKSIZE

            temp = pygame.Surface((BLOCKSIZE, BLOCKSIZE), flags=pygame.SRCALPHA)
            temp.blit(img, (0, 0), (x, y, BLOCKSIZE, BLOCKSIZE))
            img_list.append(temp)
    return img_list
