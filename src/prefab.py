from behavior import RsBehavior
import gear

def prefab_register(Fab):
    gear.Prefabs.append(Fab)
 
class RsPrefab(RsBehavior):
    def __init__(self, Sprite: object = None, Parent = None):
        self.sprite_index:object = Sprite
        self.parent = Parent
        pass

    def register(self):
        prefab_register(self)
    
    def onAwake(self):
        pass

    def onDestroy(self):
        pass

    def onUpdate(self, Time):
        """onUpdate(time)"""
        pass

    def onUpdateLater(self, Time):
        """onUpdateLater(time)"""
        pass

    def onDraw(self, Time):
        """onDraw(time)"""
        pass

    def onGUI(self, Time):
        """onGUI(time)"""
        pass
