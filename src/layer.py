class RsLayer(object):
    name: str = "Default"
    storage: list[object] = []

    def __repr__(self) -> str:
        return "Layer " + self.name

    async def onAwake(self) -> None:
        for Instance in self.storage:
            Instance.onAwake()

    async def onDestroy(self):
        for Instance in self.storage:
            Instance.onDestroy()

    async def onUpdate(self, time: int):
        for Instance in self.storage:
            Instance.onUpdate(time)

    async def onUpdateLater(self, time: int):
        for Instance in self.storage:
            Instance.onUpdateLater(time)

    async def onDraw(self, time: int):
        for Instance in self.storage:
            Instance.onDraw(time)

    async def onGUI(self, time: int):
        for Instance in self.storage:
            Instance.onGUI(time)
