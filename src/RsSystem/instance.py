from prefab import *
from utilities import *


class RsLayer(object):
    ...


class RsObject(object):
    __link_original: RsPrefab = None
    sprite_index: object = None  # Not an original sprite

    def __init__(self, layer: RsLayer = None, x: float = 0, y: float = 0):
        self.enabled = True
        self.visible = True
        self.layer = layer

        self.__xp: float = x
        self.__yp: float = y
        self.__x: float = x
        self.__y: float = y

        self.__speed: float = 0
        self.__direction: float = 0
        self.__hspeed: float = 0
        self.__vspeed: float = 0

        self.gravity: dict[str, float] = {
            "force": 0,
            "direction": 0
        }

        self.image_angle: float = 0
        self.image_index: float = 0

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def xprevious(self):
        return self.__xp

    @property
    def yprevious(self):
        return self.__yp

    @property
    def speed(self):
        return self.__speed

    @property
    def direction(self):
        return self.__direction

    @property
    def hspeed(self):
        return self.__hspeed

    @property
    def vspeed(self):
        return self.__vspeed

    @x.setter
    def x(self, value: float):
        self.__xp = self.__x
        self.__x = value

    @y.setter
    def y(self, value: float):
        self.__yp = self.__y
        self.__y = value

    @speed.setter
    def speed(self, value):
        self.__speed = value
        self.__hspeed = lengthdir_x(value, self.__direction)
        self.__vspeed = lengthdir_y(value, self.__direction)

    @direction.setter
    def direction(self, value):
        self.__direction = value
        self.__hspeed = lengthdir_x(self.__speed, self.__direction)
        self.__vspeed = lengthdir_y(self.__speed, self.__direction)

    @hspeed.setter
    def hspeed(self, value):
        self.__hspeed = value
        self.__speed = point_distance(0, 0, self.__hspeed, self.__vspeed)
        self.__direction = point_direction(0, 0, self.__hspeed, self.__vspeed)

    @vspeed.setter
    def vspeed(self, value):
        self.__vspeed = value
        self.__speed = point_distance(0, 0, self.__hspeed, self.__vspeed)
        self.__direction = point_direction(0, 0, self.__hspeed, self.__vspeed)

    def onAwake(self):
        ...

    def onDestroy(self):
        ...

    def onUpdate(self, time: int):
        ...

    def onUpdateLater(self, time: int):
        ...

    def onDraw(self, time: int):
        ...

    def onGUI(self, time: int):
        ...
