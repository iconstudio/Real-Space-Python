from RsCore.prefab import RsPrefab
from RsCore.instance import RsDirtyObject


# TODO: #2 Make ship a good example of game object
class SPACESHIP_TYPES:
    PATROL = 0


class preSpaceShip(RsPrefab):
    pass


class oSpaceShip(RsDirtyObject):
    link_original = preSpaceShip
