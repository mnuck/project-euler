#/usr/bin/env python
#
# Project Euler 102

class Point(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

class Triangle(object):
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        self.A = Point(Ax, Ay)
        self.B = Point(Bx, By)
        self.C = Point(Cx, Cy)

    def contains_origin(self):
        ABO = areaish(self.A.x, self.A.y, self.B.x, self.B.y, 0, 0)
        if ABO == 0:
            return True
        ACO = areaish(self.A.x, self.A.y, self.C.x, self.C.y, 0, 0)
        if ACO == 0:
            return True
        BCO = areaish(self.B.x, self.B.y, self.C.x, self.C.y, 0, 0)
        if BCO == 0:
            return True
        ABC = areaish(self.A.x, self.A.y, self.B.x, self.B.y, 
                      self.C.x, self.C.y)
        if ABC == (ABO + ACO + BCO):
            return True
        return False


def areaish(Ax, Ay, Bx, By, Cx, Cy):
    return abs(Ax*(By - Cy) + Bx*(Cy - Ay) + Cx*(Ay - By)) / 2


def read_triangles(filename):
    with open(filename) as f:
        for line in f.readlines():
            yield Triangle(*[int(x) for x in line.split(',')])


def solution():
    return sum(1 for x in read_triangles("triangles.txt") 
               if x.contains_origin())


if __name__ == "__main__":
    print solution()
