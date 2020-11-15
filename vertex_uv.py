# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_uv_plus

# from mathutils import Vector


class VertexUV:

    def __init__(self, mesh_uv_loop, polygon):
        # self._vector = Vector((mesh_uv_loop.uv.x, mesh_uv_loop.uv.y))
        self._mesh_uv_loop = mesh_uv_loop
        self._polygon = polygon

    def __repr__(self):
        return "VertexUv(x: {}, y: {}, Polygon: {})". \
            format(self._mesh_uv_loop.uv.x, self._mesh_uv_loop.uv.y, self._polygon)

    @property
    def polygon(self):
        return self._polygon

    @property
    def co(self):
        return self._mesh_uv_loop.uv

    def moveto(self, x, y):
        # self._vector.x = x
        # self._vector.y = y
        self._mesh_uv_loop.uv.x = x
        self._mesh_uv_loop.uv.y = y
