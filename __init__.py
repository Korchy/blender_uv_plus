# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_uv_plus

from . import uv_plus_ops
from . import uv_plus_ui
from .addon import Addon


bl_info = {
    'name': 'uv_plus',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 90, 0),
    'location': 'UV Editor - N-panel - UV Plus',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-uv-plus/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-uv-plus/',
    'description': 'Additional tools for UV Editor'
}


def register():
    if not Addon.dev_mode():
        uv_plus_ops.register()
        uv_plus_ui.register()
    else:
        print('It seems you are trying to use the dev version of the ' + bl_info['name'] + ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        uv_plus_ui.unregister()
        uv_plus_ops.unregister()


if __name__ == '__main__':
    register()
