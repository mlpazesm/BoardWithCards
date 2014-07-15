import pygame
import os

__author__ = 'fonter'


def load_image(name, folder='.'):
    fullname = os.path.join(folder, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert_alpha()
    return image, image.get_rect()
