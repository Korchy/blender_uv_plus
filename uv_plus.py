# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_uv_plus

from .polygon_uv import PolygonUV
from .uv import UVMap


class UVPlus:

    @classmethod
    def separate(cls, mesh_data):
        # separate points
        for polygon in mesh_data.polygons:
            polygon_data = [(mesh_data.uv_layers.active.data[index].uv[:]) for index in polygon.loop_indices]  # uv[:] - Vector -> tuple
            polygon_center = PolygonUV.polygon_centroid(polygon_data)
            for i in polygon.loop_indices:
                mesh_uv_loop = mesh_data.uv_layers.active.data[i]
                if mesh_uv_loop.select:
                    moveto = (mesh_uv_loop.uv - polygon_center) * 0.8 + polygon_center
                    mesh_uv_loop.uv.x = moveto.x
                    mesh_uv_loop.uv.y = moveto.y

    @classmethod
    def separate_by_edge(cls, mesh_data):
        # separate points by edge
        selected_data = UVMap.get_selected_multi_points(mesh_data=mesh_data)
        if selected_data:
            for pointgoup in selected_data['multi_point']:
                edgescount = len(selected_data['multi_point'][pointgoup]['edges_map'])
                movinglength = None
                for polygon in selected_data['multi_point'][pointgoup]['polygons']:
                    print(polygon)
                    radius_min = polygon.radius_min()
                    if movinglength is None or movinglength > radius_min:
                        movinglength = radius_min
                movinglength /= 3
                movinglength /= edgescount  # делить нм колв-во ребер входящих в группу
                for point in selected_data['multi_point'][pointgoup]['vertices']:
                    for edge in selected_data['multi_point'][pointgoup]['edges_map']:
                        sign = edge.pointside(point.polygon.centroid())
                        if edge.vertices[0].co.x == pointgoup[0] and edge.vertices[0].co.y == pointgoup[1]:  # for input edges
                            point.moveto(point.co.x + sign * movinglength * edge.normal().x, point.co.y + sign * movinglength * edge.normal().y)
