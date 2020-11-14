# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_uv_plus

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class UV_PLUS_PT_panel(Panel):
    bl_idname = 'UV_PLUS_PT_panel'
    bl_label = 'UV Plus'
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'UV Plus'

    def draw(self, context):
        box = self.layout.box()
        box.operator('uv_plus.separate', icon='UNLINKED')
        box.operator('uv_plus.separate_by_edge', icon='UNLINKED')
        self.layout.separator()
        self.layout.operator('uv_plus.weld', icon='LINKED')


def register():
    register_class(UV_PLUS_PT_panel)


def unregister():
    unregister_class(UV_PLUS_PT_panel)
