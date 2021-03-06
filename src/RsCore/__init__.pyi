from typing import Optional

import pygame.constants as PyConstants
import pygame.display as PyDisplay
import pygame.event as PyEvent
from pygame.surface import Surface as PySurface
from pygame.time import Clock as Clock

from .scene import RsScene
from .layer import RsLayer
from .prefab import RsPrefab
from .instance import RsObject
from .sprite import RsSprite
import constants as RsConstants, containers as RsContainers
from .assets import *

RsScreen: Optional[PySurface]
RsRoom: Optional[RsScene]


async def event_collect() -> int:
    ...


def init():
    ...


def rs_cleanup():
    ...


def rs_quit():
    ...
