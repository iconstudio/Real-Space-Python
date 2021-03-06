from RsCore import containers as RsContainers
from RsCore import RsScene
from Game.intro import SceneIntro


class GameGlobal(RsScene):
    def onAwake(self):
        RsContainers.RoomOrder.append(SceneIntro())
