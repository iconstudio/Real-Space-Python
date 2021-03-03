class RsBehavior(object):
    name = str()

    def __str__(self):
        return self.name

    def __init__(self):
        ...

    def onAwake(self):
        ...

    def onDestroy(self):
        ...

    async def onUpdate(self, Time):
        """onUpdate(time)"""
        ...

    async def onUpdateLater(self, Time):
        """onUpdateLater(time)"""
        ...

    async def onDraw(self, Time):
        """onDraw(time)"""
        ...

    async def onGUI(self, Time):
        """onGUI(time)"""
        ...
