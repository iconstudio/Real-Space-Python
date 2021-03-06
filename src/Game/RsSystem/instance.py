from typing import Optional
import pygame.sprite as PySprite
from pygame.sprite import Sprite as RsRawSprite
from pygame.sprite import Group as RsRawGroup

from Game.RsSystem.layer import RsLayer
from Game.RsSystem.prefab import RsPrefab
from Game.RsSystem.sprite import RsSprite
from Game.RsSystem.utilities import *


class RsCoordinates:
    def __init__(self, x: float = 0, y: float = 0):
        self.__xp: float = x
        self.__yp: float = y
        self.__x: float = x
        self.__y: float = y


class RsPhysics:
    def __init__(self):
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
        super().__init__()
        self.__link_original: Optional[RsPrefab] = None
        self.__enabled: bool = True
        self.__visible: bool = True
        self.layer: Optional[RsLayer] = layer

        self.coordinates = RsCoordinates(x, y)

    @property
    def link_original(self) -> Optional[RsPrefab]:
        return self.__link_original

    @property
    def enabled(self) -> bool:
        return self.__enabled

    @property
    def visible(self) -> bool:
        return self.__visible

    @property
    def x(self):
        return self.coordinates.__x

    @property
    def y(self):
        return self.coordinates.__y

    @property
    def xprevious(self):
        return self.coordinates.__xp

    @property
    def yprevious(self):
        return self.coordinates.__yp

    @link_original.setter
    def link_original(self, target):
        self.__link_original = target

    @enabled.setter
    def enabled(self, flag):
        self.__enabled = flag

    @visible.setter
    def visible(self, flag):
        self.__visible = flag

    @x.setter
    def x(self, value: float):
        self.coordinates.__xp = self.coordinates.__x
        self.coordinates.__x = value

    @y.setter
    def y(self, value: float):
        self.coordinates.__yp = self.coordinates.__y
        self.coordinates.__y = value

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def onAwake(self):
        if self.__link_original:
            self.__link_original.onAwake(self)

    def onDestroy(self):
        if self.__link_original:
            self.__link_original.onDestroy(self)

    def onUpdate(self, time: int):
        if self.__link_original:
            self.__link_original.onUpdate(time, self)

    def onUpdateLater(self, time: int):
        if self.__link_original:
            self.__link_original.onUpdateLater(time, self)

    def onDraw(self, time: int):
        if self.__link_original:
            self.__link_original.onDraw(time, self)

    def onGUI(self, time: int):
        if self.__link_original:
            self.__link_original.onGUI(time, self)


class RsDirtyObject(RsObject):
    def __init__(self, layer: RsLayer = None, x: float = 0, y: float = 0):
        super().__init__(layer, x, y)

        self.movement = RsPhysics()

        self.sprite_index: Optional[RsSprite] = None
        self.image_angle: float = 0
        self.image_index: float = 0

    @property
    def speed(self):
        return self.movement.__speed

    @property
    def direction(self):
        return self.movement.__direction

    @property
    def hspeed(self):
        return self.movement.__hspeed

    @property
    def vspeed(self):
        return self.movement.__vspeed

    @speed.setter
    def speed(self, value):
        self.movement.__speed = value
        self.movement.__hspeed = lengthdir_x(value, self.movement.__direction)
        self.movement.__vspeed = lengthdir_y(value, self.movement.__direction)

    @direction.setter
    def direction(self, value):
        self.movement.__direction = value
        self.movement.__hspeed = lengthdir_x(self.movement.__speed, self.movement.__direction)
        self.movement.__vspeed = lengthdir_y(self.movement.__speed, self.movement.__direction)

    @hspeed.setter
    def hspeed(self, value):
        self.movement.__hspeed = value
        self.movement.__speed = point_distance(0, 0, self.movement.__hspeed, self.movement.__vspeed)
        self.movement.__direction = point_direction(0, 0, self.movement.__hspeed, self.movement.__vspeed)

    @vspeed.setter
    def vspeed(self, value):
        self.movement.__vspeed = value
        self.movement.__speed = point_distance(0, 0, self.movement.__hspeed, self.movement.__vspeed)
        self.movement.__direction = point_direction(0, 0, self.movement.__hspeed, self.movement.__vspeed)
