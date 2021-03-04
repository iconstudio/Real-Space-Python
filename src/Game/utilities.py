import math
import random
from typing import Union


def lengthdir_x(Length: float, Direction: float) -> float:
    return math.cos(math.radians(Direction)) * Length


def lengthdir_y(Length: float, Direction: float) -> float:
    return -math.sin(math.radians(Direction)) * Length


def point_distance(X1: float, Y1: float, X2: float, Y2: float) -> float:
    return math.dist([X1, Y1], [X2, Y2])


def point_direction(X1: float, Y1: float, X2: float, Y2: float) -> float:
    return math.degrees(math.atan2(Y2 - Y1, X1 - X2))


def irandom(n: Union[int, float]) -> int:
    return random.randint(0, int(n))


def irandom_range(n1: Union[int, float], n2: Union[int, float]) -> int:
    return random.randint(int(n1), int(n2))


def distribute(x1: float, x2: float, ratio: float) -> float:
    if irandom(100) <= ratio * 100:
        return x1
    else:
        return x2


def probability_test(max: Union[int, float]) -> bool:
    return bool(irandom(max - 1) == 0)


# choice random
def choose(*args):
    length = len(args)
    if length <= 0:
        raise RuntimeError("choose 함수에 값이 제대로 전달되지 않았습니다!" + __name__)

    pick = None
    try:
        pick = args[irandom(length - 1)]
    except ValueError:
        pass
    return pick
