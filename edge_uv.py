# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_uv_plus

from mathutils import Vector


class EdgeUV:

    def __init__(self, index, vertex_uv1, vertex_uv2):
        # (int, VertexUV, VertexUV)
        self._index = index
        self._vertices = [vertex_uv1, vertex_uv2]

    def __repr__(self):
        return "EdgeUv(({}) 0: {}, 1: {})". \
            format(self._index, self._vertices[0], self._vertices[1])

    @property
    def vertices(self):
        return self._vertices

    @staticmethod
    def edgepointside(edge, point):
        # (EdgeUv, VertexUV)
        # >0 - right
        # <0 - left
        # ==0 - on edge
        side = (point.x - edge.vertices[0].co.x) * (edge.vertices[1].co.y - edge.vertices[0].co.y) - (point.y - edge.vertices[0].co.y) * (edge.vertices[1].co.x - edge.vertices[0].co.x)
        return -1 if side < 0 else (1 if side > 0 else 0)

    def pointside(self, point):
        return self.edgepointside(self, point)

    def normal(self):
        # return Vector((self._vertices[1].co.y - self._vertices[0].co.y, self._vertices[0].co.x - self._vertices[1].co.x)).normalized()
        return (self._vertices[0].co - self._vertices[1].co).orthogonal().normalized()
