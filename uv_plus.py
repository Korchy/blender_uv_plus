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
        # separate (blast) points
        for polygon in mesh_data.polygons:
            polygon_vertices_co = [(mesh_data.uv_layers.active.data[index].uv[:]) for index in polygon.loop_indices]  # uv[:] - Vector -> tuple
            polygon_center = PolygonUV.centroid_st(vertices=polygon_vertices_co)
            for i in polygon.loop_indices:
                mesh_uv_loop = mesh_data.uv_layers.active.data[i]
                if mesh_uv_loop.select:
                    move_to = (mesh_uv_loop.uv - polygon_center) * 0.8 + polygon_center
                    mesh_uv_loop.uv.x = move_to.x
                    mesh_uv_loop.uv.y = move_to.y

    @classmethod
    def separate_by_edge(cls, mesh_data):
        # separate points by selected edges
        selected_data = UVMap.get_selected_multi_points(mesh_data=mesh_data)
        if selected_data:
            # make a list with vertices to move to make a seam (prepare not to influence on next vertices processing)
            vertex_move_to = []  # [VertexUV, [x,y]] - move VertexUV to x,y
            for multipoint in selected_data['multi_points']:
                # find length to move vertices = 0.2 of min radius of all polygons connected to seam
                moving_length = None
                for polygon in selected_data['multi_points'][multipoint]['polygons']:
                    radius_min = polygon.radius_min()
                    if moving_length is None or moving_length > radius_min:
                        moving_length = radius_min
                moving_length *= 0.2
                # find the new vertex position
                for vertex in selected_data['multi_points'][multipoint]['vertices']:
                    for edge in selected_data['multi_points'][multipoint]['edges']:
                        sign = edge.which_side_point_is(vertex.polygon.centroid())
                        if edge.vertices[0].co.x == multipoint[0] and edge.vertices[0].co.y == multipoint[1]:  # for input edges
                            already_appended = next((item for item in vertex_move_to if item[0] == vertex), None)
                            if already_appended:
                                # already appended vertex - sum move_to coordinates
                                already_appended[1][0] += sign * moving_length * edge.orthogonal().x
                                already_appended[1][1] += sign * moving_length * edge.orthogonal().y
                            else:
                                # new vertex - add move_to coordinates
                                vertex_move_to.append(
                                    [
                                        vertex,
                                        [
                                            vertex.co.x + sign * moving_length * edge.orthogonal().x,
                                            vertex.co.y + sign * moving_length * edge.orthogonal().y
                                        ]
                                    ]
                                )
            # real moving
            for vertex in vertex_move_to:
                vertex[0].move_to(
                    x=vertex[1][0],
                    y=vertex[1][1]
                )
