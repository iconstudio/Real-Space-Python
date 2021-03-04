from .layer import RsLayer


class Scene(object):
    def add_layer(self, caption: str) -> None:
        Temp = RsLayer(caption)
        self.stack.append(Temp)
        self.trees[caption] = Temp

    def __init__(self):
        self.running = True
        self.stack: list[RsLayer] = []
        self.trees: dict[str, RsLayer] = {}

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

    def termiate(self):
        self.running = False

    def onAwake(self) -> None:
        for Layer in self.stack:
            Layer.onAwake()

    def onDestroy(self):
        for Layer in self.stack:
            Layer.onDestroy()

    async def onUpdate(self, time: int):
        for Layer in self.stack:
            if not self.running:
                break
            await Layer.onUpdate(time)

    async def onUpdateLater(self, time: int):
        for Layer in self.stack:
            if not self.running:
                break
            await Layer.onUpdateLater(time)

    async def onDraw(self, time: int):
        for Layer in self.stack:
            if not self.running:
                break
            await Layer.onDraw(time)

    async def onGUI(self, time: int):
        for Layer in self.stack:
            if not self.running:
                break
            await Layer.onGUI(time)
