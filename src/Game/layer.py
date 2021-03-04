from .prefab import RsPrefab


class RsLayer(object):
    def __init__(self, name: str = "Default"):
        self.name: str = name
        self.storage: list[RsPrefab] = []

    def __repr__(self) -> str:
        return "Layer " + self.name

    def onAwake(self) -> None:
        for Instance in self.storage:
            Instance.onAwake()

    def onDestroy(self):
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
