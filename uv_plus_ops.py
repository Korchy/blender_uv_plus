# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_uv_plus

import bpy
from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from .uv_plus import UVPlus


class UV_PLUS_OT_separate(Operator):
    bl_idname = 'uv_plus.separate'
    bl_label = 'Blast points'
    bl_description = 'Separate all selected UV points'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # separate all selected points
        bpy.ops.object.mode_set(mode='OBJECT')
        for obj in context.selected_objects:
            UVPlus.separate(
                mesh_data=obj.data
            )
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        if context.active_object and context.active_object.data.uv_layers.active and context.selected_objects:
            return True
        else:
            return False


class UV_PLUS_OT_separate_by_edge(Operator):
    bl_idname = 'uv_plus.separate_by_edge'
    bl_label = 'Separate by edge'
    bl_description = 'Separate all points by selected edge'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # separate all selected points by edge
        bpy.ops.object.mode_set(mode='OBJECT')
        for obj in context.selected_objects:
            UVPlus.separate_by_edge(
                mesh_data=obj.data
            )
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        if context.active_object and context.active_object.data.uv_layers.active and context.selected_objects:
            return True
        else:
            return False


class UV_PLUS_OT_weld(Operator):
    bl_idname = 'uv_plus.weld'
    bl_label = 'Weld'
    bl_description = 'Weld selected points'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # weld
        bpy.ops.uv.weld()
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        if context.active_object and context.active_object.data.uv_layers.active and context.selected_objects:
            return True
        else:
            return False


class UV_PLUS_OT_transfer_selection_to_mesh(Operator):
    bl_idname = 'uv_plus.transfer_selection_to_mesh'
    bl_label = 'Transfer to mesh'
    bl_description = 'Transfer current uv selection tom mes'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # separate all selected points by edge
        bpy.ops.object.mode_set(mode='OBJECT')
        for obj in context.selected_objects:
            UVPlus.transfer_selection_to_mesh(
                mesh_data=obj.data
            )
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        if context.active_object and context.active_object.data.uv_layers.active and context.selected_objects:
            return True
        else:
            return False


def register():
    register_class(UV_PLUS_OT_separate)
    register_class(UV_PLUS_OT_separate_by_edge)
    register_class(UV_PLUS_OT_weld)
    register_class(UV_PLUS_OT_transfer_selection_to_mesh)


def unregister():
    unregister_class(UV_PLUS_OT_transfer_selection_to_mesh)
    unregister_class(UV_PLUS_OT_weld)
    unregister_class(UV_PLUS_OT_separate_by_edge)
    unregister_class(UV_PLUS_OT_separate)
