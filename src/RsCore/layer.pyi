from RsCore.instance import RsObject


class RsLayer(object):
    name: str = ""
    storage: list[RsObject] = []

    def __init__(self, name: str):
        ...

    def __repr__(self) -> str:
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
