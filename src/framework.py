import sys
try:
    import pygame
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

    room_add("roomInit")
    room_add("roomLogo")
    room_add("roomIntro")
    room_add("roomMain")
    room_add("roomDemo")
    room_add("roomStage01")
    room_add("roomStage02")
    room_add("roomStage03")

def endup():
    print("Program is ended.")
    pygame.quit()

def startup():
    global RsScreen, RsRoom

    Rooms = RsContainers.RoomOrder
    RsRoom = Rooms[0]
    if not RsRoom:
        raise RuntimeError("No scene found")

    absolute_timer = Clock()

    # Start
    print(RsRoom)
    RsRoom.onAwake()
    while True:
        RsContainers.Events = pygame.event.get()
        for event in RsContainers.Events:
            if event.type == PyConstants.QUIT:
                sys.exit()
            elif event.type == PyConstants.KEYDOWN and event.key == PyConstants.K_ESCAPE:
                sys.exit()
            elif event.type == PyConstants.MOUSEBUTTONDOWN:
                room_goto_next()
            elif event.type == PyConstants.MOUSEBUTTONUP:
                pass

        frame_time: int = 0 if RsRoom.paused else absolute_timer.get_time()
        RsScreen.fill(RsConstants.c_black)
        RsRoom.onUpdate(frame_time)
        RsRoom.onUpdateLater(frame_time)
        RsRoom.onDraw(frame_time)
        RsRoom.onGUI(frame_time)

        PyDisplay.flip()
        absolute_timer.tick()

