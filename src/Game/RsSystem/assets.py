from typing import Optional, Union

from Game.RsSystem import constants as RsConstants, containers as RsContainers
from Game.RsSystem.instance import RsObject
from Game.RsSystem.layer import RsLayer
from Game.RsSystem.prefab import RsPrefab
from Game.RsSystem.scene import Scene

__all__ = [
    "scene_update", "room_add", "room_get", "room_goto", "room_goto_next", "instance_create"
]


async def scene_update(room: Scene, time: int) -> None:
    room.onUpdate(time)
    room.onUpdateLater(time)
    room.onDraw(time)
    room.onGUI(time)

def room_add(name: str):
    global RsRoom, RsLastRoom
    Temp: Scene = Scene(name)

    for explicit_layer in RsConstants.layer_default:
        Temp.add_layer(explicit_layer)

    Number = len(RsContainers.RoomOrder)
    if 0 < Number:
        LastRoom = RsContainers.RoomOrder[-1]
        if LastRoom:
            Temp.before = LastRoom
            LastRoom.next = Temp
    else:
        RsRoom = Temp
        RsLastRoom = Temp

    RsContainers.RoomOrder.append(Temp)
    RsContainers.RoomPot[name] = Temp

def room_get(id: Union[int, str]) -> Optional[Scene]:
    if type(id) is int:
        return RsContainers.RoomOrder[id]
    else:
        return RsContainers.RoomPot[id]

def room_set(taget: Scene):
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
        Temp: Scene = Next
        room_set(Temp)
    else:
        raise RuntimeError("The next room doesn't exist.\n")

def instance_create(prefab: type[RsObject], layer: RsLayer, x: float = 0, y: float = 0) -> RsObject:
    Instance = prefab(layer, x, y)

    return Instance
