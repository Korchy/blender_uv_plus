# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_uv_plus

from mathutils import Vector


class PolygonUV:

    def __init__(self, index, points):
        # (int, [(0.0, 1.0), ...])
        self._index = index
        self._points = []
        if isinstance(points, (list, tuple)):
            self._points = [Vector((point[0], point[1])) for point in points]

    def __repr__(self):
        return "PolygonUV ({}) {}".format(self._index, [(point.x, point.y) for point in self._points])

    @property
    def index(self):
        return self._index

    @property
    def points(self):
        return self._points

    @staticmethod
    def centroid_st(vertices):
        # returns the coordinates of the polygon center by coordinates if its vertexes
        # (Vector, Vector, ...)
        if isinstance(vertices, (list, tuple)):
            # vertices format = ((0, 0), (1, 0), (1, 1), (0, 1))
            x_list = [vertex[0] for vertex in vertices]
            y_list = [vertex[1] for vertex in vertices]
            length = len(vertices)
            x = sum(x_list) / length
            y = sum(y_list) / length
            return Vector((x, y))
        else:
            print(type(vertices))
            return None

    def centroid(self):
        return self.centroid_st([(point.x, point.y) for point in self._points])

    def radius_min(self):
        rez = None
        centroid = self.centroid()
        for point in self._points:
            radius = (point - centroid).length
            if rez is None or radius < rez:
                rez = radius
        return rez
