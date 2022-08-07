#====================== BEGIN GPL LICENSE BLOCK ======================
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#======================= END GPL LICENSE BLOCK ========================

import bpy
from bpy.app.handlers import persistent

# Version History
# 1.0.0 - 2020-09-06: First version
# 1.0.1 - 2022-08-07: Misc formatting cleanup before uploading to GitHub.

bl_info = {
    "name" : "Limit Arrow Keys Keyframe Range",
    "author" : "Jeff Boller",
    "version" : (1, 0, 1),
    "blender" : (2, 93, 0),
    "location" : "UI",
    "description" : "This Blender add-on keeps the timeline cursor between the preview range (if the Timeline's Use Preview Range option is turned on). " \
                    "If you use the arrow keys to move through the frames, when you reach the end of the loop, the cursor will go back to the other side of the loop. " \
                    "Likewise, if Timeline's Use Preview Range option is turned on and you click outside of the range of the frames, " \
                    "the cursor will stay within the range of the loop.",
    "wiki_url": "https://github.com/sundriftproductions/blenderaddon-limit-arrow-keys-keyframe-range/wiki",
    "tracker_url": "https://github.com/sundriftproductions/blenderaddon-limit-arrow-keys-keyframe-range",
    "category" : "UI"
}

@persistent
def load_handler(scn):
    handle_handlers_draw_header_col()

def handle_handlers_draw_header_col():
    if LIMIT_ARROW_KEYS_KEYFRAME_RANGE_prefset not in bpy.app.handlers.frame_change_pre:
        bpy.app.handlers.frame_change_pre.append(LIMIT_ARROW_KEYS_KEYFRAME_RANGE_prefset)

def LIMIT_ARROW_KEYS_KEYFRAME_RANGE_prefset(scene):
    if bpy.context.scene.use_preview_range and bpy.context.scene.frame_preview_start != bpy.context.scene.frame_preview_end:
        current = bpy.context.scene.frame_current

        if (current == (bpy.context.scene.frame_preview_end + 1)) or (current < (bpy.context.scene.frame_preview_start - 1)):
            bpy.context.scene.frame_set(bpy.context.scene.frame_preview_start)
        elif (current == (bpy.context.scene.frame_preview_start - 1)) or (current > (bpy.context.scene.frame_preview_end + 1)):
            bpy.context.scene.frame_set(bpy.context.scene.frame_preview_end)

def register():
    bpy.app.handlers.load_post.append(load_handler)

def unregister():
    bpy.app.handlers.load_post.remove(load_handler)

if __name__ == "__main__":
    register()
