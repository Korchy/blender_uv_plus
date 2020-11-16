# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_uv_plus


class VertexUV:

    def __init__(self, mesh_uv_loop, polygon):
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

    def move_to(self, x, y):
        self._mesh_uv_loop.uv.x = x
        self._mesh_uv_loop.uv.y = y
