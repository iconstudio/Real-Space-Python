from scene import RsScene
from prefab import RsPrefab

# Sprite texture group
global Rooms
Rooms: list[RsScene] = list()

# Sprite texture group
global Atlas
Atlas: list[object] = list()

# All game objects
global PrefabsPot
PrefabsPot: list[RsPrefab] = list()

# All sounds
global AudioesPot
AudioesPot: list[object] = list()
