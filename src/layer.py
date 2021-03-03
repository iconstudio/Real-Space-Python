class RsLayer():
    name:str = "Layer"
    depth:int = 0
    objects = []

    def onUpdate(self, Time):
        for Instance in self.objects:
            Instance.onUpdate(Time)
