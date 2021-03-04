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

        self.add_layer("Background")
        self.add_layer("Doodad Below")
        self.add_layer("Background")
        self.add_layer("Tile Below")
        self.add_layer("Trap")
        self.add_layer("Tile")
        self.add_layer("Entity")
        self.add_layer("Player")
        self.add_layer("Effect")
        self.add_layer("Doodad Above")
        self.add_layer("Effect Above")
        self.add_layer("UI")
        self.add_layer("System")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(RsContainers.RoomOrder) - 1:
            return RsContainers.RoomOrder[self.index + 1]
        else:
            raise StopIteration

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
