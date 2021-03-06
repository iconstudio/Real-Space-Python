from typing import Optional

from RsCore.layer import RsLayer
from RsCore.prefab import RsPrefab
from RsCore.sprite import RsSprite


class RsPhysics(object):
    def __init__(self):
        self.__hspeed = float(0)
        self.__vspeed = float(0)

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
    x: float = 0
    y: float = 0

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

    @link_original.setter
    def link_original(self, target):
        ...

    @enabled.setter
    def enabled(self, flag: bool):
        ...

    @visible.setter
    def visible(self, flag: bool):
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
