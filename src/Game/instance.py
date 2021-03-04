from typing import Optional

from .prefab import RsPrefab
from .layer import RsLayer
from .utilities import *


class RsCoordinates:
    def __init__(self, x: float = 0, y: float = 0):
        self.__xp: float = x
        self.__yp: float = y
        self.__x: float = x
        self.__y: float = y


class RsPhysics:
    def __init__(self, x: float = 0, y: float = 0):
        self.coordinates = RsCoordinates(x, y)

        self.__speed: float = 0
        self.__direction: float = 0
        self.__hspeed: float = 0
        self.__vspeed: float = 0

        self.gravity: dict[str, float] = {
            "force": 0,
            "direction": 0
        }


class RsObject(object):
    def __init__(self, layer: RsLayer = None, x: float = 0, y: float = 0):
        self.__link_original = None
        self.enabled = True
        self.visible = True
        self.layer = layer

        self.physical = RsPhysics(x, y)
        
        self.sprite_index: object = None  # Not an original sprite
        self.image_angle: float = 0
        self.image_index: float = 0

    def __del__(self):
        pass

    @property
    def link_original(self) -> Optional[RsPrefab]:
        return self.__link_original

    @property
    def x(self):
        return self.physical.coordinates.__x

    @property
    def y(self):
        return self.physical.coordinates.__y

    @property
    def xprevious(self):
        return self.physical.coordinates.__xp

    @property
    def yprevious(self):
        return self.physical.coordinates.__yp

    @property
    def speed(self):
        return self.physical.__speed

    @property
    def direction(self):
        return self.physical.__direction

    @property
    def hspeed(self):
        return self.physical.__hspeed

    @property
    def vspeed(self):
        return self.physical.__vspeed

    @link_original.setter
    def link_original(self, target):
        self.__link_original = target

    @x.setter
    def x(self, value: float):
        self.physical.coordinates.__xp = self.physical.coordinates.__x
        self.physical.coordinates.__x = value

    @y.setter
    def y(self, value: float):
        self.physical.coordinates.__yp = self.physical.coordinates.__y
        self.physical.coordinates.__y = value

    @speed.setter
    def speed(self, value):
        self.physical.__speed = value
        self.physical.__hspeed = lengthdir_x(value, self.physical.__direction)
        self.physical.__vspeed = lengthdir_y(value, self.physical.__direction)

    @direction.setter
    def direction(self, value):
        self.physical.__direction = value
        self.physical.__hspeed = lengthdir_x(self.physical.__speed, self.physical.__direction)
        self.physical.__vspeed = lengthdir_y(self.physical.__speed, self.physical.__direction)

    @hspeed.setter
    def hspeed(self, value):
        self.physical.__hspeed = value
        self.physical.__speed = point_distance(0, 0, self.physical.__hspeed, self.physical.__vspeed)
        self.physical.__direction = point_direction(0, 0, self.physical.__hspeed, self.physical.__vspeed)

    @vspeed.setter
    def vspeed(self, value):
        self.physical.__vspeed = value
        self.physical.__speed = point_distance(0, 0, self.physical.__hspeed, self.physical.__vspeed)
        self.physical.__direction = point_direction(0, 0, self.physical.__hspeed, self.physical.__vspeed)
