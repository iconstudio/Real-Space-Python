import sys
import asyncio

import pygame
from pygame.time import Clock


if __name__ is "__main__":
    pygame.init()
    absolute_timer = Clock()

    black = (0, 0, 0)
    from Game import constants as RsConstants
    screen = pygame.display.set_mode(RsConstants.Resolutions)

    from Game import containers as RsContainers
    Stage = RsContainers.Rooms

    from Game.Scenes.scene_intro import SceneIntro
    Current_scene = SceneIntro()
    Stage.append(Current_scene)

    if not Current_scene:
        raise RuntimeError("No scene found")

    # Start
    Current_scene.onAwake()
    while Current_scene.running:
        RsContainers.Events = pygame.event.get()
        for event in RsContainers.Events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.MOUSEBUTTONUP:
                pass

        frame_time = absolute_timer.get_time()
        screen.fill(black)
        asyncio.run(Current_scene.onUpdate(frame_time))
        asyncio.run(Current_scene.onUpdateLater(frame_time))
        asyncio.run(Current_scene.onDraw(frame_time))
        asyncio.run(Current_scene.onGUI(frame_time))

        pygame.display.flip()
        absolute_timer.tick()

    Current_scene.onDestroy()
    if 0 < len(Stage):
        Current_scene = Stage.pop()
        Current_scene.onAwake()

    print("Program is ended.")
    pygame.quit()
