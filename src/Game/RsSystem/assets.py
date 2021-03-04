from typing import Optional, Union

from Game.RsSystem import constants as RsConstants, containers as RsContainers
from Game.RsSystem.scene import Scene


def room_add(name: str):
    global RsRoom
    Temp = Scene(name)

    RsRoom = Temp
    Temp.index = len(RsContainers.RoomOrder)
    for explicit_layer in RsConstants.layer_default:
        Temp.add_layer(explicit_layer)

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

    try:
        Temp: Scene = next(RsRoom)
    except StopIteration:
        raise RuntimeError("The next room doesn't exist.\n")
    else:
        room_set(Temp)
