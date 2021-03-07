from RsCore.scene import RsScene
from RsCore.layer import RsLayer
from RsCore.prefab import RsPrefab
from RsCore.instance import RsObject
from RsCore.sprite import RsSprite
from RsCore import constants as RsConstants, containers as RsContainers
from RsCore.assets import room_register, instance_create

import Game.game_cfg as GameConstants



def init():
    room_register("roomInit")
    room_register("roomLogo")
    room_register("roomIntro")
    room_register("roomMain")
    room_register("roomDemo")
    room_register("roomStage01")
    room_register("roomStage02")
    room_register("roomStage03")

    # Test
    from Game.spaceships import oSpaceShip
    TestInstance = instance_create(oSpaceShip, GameConstants.LAYERS.PLAYER_7, 0, 50)
    print(TestInstance)


