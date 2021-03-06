from pygame.event import Event

from RsCore import RsPrefab
from RsCore import RsScene
from RsCore import RsSprite

# Rooms
RoomOrder: list[RsScene]
RoomPot: dict[str, RsScene]

# Events
Events: list[Event]

# Sprite texture group
Atlas: dict[str, RsSprite]

# All game objects
PrefabsPot: dict[str, RsPrefab]

# All sounds
AudioPot: dict[str, object]
