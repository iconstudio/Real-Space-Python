from typing import Optional

from RsCore.layer import RsLayer
from RsCore.prefab import RsPrefab
from RsCore.sprite import RsSprite


class RsCoordinates(object):
    __x: float = 0
    __y: float = 0
    __xp: float = 0
    __yp: float = 0

    def __init__(self, x: float, y: float):
        ...


class RsPhysics(object):
    __speed: float = 0
    __direction: float = 0
    __hspeed: float = 0
    __vspeed: float = 0
    gravity: dict[str, float]
    ...


class RsObject(object):
    __link_original: Optional[RsPrefab] = None
    __enabled: bool = True
    __visible: bool = True
    layer: Optional[RsLayer] = None
    coordinates: RsCoordinates

    def __init__(self, layer: RsLayer = None, x: float = 0, y: float = 0):
        ...

    @property
    def link_original(self) -> Optional[RsPrefab]:
        ...

    @property
    def enabled(self) -> bool:
        ...

    @property
    def visible(self) -> bool:
        ...

    @property
    def x(self) -> float:
        ...

    @property
    def y(self) -> float:
        ...

    @property
    def xprevious(self) -> float:
        ...

    @property
    def yprevious(self) -> float:
        ...

    @link_original.setter
    def link_original(self, target):
        ...

    @enabled.setter
    def enabled(self, flag: bool):
        ...

    @visible.setter
    def visible(self, flag: bool):
        ...

    @x.setter
    def x(self, value: float):
        ...

    @y.setter
    def y(self, value: float):
        ...

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

    ...


class RsDirtyObject(RsObject):
    movement: RsPhysics
    sprite_index: Optional[RsSprite] = None
    image_angle: float = 0
    image_index: float = 0

    def __init__(self, layer: RsLayer = None, x: float = 0, y: float = 0):
        ...

    ...
