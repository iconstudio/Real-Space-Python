from typing import Optional


class RsObject(object):
    ...


class RsPrefab(object):
    def __init__(self):
        self.name: str = "RsPrefab"
        self.object_index: type = RsPrefab
        self.__parent: Optional[RsPrefab] = None
        self.children: list[RsPrefab] = []
        self.__link_implement = None
        self.sprite_index: Optional[object] = None
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
