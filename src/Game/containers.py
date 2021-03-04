from .prefab import RsPrefab


# States
global Rooms
Rooms = list()

# Events
global Events
Events = list()

# Sprite texture group
global Atlas
Atlas: list[object] = list()

# All game objects
global PrefabsPot
PrefabsPot: list[RsPrefab] = list()

# All sounds
global AudioesPot
AudioesPot: list[object] = list()
