# Artemy Belzer's Blender Utilities - Additional Blender utilities.
# Copyright (C) 2023 Artemy Belzer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import bpy
import rna_keymap_ui
from . import ab_constants, ab_keymaps, ab_op_menus
from ..lib import ab_fbx

UPDATE_UI : callable = None

def change_pie_menu_label(prefs : bpy.types.AddonPreferences, context : any) -> None:
    new_label : str = ab_constants.plugin_menu_name + (" Pie " if not prefs.alternative_menu else " ") + "Menu"
    ab_op_menus.OBJECT_MT_ab_utility_base_menu_pie.change_bl_label(new_label)

class PanelVars(bpy.types.PropertyGroup):
    tabs : bpy.props.EnumProperty(
        name = "Tabs",
        items=ab_constants.e_pref_tab,
        default = 'GENERAL'
    )

    menu_display_tabs : bpy.props.EnumProperty(
        name = "Tabs",
        items=ab_constants.e_pref_display_tab,
        default = 'SUBMENUS'
    )

    quick_export_name_selection : bpy.props.IntProperty(
        description = "If a part of a child object's name is contained in this list,\nit will always be selected when exporting objects"
    )

class ABUtilQuickExportNames(bpy.types.PropertyGroup):
    arg_type : bpy.props.EnumProperty(
        name = "Type",
        items = ab_constants.e_string_find_action,
        default = 'CONTAINS'
    )

