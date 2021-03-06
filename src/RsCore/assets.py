from typing import Optional, Union, Type

from RsCore.scene import RsScene
from RsCore.layer import RsLayer
from RsCore.prefab import RsPrefab
from RsCore.instance import RsObject
from RsCore import constants as RsConstants, containers as RsContainers

from Game import game_cfg as GameConstants

__all__ = [
    "object_register",
    "scene_update", "room_register", "room_get", "room_goto", "room_goto_next",
    "layer_find",
    "instance_create"
]


def object_register(name: str) -> RsPrefab:
    Temp = RsPrefab(name)
    # TODO: #3 object add
    RsContainers.PrefabsPot[name] = Temp

    return Temp


async def scene_update(room: RsScene, time: int) -> None:
    room.onUpdate(time)
    room.onUpdateLater(time)
    room.onDraw(time)
    room.onGUI(time)


def room_register(name: str):
    global RsRoom, RsLastRoom
    NewRoom = RsScene(name)

    for explicit_layer in GameConstants.layer_default:
        NewRoom.add_layer(explicit_layer)

    Number = len(RsContainers.RoomOrder)
    if 0 < Number:
        LastRoom = RsContainers.RoomOrder[-1]
        if LastRoom and NewRoom:
            NewRoom.before = LastRoom
            LastRoom.next = NewRoom
    else:
        RsRoom = NewRoom
        RsLastRoom = NewRoom

    RsContainers.RoomOrder.append(NewRoom)
    RsContainers.RoomPot[name] = NewRoom


def room_get(id: Union[int, str]) -> Optional[RsScene]:
    if type(id) is int:
        return RsContainers.RoomOrder[id]
    elif type(id) is str:
        return RsContainers.RoomPot[id]


def room_set(taget: RsScene):
    global RsRoom

    if RsRoom:
        RsRoom.onDestroy()
    RsRoom = taget
    RsRoom.onAwake()
    print("Go to " + str(RsRoom))


def room_goto(name: str):
    global RsRoom

    Temp = room_get(name)
    if not Temp:
        raise RuntimeError("The room " + name + " doesn't exist.")
    elif Temp is not RsRoom:
        room_set(Temp)


def room_goto_next():
    global RsRoom

    Next = RsRoom.next
    print(Next)
    if Next:
        Temp: RsScene = Next
        room_set(Temp)
    else:
        raise RuntimeError("The next room doesn't exist.\n")


def layer_find(name: str) -> Optional[RsLayer]:
    global RsRoom
    if RsRoom and name in GameConstants.layer_default:
        Where = RsRoom.trees[name]
        return Where


def instance_create(prefab: Type[RsObject], layer: Union[str, RsLayer], x: float = 0, y: float = 0) -> Optional[RsObject]:
    global RsRoom
    if RsRoom:
        if type(layer) is str:
            Layer = layer_find(layer)
            if not layer:
                return
            Instance = prefab(RsRoom, Layer, x, y)
        else:
            Instance = prefab(RsRoom, layer, x, y)
        Instance.onAwake()
        RsRoom.SpecificInstancesPot[prefab.name].append(Instance)
        RsRoom.EveryInstancesPot.append(Instance)

        return Instance
    else:
        return None


def instance_destroy(instance: RsObject):
    instance.onDestroy()
    del instance
