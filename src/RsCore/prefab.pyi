from typing import Optional

from RsCore.instance import RsObject
from RsCore.sprite import RsSprite


class RsPrefab(object):
    name: str
    __parent: Optional[RsPrefab]
    children: list[RsPrefab]
    __link_implement: Optional[RsObject]
    sprite_index: Optional[RsSprite]
    serial: int

    def __init__(self, name: str):
        ...

    def __hash__(self) -> int:
        ...

    @property
    def parent(self) -> Optional[RsPrefab]:
        ...

    @parent.setter
    def parent(self, target: Optional[RsPrefab]):
        ...

    @property
    def link_implement(self) -> Optional[RsObject]:
        ...

    @link_implement.setter
    def link_implement(self, target: Optional[RsPrefab]):
        ...

    def onAwake(self, target: RsObject):
        ...

    def onDestroy(self, target: RsObject):
        ...

    def onUpdate(self, time: int, target: RsObject):
        ...

    def onUpdateLater(self, time: int, target: RsObject):
        ...

    def onDraw(self, time: int, target: RsObject):
        ...

    def onGUI(self, time: int, target: RsObject):
        ...

    ...
