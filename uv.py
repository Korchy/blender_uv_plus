# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_uv_plus

from .vertex_uv import VertexUV
from .edge_uv import EdgeUV
from .polygon_uv import PolygonUV
import copy


class UVMap:

    @staticmethod
    def get_selected_multi_points(mesh_data):
        # return list of points (multipoints). to every point add a structure with connected vertices, edges, polygons
        # one multipoint - is a set of uv vertices at the same position (with the same coordinates)
        # {multipoints:
        #   (0.0, 1.0) = {vertices: [VertexUV, ...], edges: [EdgeUV, ...], polygons: [PolygonUV, ...]}
        #   (0.5, 0.5) = {vertices: [VertexUV, ...], edges: [EdgeUV, ...], polygons: [PolygonUV, ...]}
        # }
        data = {'multi_points': {}}
        multi_point_data = {'vertices': [], 'edges': [], 'polygons': []}
        for polygon_index, polygon in enumerate(mesh_data.polygons):
            for i1, i in enumerate(polygon.loop_indices):
                mesh_uv_loop = mesh_data.uv_layers.active.data[i]
                mesh_uv_loop_prev = mesh_data.uv_layers.active.data[i - 1 if i1 > 0 else i + len(polygon.loop_indices) - 1]
                mesh_uv_loop_next = mesh_data.uv_layers.active.data[i + 1 if (i1 < (len(polygon.loop_indices) - 1)) else (i - (len(polygon.loop_indices) - 1))]
                if mesh_uv_loop.select:
                    if mesh_uv_loop.uv[:] not in data['multi_points']:
                        data['multi_points'][mesh_uv_loop.uv[:]] = copy.deepcopy(multi_point_data)
                    if mesh_uv_loop_next.select and mesh_uv_loop_next.uv[:] not in data['multi_points']:
                        data['multi_points'][mesh_uv_loop_next.uv[:]] = copy.deepcopy(multi_point_data)
                    polygon_uv = PolygonUV(polygon_index, [(mesh_data.uv_layers.active.data[i2].uv[:]) for i2 in polygon.loop_indices])
                    vertex_uv = VertexUV(mesh_uv_loop, polygon_uv)
                    vertex_uv_next = VertexUV(mesh_uv_loop_next, polygon_uv)
                    edge_uv = None
                    if mesh_uv_loop_next.select:
                        edge_uv = EdgeUV(index=i1, vertex_uv1=vertex_uv, vertex_uv2=vertex_uv_next)
                    data['multi_points'][mesh_uv_loop.uv[:]]['vertices'].append(vertex_uv)
                    if edge_uv:
                        # edges
                        data['multi_points'][mesh_uv_loop.uv[:]]['edges'].append(edge_uv)
                        data['multi_points'][mesh_uv_loop_next.uv[:]]['edges'].append(edge_uv)
                    if polygon_uv.index not in [polygon1.index for polygon1 in data['multi_points'][mesh_uv_loop.uv[:]]['polygons']]:
                        data['multi_points'][mesh_uv_loop.uv[:]]['polygons'].append(polygon_uv)
        return data
