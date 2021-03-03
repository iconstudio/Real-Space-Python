from scene import RsScene
from sprite import RsSprite
from prefab import RsPrefab
from scene import RsScene

# Sprite texture group
global Scenes
Scenes: list[RsScene] = list()

# Sprite texture group
global Atlas
Atlas: list[RsSprite] = list()

# All game objects
global Prefabs
Prefabs: list[RsPrefab] = list()

# All sounds
global Audioes
Audioes: list[object] = list()

