from layer import RsLayer


class RsScene(object):
    def __init__(self):
        self.running = True
        self.storage: list[RsLayer] = []

    def __add__(self, layer: RsLayer):
        self.storage.append(layer)

    def add_layer(self, layer: RsLayer):
        self.storage.append(layer)

    async def onAwake(self) -> None:
        for Layer in self.storage:
            await Layer.onAwake()

    async def onDestroy(self):
        for Layer in self.storage:
            await Layer.onDestroy()

    async def onUpdate(self, time: int):
        for Layer in self.storage:
            await Layer.onUpdate(time)

    async def onUpdateLater(self, time: int):
        for Layer in self.storage:
            await Layer.onUpdateLater(time)

    async def onDraw(self, time: int):
        for Layer in self.storage:
            await Layer.onDraw(time)

    async def onGUI(self, time: int):
        for Layer in self.storage:
            await Layer.onGUI(time)
