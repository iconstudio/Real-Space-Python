#! Initialization
resolutions = {
    "width": 640,
    "height": 480
}

# Sprite texture group
global ScenesPot
ScenesPot: list[RsScene] = list()

# Sprite texture group
global Atlas
Atlas: list[RsSprite] = list()

# All game objects
global Prefabs
Prefabs: list[RsPrefab] = list()

# All sounds
global Audioes
Audioes: list[object] = list()
