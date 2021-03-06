class RsPrefab(object):
    def __init__(self, name: str):
        self.name = name
        self.__parent = None
        self.children = []
        self.__link_implement = None
        self.sprite_index = None
        self.serial: int = 0

    def __hash__(self) -> int:
        return self.name.__hash__()

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
    def link_implement(self):
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

    def onUpdate(self, time, target):
        pass

    def onUpdateLater(self, time, target):
        pass

    def onDraw(self, time, target):
        pass

    def onGUI(self, time, target):
        pass
