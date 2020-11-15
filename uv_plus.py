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
        # print(selected_data)
        if selected_data:
            p = []  # (point, (x,y))
            for multipoint in selected_data['multi_points']:
                print('-')
                print(multipoint)
                # edgescount = len(selected_data['multi_points'][multipoint]['edges_map'])
                # print(edgescount)
                movinglength = None
                for polygon in selected_data['multi_points'][multipoint]['polygons']:
                    # print(polygon)
                    radius_min = polygon.radius_min()
                    # print(radius_min)
                    if movinglength is None or movinglength > radius_min:
                        movinglength = radius_min
                movinglength /= 3
                # movinglength /= edgescount  # делить нм колв-во ребер входящих в группу
                # p = []  # (point, (x,y))
                for point in selected_data['multi_points'][multipoint]['vertices']:
                    print('')
                    print(point)
                    for edge in selected_data['multi_points'][multipoint]['edges_map']:
                        print('edge', edge)
                        sign = edge.pointside(point.polygon.centroid())
                        print('sign', sign)
                        if edge.vertices[0].co.x == multipoint[0] and edge.vertices[0].co.y == multipoint[1]:  # for input edges
                        #     point.moveto(point.co.x + sign * movinglength * edge.normal().x, point.co.y + sign * movinglength * edge.normal().y)
                            print('edge normal', edge.normal())
                            print('move_to x:', point.co.x + sign * movinglength * edge.normal().x)
                            print('move_to y:', point.co.y + sign * movinglength * edge.normal().y)
                            # point.moveto(point.co.x + sign * movinglength * edge.normal().x, point.co.y + sign * movinglength * edge.normal().y)
                            p.append((point, (point.co.x + sign * movinglength * edge.normal().x, point.co.y + sign * movinglength * edge.normal().y)))
            for elem in p:
                elem[0].moveto(elem[1][0], elem[1][1])
