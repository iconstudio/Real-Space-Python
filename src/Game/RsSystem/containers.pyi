from typing import Optional, Union
from pygame.event import Event

from Game.RsSystem import constants as RsConstants, containers as RsContainers
from Game.RsSystem.instance import RsObject
from Game.RsSystem.layer import RsLayer
from Game.RsSystem.prefab import RsPrefab
from Game.RsSystem.scene import Scene
from Game.RsSystem.sprite import RsSprite

# Rooms
RoomOrder: list[Scene]
RoomPot: dict[str, Scene]

# Events
Events: list[Event]

# Sprite texture group
Atlas: dict[str, RsSprite]

# All game objects
PrefabsPot: dict[str, RsPrefab]

# All sounds
AudioPot: dict[str, object]
