from Game.RsSystem.layer import RsLayer
from Game.RsSystem.instance import RsObject


class oCamera(RsObject):
    def __init__(self, layer: RsLayer):
        super().__init__(layer)
