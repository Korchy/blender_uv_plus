# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_uv_plus


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
    def which_side_point_is_st(edge, point):
        # (EdgeUv, Vector)
        # >0 - right
        # <0 - left
        # ==0 - on edge
        side = (point.x - edge.vertices[0].co.x) * (edge.vertices[1].co.y - edge.vertices[0].co.y) - (point.y - edge.vertices[0].co.y) * (edge.vertices[1].co.x - edge.vertices[0].co.x)
        return -1 if side < 0 else (1 if side > 0 else 0)

    def which_side_point_is(self, point):
        return self.which_side_point_is_st(self, point)

    def orthogonal(self):
        return (self._vertices[0].co - self._vertices[1].co).orthogonal().normalized()
