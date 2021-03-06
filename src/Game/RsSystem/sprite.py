import json
import os
from typing import Optional, Union, overload

from pygame.rect import Rect as PyRect
import pygame.surface as PySurface
import pygame.image as PyImage

from Game.RsSystem import constants as RsConstants


class RsImage(object):
    number: int = -1
    raw_data: list[PySurface.Surface]
    boundbox = PyRect(0, 0, 0, 0)

    def __init__(self, filepath: Union[list[str], str]) -> None:
        if type(filepath) is str:
            self.number = 0
            self.raw_data.append(PyImage.load(filepath))
            self.filename = os.path.splitext(filepath)[0]
            
        else:
            self.number = len(filepath)
            
            for file in filepath:
                self.raw_data.append(PyImage.load(file))
            self.filename = os.path.splitext(filepath[0])[0]

        self.boundbox.width = self.raw_data[0].get_width()
        self.boundbox.height = self.raw_data[0].get_height()

    def draw(self, x: float, y: float, index: int):
        if self.number == 0:
            Temp = self.raw_data[0]
            Temp.get_rect()
        else:
            pass


class RsSprite(object):
    xoffset: int = 0
    yoffset: int = 0
    raw_data: Optional[RsImage] = None

    def __init__(self, image: RsImage, mask_type = RsConstants.MASKS.RECTANGLE, xo: int = 0, yo: int = 0):
        self.raw_data = image
        self.xoffset = xo
        self.yoffset = yo

    def update(self, x: float, y: float):
        if self.raw_data:
            Box = self.raw_data.boundbox
            Box.x = int(x)
            Box.y = int(y)

    def draw(self, x: float, y: float, index: int = 0):
        self.raw_data.draw(x, y, index)


sprite_list: dict = {}


def load_image(filename: str, xo: float, yo: float):
    ...


class LegacySprite(object):
    name: str = ""
    number: int = 0
    width, height = 0, 0
    isSeparate: bool = False
    xoffset, yoffset = 0, 0
    __data__ = []

    def __init__(self, filepath: Union[list[str], str], number, xoffset, yoffset):
        """
            이미지 불러오기, 이미지 분할, 리스트화 작업
        """
        self.__data__ = []
        if type(filepath) is list[str]:  # 스프라이트가 여러 개의 이미지로 구성됨.
            self.isSeparate = True
            self.number = len(filepath)

            try:
                if self.number > 0:
                    for specpath in filepath:
                        img = load_image(specpath, xoffset, yoffset)
                        self.__data__.append(img)
                    self.width = int(self.__data__[0].w)
                    self.height = int(self.__data__[0].h)
            except IndexError:
                raise RuntimeError("스프라이트 목록이 비어있습니다!")
        else:  # 스프라이트가 낱장의 이미지로 구성됨.
            img = load_image(filepath, xoffset, yoffset)
            self.__data__.append(img)
            self.number = number  # the number of sprite in an image
            # size of each index
            self.width = int(self.__data__[0].w / number)
            self.height = int(self.__data__[0].h)

        self.xoffset, self.yoffset = self.__data__[0].xoffset, self.__data__[0].yoffset
        try:
            tempTy = type(number)
            if tempTy != int and tempTy != float:
                raise RuntimeError("스프라이트 불러오기 시 인자가 숫자가 아닙니다.")
        except ZeroDivisionError:
            raise RuntimeError("스프라이트의 갯수는 0개가 될 수 없습니다.")

    def __eq__(self, other) -> bool:
        if type(other) != LegacySprite:
            return False
        if self.__repr__() == other.__repr__():
            return True
        return False

    def __repr__(self) -> str:
        return self.name

    def draw(self, index: int or float, sx, sy, xscale=float(1), yscale=float(1), rot=float(0.0),
             alpha=float(1.0)) -> None:
        dx = 0
        if not self.isSeparate:
            data = self.__data__[0]
            dx = int(self.width * index)
        else:
            data = self.__data__[int(index % self.number)]

        data.opacify(alpha)
        flipmod: str = ""
        if xscale < 0:
            flipmod += "h"
        if yscale < 0:
            flipmod += "v"
        xscale, yscale = abs(xscale), abs(yscale)

        data.clip_composite_draw_angle(dx, 0, self.width, self.height, rot, flipmod, sx, sy, int(self.width * xscale),
                                       int(self.height * yscale))

    def get_handle(self):
        return self.__data__


def sprite_load(filepaths, name=str("default"), xoffset=None, yoffset=None, number=int(1)) -> Sprite:
    global sprite_list
    new = LegacySprite(filepaths, number, xoffset, yoffset)
    new.name = name
    sprite_list[name] = new
    return new


def sprite_get(name: str) -> LegacySprite:
    global sprite_list
    try:
        val = sprite_list[name]
    except KeyError as e:
        raise RuntimeError(str(e) + "\n 해당 스프라이트가 존재하지 않습니다!")
    return val


def draw_sprite(spr: LegacySprite, index=int(0) or float(0), sx=int(0), sy=int(0), xscale=float(1), yscale=float(1),
                rot=float(0.0), alpha=float(1.0)) -> None:
    spr.draw(index, sx, sy, xscale, yscale, rot, alpha)


def sprite_json_loads():
    try:
        with open("Data\\sprite.json") as sprfile:
            parsed = json.load(sprfile)

            for content in parsed:
                sprite_load(content["path"], content["name"], content["xoffset"], content["yoffset"], content["number"])

    except FileNotFoundError:
        pass
