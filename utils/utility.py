import sys

def getXY(shape):
    """Returns list of coordinates and area
    """
    min_x = sys.maxsize
    max_x = 0
    min_y = sys.maxsize
    max_y = 0
    for point in shape.points:
        min_x = min(point.x(), min_x)
        min_y = min(point.y(), min_y)
        max_x = max(point.x(), max_x)
        max_y = max(point.y(), max_y)
        area = (max_y - min_y) * (max_x - min_x)

    return [min_x, min_y, max_x, max_y, area]

def hasIntersect(shape1, shape2):
    """Determine whether 2 shapes has IOU > 0.0
    """
    s1 = getXY(shape1)
    s2 = getXY(shape2)
    return (max(s1[0], s2[0]) < min(s1[2], s2[2])) and (max(s1[1], s2[1]) < min(s1[3], s2[3])), s1[4], s2[4]

