from Game.RsSystem.scene import Scene
from Game.intro import SceneIntro
from Game.RsSystem import constants as RsConstants, containers as RsContainers


class GameGlobal(Scene):
    def onAwake(self):
        RsContainers.RoomOrder.append(SceneIntro())