class ABUTIL_UL_name_slots(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        split = layout.split(factor = 0.3)
        split.prop(item, "name", icon = 'OBJECT_DATAMODE', emboss = False, text="")
        split.prop(item, "arg_type")

    def invoke(self, context, event):
        pass

class ABUtilAddonPrefs(bpy.types.AddonPreferences):
    bl_idname = __package__[:len(__package__)-6]

    panel_vars_ptr : bpy.props.PointerProperty(type=PanelVars)

    # Alternative menu
    alternative_menu : bpy.props.BoolProperty(
        name = "Alternative Vertical Menu",
        default = False,
        update = lambda x, y: change_pie_menu_label(x, y)
    )

    # Utilities in properties
    utilties_in_properties : bpy.props.BoolProperty(
        name = "Utilities in the properties panel",
        default = False
    )

    # Quick export collection property
    quick_export_name_collection : bpy.props.CollectionProperty(
        type = ABUtilQuickExportNames
    )

    # Old advanced rename menu
    legacy_rename_menu : bpy.props.BoolProperty(
        name = "Legacy Menu",
        default = False,
        description = "The old Auto/Advanced Rename tool menu before Batch Rename+.\nReplaces Batch Rename+ with the old Auto/Advanced tool menu."
    )

    # Num splitter

    use_unique_num_splitter : bpy.props.BoolProperty(
        name = "Unique Splitter",
        default = False
    )

    num_splitter : bpy.props.StringProperty(
        name = "Number Splitter",
        default = ".",
        description = "Splitter that is used for numbers."
    )

    # Sub-menu display

    submenu_attributes_show : bpy.props.BoolProperty(
        name = "Attributes",
        default = True
    )

    submenu_cleanup_show : bpy.props.BoolProperty(
        name = "Cleanup",
        default = True
    )

    submenu_file_show : bpy.props.BoolProperty(
        name = "File",
        default = True
    )

    submenu_modifiers_show : bpy.props.BoolProperty(
        name = "Modifiers",
        default = True
    )

    submenu_naming_show : bpy.props.BoolProperty(
        name = "Naming",
        default = True
    )

    submenu_objects_show : bpy.props.BoolProperty(
        name = "Objects",
        default = True
    )

    submenu_selection_show : bpy.props.BoolProperty(
        name = "Selection",
        default = True
    )

    submenu_uvs_show : bpy.props.BoolProperty(
        name = "UVs",
        default = True
    )

    submenu_fbx_quick_export_show : bpy.props.BoolProperty(
        name = "FBX Quick Export",
        default = True
    )

    submenu_point_cloud_show : bpy.props.BoolProperty(
        name = "Point cloud",
        default = True
    )

    submenu_colors_show : bpy.props.BoolProperty(
        name = "Colors",
        default = True
    )

    # Button display
    pie_menu_button_spacing_x : bpy.props.IntProperty(
        name = "Spacing Horizontal",
        default = 5
    )

    pie_menu_button_spacing_y : bpy.props.IntProperty(
        name = "Spacing Vertical",
        default = 5
    )


    submenu_attributes_buttons : bpy.props.BoolProperty(
        name = "Attributes",
        default = False
    )

    submenu_cleanup_buttons : bpy.props.BoolProperty(
        name = "Cleanup",
        default = False
    )

    submenu_file_buttons : bpy.props.BoolProperty(
        name = "File",
        default = True
    )

    submenu_modifiers_buttons : bpy.props.BoolProperty(
        name = "Modifiers",
        default = False
    )

    submenu_naming_buttons : bpy.props.BoolProperty(
        name = "Naming",
        default = False
    )

    submenu_objects_buttons : bpy.props.BoolProperty(
        name = "Objects",
        default = False
    )

    submenu_selection_buttons : bpy.props.BoolProperty(
        name = "Selection",
        default = False
    )

    submenu_uvs_buttons : bpy.props.BoolProperty(
        name = "UVs",
        default = False
    )

    submenu_fbx_quick_export_buttons : bpy.props.BoolProperty(
        name = "FBX Quick Export",
        default = False
    )

    submenu_point_cloud_buttons : bpy.props.BoolProperty(
        name = "Point cloud",
        default = False
    )

    submenu_colors_buttons : bpy.props.BoolProperty(
        name = "Colors",
        default = False
    )

    # Panel display

    panel_attributes_show : bpy.props.BoolProperty(
        name = "Attributes",
        default = False
    )

    panel_cleanup_show : bpy.props.BoolProperty(
        name = "Cleanup",
        default = False
    )

    panel_file_show : bpy.props.BoolProperty(
        name = "File",
        default = False
    )

    panel_modifiers_show : bpy.props.BoolProperty(
        name = "Modifiers",
        default = True
    )

    panel_naming_show : bpy.props.BoolProperty(
        name = "Naming",
        default = False
    )

    panel_objects_show : bpy.props.BoolProperty(
        name = "Objects",
        default = False
    )

    panel_selection_show : bpy.props.BoolProperty(
        name = "Selection",
        default = False
    )

    panel_uvs_show : bpy.props.BoolProperty(
        name = "UVs",
        default = False
    )

    panel_fbx_quick_export_show : bpy.props.BoolProperty(
        name = "FBX Quick Export",
        default = True
    )

    panel_point_cloud_show : bpy.props.BoolProperty(
        name = "Point cloud",
        default = True
    )

    panel_colors_show : bpy.props.BoolProperty(
        name = "Colors",
        default = False
    )

    # Exporting

    uses_default_export_path : bpy.props.BoolProperty(
        name = "Use default export path",
        default = False
    )

    default_export_path : bpy.props.StringProperty(
        name = "Default Export Path",
        description = "Quick export directory path",
        subtype = 'DIR_PATH'
    )

    load_viewport_panel : bpy.props.BoolProperty(
        name = "Load viewport panel",
        default = True,
        description = "Loads all the sub panels under the plugin's category."
    )

    auto_numbering : bpy.props.BoolProperty(
        name = "Auto numbering",
        default = False,
        description = "When checked, the Batch Rename+ tool will use a custom numbering convention (ie. \"_##\" vs the regular \".###\")."
    )

    use_a_splitter_between_actions : bpy.props.BoolProperty(
        name = "Use a splitter between actions",
        default = False,
        description = "Adds a splitter between batch naming actions"
    )

    name_splitter : bpy.props.StringProperty(
        name = "Name Splitter",
        default = "_",
        description = "Splitter that is used for auto naming.\n\
        Ex: \"ObjectName<splitter>01\", \
        \"ObjectName<splitter>02\""
    )

    num_padding : bpy.props.IntProperty(
        name = "Zero Padding Count",
        default = 1
    )

    # Panels in properties
    show_object_attribute_utils_in_properties : bpy.props.BoolProperty(
        name = "Attribute Utilities in object properties",
        default = True
    )

    show_data_attribute_utils_in_properties : bpy.props.BoolProperty(
        name = "Attribute Utilities in data properties",
        default = True
    )

    show_color_attribute_utils_in_properties : bpy.props.BoolProperty(
        name = "Color Utilities in data properties",
        default = True
    )

    show_uv_attribute_utils_in_properties : bpy.props.BoolProperty(
        name = "UV Utilities in data properties",
        default = True
    )


    # Exporting

    fbx_exporter_type : bpy.props.EnumProperty(
        name = "Exporter Type",
        default = 'NATIVE',
        items = ab_fbx.exporter_type
    )

    native_fbx_ex_check_existing : bpy.props.BoolProperty(
        name = "Check Existing",
        default = False,
        description = "When set to true, the FBX file will not export if it already exists"
    )

    native_fbx_ex_scale_options : bpy.props.EnumProperty(
        name = "Scale Option",
        items = ab_fbx.scale_options,
        default = 'FBX_SCALE_CUSTOM',
        description = "The scale option for the FBX file.\n\
        It's recommended to use 'FBX_SCALE_CUSTOM' as that will export the scale as (1,1,1)"
    )

    native_fbx_ex_export_empty : bpy.props.BoolProperty(
        name = "Empty",
        default = True
    )

    native_fbx_ex_export_camera : bpy.props.BoolProperty(
        name = "Camera",
        default = False
    )

    native_fbx_ex_export_light : bpy.props.BoolProperty(
        name = "Light",
        default = False
    )

    native_fbx_ex_export_armature : bpy.props.BoolProperty(
        name = "Armature",
        default = True
    )

    native_fbx_ex_export_mesh : bpy.props.BoolProperty(
        name = "Mesh",
        default = True
    )

    native_fbx_ex_export_other : bpy.props.BoolProperty(
        name = "Other",
        default = False
    )

    native_fbx_ex_mesh_smooth_type : bpy.props.EnumProperty(
        name = "Mesh smooth type",
        items = ab_fbx.mesh_smooth_types,
        default = 'OFF',
        description = "Mesh smoothing export.\n\
            Setting this to 'OFF' will export vertex normals.\n\
            Setting this to anything else will export either 'FACE' or 'EDGE' smoothing."
    )

    native_fbx_ex_use_tspace : bpy.props.BoolProperty(
        name = "Use Tangent Space",
        default = True,
        description = "Exports binormal and tangent vectors"
    )

    native_fbx_ex_use_custom_props : bpy.props.BoolProperty(
        name = "Export Custom Properties",
        default = True,
        description = "Exports custom properties"
    )

    # Keymaps

    do_not_load_keymaps : bpy.props.BoolProperty(
        name = "Skip Loading",
        default = False,
        description = "Prevents loading keymaps on start"
    )

    reload_missing_keymaps : bpy.props.BoolProperty(
        name = "Reload Missing",
        default = True,
        description = "Automatically adds in missing keymaps from the user keyconfig."
    )
    
    def draw(self, context) -> None:
        layout = self.layout  # bpy.types.UILayout
        
        column = layout.column(align=True)
        row = column.row()
        row.prop(self.panel_vars_ptr, "tabs", expand=True)

        box = column.box()

        if self.panel_vars_ptr.tabs == 'GENERAL':
            self.__draw_general(context, box)
        elif self.panel_vars_ptr.tabs == 'NAMING':
            self.__draw_naming(box)
        elif self.panel_vars_ptr.tabs == 'KEYS':
            self.__draw_keymaps(box)
        elif self.panel_vars_ptr.tabs == 'QUICK_EXPORT':
            self.__draw_quick_export(box)
        elif self.panel_vars_ptr.tabs == 'ADVANCED':
            self.__draw_advanced(box)

    def __draw_quick_export_names(self, parent) -> None:
        box = parent.box()

        row = box.row()

        row.template_list("ABUTIL_UL_name_slots", "", self, "quick_export_name_collection", self.panel_vars_ptr, "quick_export_name_selection", rows=5)

        col = row.column(align=True)
        col.operator("object.ab_add_remove_quick_export_name", icon='ADD', text="").arg = 'ADD'
        col.operator("object.ab_add_remove_quick_export_name", icon='REMOVE', text="").arg = 'REMOVE'


    def __draw_submenu_buttons(self, parent) -> None:
        box = parent.box()
        box.label(text = "You can render a submenu as buttons in a pie menu by checking these boxes.")
        box.label(text = "The parent of a submenu determines if it's rendered as buttons.")

        box.prop(self, "pie_menu_button_spacing_x")
        box.prop(self, "pie_menu_button_spacing_y")

        row = box.row()
        row.prop(self, "submenu_attributes_buttons")
        row.prop(self, "submenu_cleanup_buttons")
        row.prop(self, "submenu_colors_buttons")
        row = box.row()
        row.prop(self, "submenu_file_buttons")
        row.prop(self, "submenu_modifiers_buttons")
        row.prop(self, "submenu_naming_buttons")
        row = box.row()
        row.prop(self, "submenu_objects_buttons")
        row.prop(self, "submenu_point_cloud_buttons")
        row.prop(self, "submenu_selection_buttons")
        row = box.row()
        row.prop(self, "submenu_uvs_buttons")
        row.prop(self, "submenu_fbx_quick_export_buttons")
        row.label(text = "")

    def __draw_panel_show(self, parent) -> None:
        box = parent.box()
        box.label(text = "You can include menus in a 3D Viewport panel.")

        row = box.row()
        row.prop(self, "panel_attributes_show")
        row.prop(self, "panel_cleanup_show")
        row.prop(self, "panel_colors_show")
        row = box.row()
        row.prop(self, "panel_file_show")
        row.prop(self, "panel_modifiers_show")
        row.prop(self, "panel_naming_show")
        row = box.row()
        row.prop(self, "panel_objects_show")
        row.prop(self, "panel_point_cloud_show")
        row.prop(self, "panel_selection_show")
        row = box.row()
        row.prop(self, "panel_uvs_show")
        row.prop(self, "panel_fbx_quick_export_show")
        row.label(text = "")

    def __draw_submenu_show(self, parent) -> None:
        box = parent.box()
        box.label(text = "You can exclude certain menus from appearing here.")
        box.label(text = "Disabling the \"Attributes\" menu for example will instead render its first submenu")
        box.label(text = " \"Colors\".")

        row = box.row()
        row.prop(self, "submenu_attributes_show")
        row.prop(self, "submenu_cleanup_show")
        row.prop(self, "submenu_colors_show")
        row = box.row()
        row.prop(self, "submenu_file_show")
        row.prop(self, "submenu_modifiers_show")
        row.prop(self, "submenu_naming_show")
        row = box.row()
        row.prop(self, "submenu_objects_show")
        row.prop(self, "submenu_point_cloud_show")
        row.prop(self, "submenu_selection_show")
        row = box.row()
        row.prop(self, "submenu_uvs_show")
        row.prop(self, "submenu_fbx_quick_export_show")
        row.label(text = "")

    def __draw_panels_in_props(self, parent) -> None:
        box = parent.box()
        box.label(text = "Adds panels to the properties panel.")

        row = box.row()
        row.prop(self, "show_color_attribute_utils_in_properties")
        row.prop(self, "show_data_attribute_utils_in_properties")
        row = box.row()
        row.prop(self, "show_object_attribute_utils_in_properties")
        row.prop(self, "show_uv_attribute_utils_in_properties")

    def __draw_advanced(self, parent) -> None:
        split = parent.split()
        box = split.box()

        row_rename_keymaps = box.row()
        box_rename = row_rename_keymaps.box()
        box_rename.label(text = "Batch Rename+")
        col = box_rename.column()
        col.prop(self, "legacy_rename_menu")

        box_keymaps = row_rename_keymaps.box()
        box_keymaps.label(text = "Keymaps")
        row = box_keymaps.row()
        col = row.column()
        col.prop(self, "do_not_load_keymaps")
        col = row.column()
        col.prop(self, "reload_missing_keymaps")

        box_panels = box.box()
        box_panels.label(text = "Panels")
        col = box_panels.column()
        col.prop(self, "load_viewport_panel")


    def __draw_general(self, context, parent) -> None:
        split = parent.split()
        box = split.box()

        # Update UI
        if UPDATE_UI != None:
            UPDATE_UI(self, context, box)

        row = box.row()
        box_properties_panel = row.box()
        box_properties_panel.label(text = "Property Panel")

        box_properties_panel.prop(self, "utilties_in_properties")

        box_alternative_menu = box.box()
        box_alternative_menu.label(text = "Alternative Menu")

        box_alternative_menu.prop(self, "alternative_menu")

        box_menus = box.box()
        box_menus.label(text = "Display Settings")

        row = box_menus.row()
        row.prop(self.panel_vars_ptr, "menu_display_tabs", expand=True)
        
        if self.panel_vars_ptr.menu_display_tabs == 'SUBMENUS':
            self.__draw_submenu_show(box_menus)
        elif self.panel_vars_ptr.menu_display_tabs == 'PANELS':
            self.__draw_panel_show(box_menus)
        elif self.panel_vars_ptr.menu_display_tabs == 'SUBMENU_BUTTONS':
            self.__draw_submenu_buttons(box_menus)
        elif self.panel_vars_ptr.menu_display_tabs == 'PANELS_IN_PROPERTIES':
             self.__draw_panels_in_props(box_menus)
    
                
    def __draw_naming(self, parent) -> None:
        split = parent.split()
        box = split.box()
        
        col = box.column()
        box_actions = col.box()
        box_actions.label(text = "Actions:")
        box_actions.prop(self, "use_a_splitter_between_actions")
        
        box_naming = col.box()
        box_naming.label(text = "Naming:")
        box_naming.prop(self, "name_splitter")

        box_numbering = col.box()
        box_numbering.label(text = "Numbering:")
        box_numbering.prop(self, "auto_numbering")
        row = box_numbering.row()
        row.prop(self, "num_padding")
        row.prop(self, "use_unique_num_splitter")
        if self.use_unique_num_splitter:
            box_numbering.prop(self, "num_splitter")

    def __draw_keymaps(self, parent) -> None:
        split = parent.split()
        box = split.box()

        column = box.column()
        wm = bpy.context.window_manager
        kc = wm.keyconfigs.user
        column.label(text = ab_constants.prefs_keymap_do_not_remove_msg)
        column.label(text = ab_constants.prefs_keymap_disable_msg)
        for km, kmi in ab_keymaps.get_user_keymaps():
            if kmi is not None:
                km = km.active()
                column.context_pointer_set("keymap", km)
                rna_keymap_ui.draw_kmi([], kc, km, kmi, column, 0)

    def __draw_quick_export(self, parent) -> None:
        split = parent.split()
        column = split.column()
        box = column.box()

        box_exporting = box.box()
        box_exporting.label(text = "Paths")
        row = box_exporting.row()
        row.prop(self, "uses_default_export_path")
        row.operator("wm.ab_delete_scene_quick_export_paths")
        if self.uses_default_export_path:
            box_exporting.prop(self, "default_export_path")
        

        box.prop(self, "fbx_exporter_type")
        box = column.box()
        if self.fbx_exporter_type == 'NATIVE':
            box.label(text = "Native FBX Export Preferences")
            box_naming = box.box()
            box_naming.label(text = "Quick Export Name Collection")
            box_naming.label(text = "Include the following objects despite their viewport display type:")
            self.__draw_quick_export_names(box_naming)
            box.prop(self, "native_fbx_ex_scale_options")
            box.prop(self, "native_fbx_ex_mesh_smooth_type")
            box.prop(self, "native_fbx_ex_use_tspace")
            box.prop(self, "native_fbx_ex_use_custom_props")
            row = box.column(align = True)
            row.prop(self, "native_fbx_ex_export_empty", icon = 'EMPTY_ARROWS')
            row.prop(self, "native_fbx_ex_export_camera", icon = 'CAMERA_DATA')
            row.prop(self, "native_fbx_ex_export_light", icon = 'LIGHT')
            row.prop(self, "native_fbx_ex_export_armature", icon = 'ARMATURE_DATA')
            row.prop(self, "native_fbx_ex_export_mesh", icon = 'MESH_DATA')
            row.prop(self, "native_fbx_ex_export_other", icon = 'FILE_3D')
            box.prop(self, "native_fbx_ex_check_existing")
        elif self.fbx_exporter_type == 'CUSTOM':
            box.label(text = "A custom exporter can be implemented inside `operators\\file_ops\\file_ops_custom.py`.")

    @classmethod
    def set_update_ui_function(cls, function : callable) -> None:
        cls.update_ui_function = function
