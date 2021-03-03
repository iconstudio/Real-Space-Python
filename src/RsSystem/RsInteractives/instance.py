class RsInstance(RsPrefab):
    def __init__(self, X: float = 0, Y: float = 0):
        self.__x:float = X
        self.__y:float = Y

        self.__speed:float = 0
        self.__direction:float = 0
        self.__hspeed:float = 0
        self.__vspeed:float = 0

        self.gravity: dict[str, float] = {
            "force" : 0,
            "direction": 0
        }

        self.image_angle:float = 0
        self.image_index:float = 0

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

    @speed.setter
    def speed(self, value):
        self.__speed = value
        self.__hspeed = utilities.lengthdir_x(value, self.direction)
        self.__vspeed = utilities.lengthdir_y(value, self.direction)

    @direction.setter
    def direction(self, value):
        self.__direction = value
        self.__hspeed = utilities.lengthdir_x(self.__speed, self.direction)
        self.__vspeed = utilities.lengthdir_y(self.__speed, self.direction)

    @hspeed.setter
    def hspeed(self, value):
        self.__hspeed = value
        self.__speed = utilities.point_distance(0, 0, self.__hspeed, self.__vspeed)
        self.__direction = utilities.point_direction(0, 0, self.__hspeed, self.__vspeed)

    @vspeed.setter
    def vspeed(self, value):
        self.__vspeed = value
        self.__speed = utilities.point_distance(0, 0, self.__hspeed, self.__vspeed)
        self.__direction = utilities.point_direction(0, 0, self.__hspeed, self.__vspeed)
