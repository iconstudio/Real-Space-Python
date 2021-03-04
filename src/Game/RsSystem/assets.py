from typing import Optional, Union

from Game.RsSystem import constants as RsConstants, containers as RsContainers
from Game.RsSystem.scene import Scene


def room_add(name: str):
    Temp = Scene(name)
    Temp.index = len(RsContainers.RoomOrder)
    RsContainers.RoomOrder.append(Temp)
    RsContainers.RoomPot[name] = Temp

def room_get(id: Union[int, str]) -> Optional[Scene]:
    if type(id) is int:
        return RsContainers.RoomOrder[id]
    else:
        return RsContainers.RoomPot[id]

def room_goto(name: str):
    global RsRoom

    Temp = room_get(name)
    if not Temp:
        raise RuntimeError("The room " + name + " doesn't exist.")
    elif Temp is not RsRoom:
        RsRoom.onDestroy()
        RsRoom = Temp
        RsRoom.onAwake()

def room_goto_next():
    global RsRoom

    try:
        Temp: Optional[Scene] = next(RsRoom)
    except StopIteration:
        raise RuntimeError("")
    else:
        RsRoom.onDestroy()
        RsRoom = Temp
        RsRoom.onAwake()
        

