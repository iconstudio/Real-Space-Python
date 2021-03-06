import asyncio
import sys

import pygame
import pygame.constants as PyConstants
import pygame.display as PyDisplay
import pygame.event as PyEvent
from pygame.time import Clock as Clock

from RsCore.scene import RsScene
from RsCore.layer import RsLayer
from RsCore.prefab import RsPrefab
from RsCore.instance import RsObject
from RsCore.sprite import RsSprite
from RsCore import constants as RsConstants, containers as RsContainers
from RsCore.assets import *

import Game

RsScreen = None
RsRoom = None


async def event_collect():
    # TODO: #1 summary events in a list for each types.
    RsContainers.Events = PyEvent.get()
    for event in RsContainers.Events:
        if event.type == PyConstants.QUIT:
            rs_quit()
        elif event.type == PyConstants.KEYDOWN and event.key == PyConstants.K_ESCAPE:
            rs_quit()
        elif event.type == PyConstants.MOUSEBUTTONDOWN:
            room_goto_next()
        elif event.type == PyConstants.MOUSEBUTTONUP:
            pass

    return len(RsContainers.Events)


def init():
    global RsScreen, RsRoom

    pygame.init()
    PyDisplay.init()
    PyDisplay.set_caption("Real Space")
    PyDisplay.set_allow_screensaver(False)
    RsScreen = PyDisplay.set_mode(RsConstants.Resolutions)

    # Test
    TestLayer1 = RsLayer("Test 1")
    TestLayer2 = RsLayer("Test 2")
    TestInstance = RsObject(TestLayer1)
    TestInstance.x = 40
    TestInstance.y = 70
    print(TestLayer1)
    print(TestLayer2)
    TestInstance.layer = TestLayer2
    print("x = " + str(TestInstance.x))
    print(TestInstance)
    TestInstance.x = 70
    TestInstance.x += 20
    print("x = " + str(TestInstance.x))

    # Startup
    Game.init()
    Rooms = RsContainers.RoomOrder
    RsRoom = Rooms[0]
    if not RsRoom:
        raise RuntimeError("No scene found.")

    absolute_timer = Clock()

    # Load rooms
    print(RsRoom)
    RsRoom.onAwake()
    while True:
        frame_time: int = 0 if RsRoom.paused else absolute_timer.get_time()
        RsScreen.fill(RsConstants.c_black)

        asyncio.run(event_collect())
        asyncio.run(scene_update(RsRoom, frame_time))

        PyDisplay.flip()
        absolute_timer.tick()


def rs_quit():
    rs_cleanup()
    sys.exit()


def rs_cleanup():
    print("Program is ended.")
    pygame.quit()
