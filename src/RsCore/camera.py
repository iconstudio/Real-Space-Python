from RsCore.instance import RsObject
from RsCore.layer import RsLayer


class oCamera(RsObject):
    def __init__(self, layer: RsLayer):
        super().__init__(layer)
