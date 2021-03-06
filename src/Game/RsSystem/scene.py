from Game.RsSystem.layer import RsLayer
from Game.RsSystem import containers as RsContainers


class Scene(object):
    paused: bool = False
    stack: list[RsLayer]
    trees: dict[str, RsLayer]
    EveryInstancesPot: list
    SpecificInstancesPot: dict[str, list]
    before = None
    next = None

    def add_layer(self, caption: str):
        Temp = RsLayer(caption)
        self.stack.append(Temp)
        self.trees[caption] = Temp

    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return "Room " + self.name

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def onAwake(self):
        for Layer in self.stack:
            Layer.onAwake()

    def onDestroy(self):
        for Layer in self.stack:
            Layer.onDestroy()

    def onUpdate(self, time: int):
        for Layer in self.stack:
            Layer.onUpdate(time)

    def onUpdateLater(self, time: int):
        for Layer in self.stack:
            Layer.onUpdateLater(time)

    def onDraw(self, time: int):
        for Layer in self.stack:
            Layer.onDraw(time)

    def onGUI(self, time: int):
        for Layer in self.stack:
            Layer.onGUI(time)
