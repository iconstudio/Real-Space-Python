import sys
import asyncio
try:
    import pygame
    import pygame.event as PyEvent
    import pygame.display as PyDisplay
    import pygame.constants as PyConstants
    from pygame.time import Clock
except (ImportError, IOError):
    print("No pygame module found.")

from Game.RsSystem.scene import Scene
from Game.RsSystem import constants as RsConstants, containers as RsContainers
from Game.RsSystem.assets import *


def init():
    global RsScreen

    pygame.init()
    PyDisplay.set_caption("Real Space")
    PyDisplay.set_allow_screensaver(False)
    RsScreen = PyDisplay.set_mode(RsConstants.Resolutions)

    room_register("roomInit")
    room_register("roomLogo")
    room_register("roomIntro")
    room_register("roomMain")
    room_register("roomDemo")
    room_register("roomStage01")
    room_register("roomStage02")
    room_register("roomStage03")

def endup():
    print("Program is ended.")
    pygame.quit()

async def event_collect() -> int:
    #TODO: #1 summary events in a list for each types.
    RsContainers.Events = PyEvent.get()
    for event in RsContainers.Events:
        if event.type == PyConstants.QUIT:
            endup()
            sys.exit()
        elif event.type == PyConstants.KEYDOWN and event.key == PyConstants.K_ESCAPE:
            endup()
            sys.exit()
        elif event.type == PyConstants.MOUSEBUTTONDOWN:
            room_goto_next()
        elif event.type == PyConstants.MOUSEBUTTONUP:
            pass

    return len(RsContainers.Events)

def startup():
    global RsScreen, RsRoom

    Rooms = RsContainers.RoomOrder
    RsRoom = Rooms[0]
    if not RsRoom:
        raise RuntimeError("No scene found.")

    absolute_timer = Clock()

    # Start
    print(RsRoom)
    RsRoom.onAwake()
    while True:
        frame_time: int = 0 if RsRoom.paused else absolute_timer.get_time()
        RsScreen.fill(RsConstants.c_black)

        asyncio.run(event_collect())
        asyncio.run(scene_update(RsRoom, frame_time))

        PyDisplay.flip()
        absolute_timer.tick()
