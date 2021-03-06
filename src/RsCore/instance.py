from RsCore.utilities import *


class RsObject(object):
    def __init__(self, layer=None, x=0, y=0):
        self.__link_original = None
        self.__enabled = True
        self.__visible = True
        self.layer = layer
        self.x = x
        self.y = y

    @property
    def link_original(self):
        return self.__link_original

    @property
    def enabled(self):
        return self.__enabled

    @property
    def visible(self):
        return self.__visible

    @link_original.setter
    def link_original(self, target):
        self.__link_original = target

    @enabled.setter
    def enabled(self, flag):
        self.__enabled = flag

    @visible.setter
    def visible(self, flag):
        self.__visible = flag

    def onAwake(self):
        if self.__link_original:
            self.__link_original.onAwake(self)

    def onDestroy(self):
        if self.__link_original:
            self.__link_original.onDestroy(self)

    def onUpdate(self, time):
        if self.__link_original:
            self.__link_original.onUpdate(time, self)

    def onUpdateLater(self, time):
        if self.__link_original:
            self.__link_original.onUpdateLater(time, self)

    def onDraw(self, time):
        if self.__link_original:
            self.__link_original.onDraw(time, self)

    def onGUI(self, time):
        if self.__link_original:
            self.__link_original.onGUI(time, self)


class RsDirtyObject(RsObject):
    def __init__(self, layer=None, x=0, y=0):
        super().__init__(layer, x, y)

        self.image_angle = 0
        self.image_index = 0
        self.__speed = 0
        self.__direction = 0
        self.__hspeed = 0
        self.__vspeed = 0
        self.gravity = {
            "force": 0,
            "direction": 0
        }

    @property
    def speed(self) -> float:
        return self.__speed

    @property
    def direction(self) -> float:
        return self.__direction

    @property
    def hspeed(self) -> float:
        return self.__hspeed

    @property
    def vspeed(self) -> float:
        return self.__vspeed

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

    def onUpdateLater(self, time):
        super().onUpdateLater(time)

        Hspeed = self.__hspeed
        if Hspeed != 0:
            self.x += Hspeed

        Vspeed = self.__vspeed
        if Vspeed != 0:
            self.y += Vspeed
