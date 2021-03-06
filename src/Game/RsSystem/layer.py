class RsLayer(object):
    def __init__(self, name: str):
        self.name: str = name
        self.storage = []

    def __repr__(self) -> str:
        return "Layer " + self.name

    def onAwake(self):
        for Instance in self.storage:
            Instance.onAwake()

    def onDestroy(self):
        for Instance in self.storage:
            Instance.onDestroy()

    def onUpdate(self, time: int):
        for Instance in self.storage:
            Instance.onUpdate(time)

    def onUpdateLater(self, time: int):
        for Instance in self.storage:
            Instance.onUpdateLater(time)

    def onDraw(self, time: int):
        for Instance in self.storage:
            Instance.onDraw(time)

    def onGUI(self, time: int):
        for Instance in self.storage:
            Instance.onGUI(time)
