from behavior import RsBehavior
from layer import RsLayer

class RsScene(RsBehavior):
    def __init__(self):
        super().__init__()
        self.running = True
        self.layers:list[RsLayer] = []

    def add_layer(self, Layer: RsLayer):
        self.layers.append(Layer)

    def onUpdate(self, Time):
        for Layer in self.layers:
            Layer.onUpdate(Time)
