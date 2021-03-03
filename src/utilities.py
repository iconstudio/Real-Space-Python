import math

def lengthdir_x(Length:float, Direction:float) -> float:
    return math.cos(math.radians(Direction)) * Length

def lengthdir_y(Length:float, Direction:float) -> float:
    return -math.sin(math.radians(Direction)) * Length

def point_distance(X1:float, Y1:float, X2:float, Y2:float) -> float:
    return math.dist([X1, Y1], [X2, Y2])

def point_direction(X1:float, Y1:float, X2:float, Y2:float) -> float:
    return math.degrees(math.atan2(Y2 - Y1, X1 - X2))
