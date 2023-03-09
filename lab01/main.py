

import math


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance(self, point2):
        x = max(self.x, point2.x) - min(self.x, point2.x)
        y = max(self.y, point2.y) - min(self.y, point2.y)

        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))


class Points:

    def __init__(self, *points: Point):
        self.points = list(points)

    def addPoint(self, x: int, y: int):
        point = Point(x, y)
        self.points.append(point)

    def distance(self):
        distance = 0
        for i, _ in enumerate(self.points[:-1]):
            distance += self.points[i].distance(self.points[i + 1])

        return distance

    def polygon(self):
        polygon = 0
        localPoints = self.points[:]

        lastElement = localPoints[:-1]
        firstElement = localPoints[0]

        if (firstElement != lastElement):
            localPoints.append(firstElement)

        for i, _ in enumerate(localPoints[:-1]):
            polygon += (localPoints[i].x * localPoints[i + 1].y) - \
                (localPoints[i + 1].x * localPoints[i].y)

        return abs(polygon / 2)


def avg_marks(values, scales):
    sum = 0
    scalesSum = 0
    for value, scale in zip(values, scales):
        sum += value * scale
        scalesSum += scale

    return sum / scalesSum


def strong(num):
    if num == 0:
        return 1

    return num * strong(num - 1)


points = Points(Point(1, 1), Point(1, 3), Point(3, 3), Point(3, 1))

print(points.polygon())
print(points.distance())
