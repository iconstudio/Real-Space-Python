from RsCore.utilities import *


class RsCoordinates:
    def __init__(self, x, y):
        self.__xp = x
        self.__yp = y
        self.__x = x
        self.__y = y


class RsPhysics:
    def __init__(self):
        self.gravity = {
            "force": 0,
            "direction": 0
        }


class RsObject(object):
    def __init__(self, layer=None, x=0, y=0):
        self.__link_original = None
        self.__enabled = True
        self.__visible = True
        self.layer = layer
        self.coordinates = RsCoordinates(x, y)

    @property
    def link_original(self):
        return self.__link_original

    @property
    def enabled(self):
        return self.__enabled

    @property
    def visible(self):
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
    def x(self, value):
        self.coordinates.__xp = self.coordinates.__x
        self.coordinates.__x = value

    @y.setter
    def y(self, value):
        self.coordinates.__yp = self.coordinates.__y
        self.coordinates.__y = value

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
    def __init__(self, layer=None, x=0, y=0):
        super().__init__(layer, x, y)

        self.movement = RsPhysics()

    @property
    def speed(self) -> float:
        return self.movement.__speed

    @property
    def direction(self) -> float:
        return self.movement.__direction

    @property
    def hspeed(self) -> float:
        return self.movement.__hspeed

    @property
    def vspeed(self) -> float:
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
