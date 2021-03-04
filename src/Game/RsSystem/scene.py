from Game.RsSystem.layer import RsLayer
from Game.RsSystem import containers as RsContainers


class Scene(object):
    def add_layer(self, caption: str):
        Temp = RsLayer(caption)
        self.stack.append(Temp)
        self.trees[caption] = Temp

    def __init__(self, name: str):
        self.index: int = 0
        self.name = name
        self.paused = False
        self.stack: list[RsLayer] = []
        self.trees: dict[str, RsLayer] = {}
        self.EveryInstancesPot: list = []
        self.SpecificInstancesPot: dict[str, list] = {}

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(RsContainers.RoomOrder) - 1:
            return RsContainers.RoomOrder[self.index + 1]
        else:
            raise StopIteration

    def __repr__(self) -> str:
        return "Room " + self.name + " at (" + str(self.index) + ")"

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
