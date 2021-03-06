from typing import Optional

from Game.RsSystem.sprite import RsSprite


class RsObject(object): ...


class RsPrefab(object):
    def __hash__(self) -> int:
        return self.name.__hash__()

    def __init__(self, name: str):
        self.name: str = name
        self.__parent: Optional[RsPrefab] = None
        self.children: list[RsPrefab] = []
        self.__link_implement = None
        self.sprite_index: Optional[RsSprite] = None
        self.serial: int = 0

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, target):
        if not target:
            self.__parent = None
        else:
            Parent = self.__parent
            if Parent:
                Parent.children.remove(self)
            self.__parent = target
            target.children.append(self)

    @property
    def link_implement(self) -> Optional[RsObject]:
        return self.__link_implement

    @link_implement.setter
    def link_implement(self, target):
        Before = self.__link_implement
        if Before and Before is not target:
            Before.__link_original = None
        if target:
            self.__link_implement = target
            target.__link_original = self

    def onAwake(self, target):
        pass

    def onDestroy(self, target):
        pass

    def onUpdate(self, time: int, target):
        pass

    def onUpdateLater(self, time: int, target):
        pass

    def onDraw(self, time: int, target):
        pass

    def onGUI(self, time: int, target):
        pass
