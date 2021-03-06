from typing import Optional

from RsCore.layer import RsLayer
from RsCore.prefab import RsPrefab
from RsCore.sprite import RsSprite


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
    sprite_index: Optional[RsSprite] = None
    image_angle: float
    image_index: float
    __speed: float
    __direction: float
    __hspeed: float
    __vspeed: float
    gravity: dict[str, float]

    def __init__(self, layer: RsLayer = None, x: float = 0, y: float = 0):
        ...

    ...
