from pygame import Surface
from pygame.sprite import Sprite as RsSprite
import pygame.image as ImgLoader
import pygame.sprite as Sprite

import gear


def sprite_add(File):
    Temp = ImgLoader.load(File)
    return Temp
