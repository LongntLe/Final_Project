
class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.seen = False


class Segment:
    def __init__(self, name, p, q): # p, q belong to class Point
        self.name = name
        self.leftPoint = p
        self.rightPoint = q
        if q.x < p.x:
            self.leftPoint = q
            self.rightPoint = p

        self.slope = (self.rightPoint.y - self.leftPoint.y) / (self.rightPoint.x - self.leftPoint.x)
        self.intercept = self.leftPoint.y - (self.slope * self.leftPoint.x)

    def isAbove(self, point):
        if point.y > (self.slope * point.x) + self.intercept:
            return True
        return False

    def getY(self, x):
        if self.leftPoint.x <= x <= self.rightPoint.x:
            return (self.slope * x) + self.intercept
        return None