from typing import Optional


class RsPrefab(object):
    def __init__(self):
        self.children = None

    ...


class RsObject(object):
    ...


class RsPrefab(object):
    def __init__(self):
        self.name: str = "RsPrefab"
        self.object_index: type = RsPrefab
        self.__parent: RsPrefab = None
        self.children: list[RsPrefab] = []
        self.__link_implement: RsObject = None
        self.sprite_index: object = None
        self.serial: int = 0

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, target: Optional[RsPrefab]):
        if not target:
            self.__parent = None
            return
        Parent: RsPrefab = self.__parent
        if Parent:
            Parent.children.remove(self)
        self.__parent = target
        target.children.append(self)

    @property
    def link_implement(self) -> Optional[RsObject]:
        return self.__link_implement

    @link_implement.setter
    def link_implement(self, target: Optional[RsPrefab]):
        Before: RsObject = self.__link_implement
        if Before and Before is not target:
            Before.__link_original = None
        if target:
            self.__link_implement = target
            target.__link_original = self
