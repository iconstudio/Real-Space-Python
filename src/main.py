import sys

import pygame
import pygame.time as PyTime

import constants
import containers

if __name__ == "__main__":
    pygame.init()

    black = (0, 0, 0)
    screen = pygame.display.set_mode(constants.Resolutions)
    absolute_timer = PyTime.Clock()

    import Scenes.scene_intro as Intro
    from Scenes.scene_intro import SceneIntro

    Intro.storage += 7
    Scenes = containers.Rooms
    Current_scene = SceneIntro()
    Scenes.append(Current_scene)

    if not Current_scene:
        raise RuntimeError("No scene found")

    Current_scene.onAwake()

    # Start
    while Current_scene.running:
        for event in pygame.event.get():
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
        Current_scene.onUpdate(frame_time)
        Current_scene.onUpdateLater(frame_time)
        Current_scene.onDraw(frame_time)
        Current_scene.onGUI(frame_time)

        pygame.display.flip()
        absolute_timer.tick()

    Current_scene.onDestroy()
    if 0 < len(Scenes):
        Current_scene = Scenes.pop()
        Current_scene.onAwake()

    print("Program is ended.")
    pygame.quit()
