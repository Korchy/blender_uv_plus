# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_uv_plus

from mathutils import Vector
from .vertex_uv import VertexUV
from .edge_uv import EdgeUV
from .polygon_uv import PolygonUV
import copy


class UVMap:

    @staticmethod
    def get_selected_multi_points(mesh_data):
        # return list of points which have the same coordinates. to every point add a structure with connected vertices, edges, polygons
        data = {'multi_point': {}}
        multi_point_data = {'vertices': [], 'edges': [], 'polygons': [], 'edges_map': []}
        for polygon_index, polygon in enumerate(mesh_data.polygons):
            for i1, i in enumerate(polygon.loop_indices):
                mesh_uv_loop = mesh_data.uv_layers.active.data[i]
                mesh_uv_loop_prev = mesh_data.uv_layers.active.data[i - 1 if i1 > 0 else i + len(polygon.loop_indices) - 1]
                mesh_uv_loop_next = mesh_data.uv_layers.active.data[i + 1 if (i1 < (len(polygon.loop_indices) - 1)) else (i - (len(polygon.loop_indices) - 1))]
                if mesh_uv_loop.select:
                    if mesh_uv_loop.uv[:] not in data['multi_point']:
                        data['multi_point'][mesh_uv_loop.uv[:]] = copy.deepcopy(multi_point_data)
                    if mesh_uv_loop_next.select and mesh_uv_loop_next.uv[:] not in data['multi_point']:
                        data['multi_point'][mesh_uv_loop_next.uv[:]] = copy.deepcopy(multi_point_data)
                    polygon_uv = PolygonUV(polygon_index, [(mesh_data.uv_layers.active.data[i2].uv[:]) for i2 in polygon.loop_indices])
                    vertex_uv = VertexUV(mesh_uv_loop, polygon_uv)
                    edge_uv = None
                    if mesh_uv_loop_next.select:
                        edge_uv = EdgeUV(i1, vertex_uv, VertexUV(mesh_uv_loop_next, polygon_uv))
                    data['multi_point'][mesh_uv_loop.uv[:]]['vertices'].append(vertex_uv)
                    if edge_uv:
                        # edges
                        data['multi_point'][mesh_uv_loop.uv[:]]['edges'].append(edge_uv)
                        data['multi_point'][mesh_uv_loop_next.uv[:]]['edges'].append(edge_uv)
                        # data['multi_point'][mesh_uv_loop.uv[:]]['edges_map'].append(EdgeUV(i1, Vector((edge_uv.vertices[0].x, edge_uv.vertices[0].y)), Vector((edge_uv.vertices[1].x, edge_uv.vertices[1].y))))
                        # data['multi_point'][mesh_uv_loop_next.uv[:]]['edges_map'].append(EdgeUV(i1, Vector2d(edge_uv.vertices[0].x, edge_uv.vertices[0].y), Vector2d(edge_uv.vertices[1].x, edge_uv.vertices[1].y)))
                        data['multi_point'][mesh_uv_loop.uv[:]]['edges_map'].append(
                            EdgeUV(i1, VertexUV(mesh_uv_loop, polygon_uv), VertexUV(mesh_uv_loop_next, polygon_uv))
                        )
                        data['multi_point'][mesh_uv_loop_next.uv[:]]['edges_map'].append(
                            EdgeUV(i1, VertexUV(mesh_uv_loop, polygon_uv), VertexUV(mesh_uv_loop_next, polygon_uv))
                        )
                    if polygon_uv.index not in [polygon1.index for polygon1 in data['multi_point'][mesh_uv_loop.uv[:]]['polygons']]:
                        data['multi_point'][mesh_uv_loop.uv[:]]['polygons'].append(polygon_uv)
        return data
