class RsBehavior(object):
    name = "RS Object"

    def __str__(self):
        return self.name

    def __init__(self):
        ...

    def onAwake(self):
        ...

    def onDestroy(self):
        ...

    def onUpdate(self, Time):
        """onUpdate(time)"""
        ...

    def onUpdateLater(self, Time):
        """onUpdateLater(time)"""
        ...

    def onDraw(self, Time):
        """onDraw(time)"""
        ...

    def onGUI(self, Time):
        """onGUI(time)"""
        ...
