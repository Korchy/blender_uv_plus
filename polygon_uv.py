# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_uv_plus

# import mathutils
# from .Vector2d import Vector2d
from mathutils import Vector


class PolygonUV:

    def __init__(self, index, points):
        self._index = index
        self.__points = []
        if isinstance(points, (list, tuple)):
            self.__points = [Vector((point[0], point[1])) for point in points]

    def __repr__(self):
        return "PolygonUV ({}) {}".format(self._index, [(point.x, point.y) for point in self.__points])

    @property
    def index(self):
        return self._index

    @property
    def points(self):
        return self.__points

    @staticmethod
    def polygon_centroid(polygon_data):
        # returns the coordinates of the polygon center by coordinates if its vertexes
        if isinstance(polygon_data, (list, tuple)):
            # polygon_data format = ((0, 0), (1, 0), (1, 1), (0, 1))
            x_list = [vertex[0] for vertex in polygon_data]
            y_list = [vertex[1] for vertex in polygon_data]
            length = len(polygon_data)
            x = sum(x_list) / length
            y = sum(y_list) / length
            return Vector((x, y))
        else:
            print(type(polygon_data))
            return None

    def centroid(self):
        return self.polygon_centroid([(point.x, point.y) for point in self.__points])

    def radius_min(self):
        rez = None
        centroid = self.centroid()
        for point in self.__points:
            radius = (point - centroid).length
            if rez is None or radius < rez:
                rez = radius
        return rez
