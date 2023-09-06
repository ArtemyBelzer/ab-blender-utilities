# Artemy Belzer's Blender Utilities
### A plugin with additional utilities for speeding up workflow in Blender.
## Feature Overview
* Bulk asset quick export to an intermediate directory.
* Usage of directories in object names for quick exporting.
* Export/Import a point cloud of selected assets in a .JSON format for other applications.
* Cache object modifiers: create a non-evaluating copy of an object for quick previews.
* Bulk UV utilities: Add, delete, rename, and set active functionality on multiple objects.
* Bulk Color Attribute/Vertex Color utilities: Delete, remove, rename, set to render, set active.
* Select all objects referenced in modifiers.
* Remove unused materials on selected objects.
* Clean up unused data blocks (Global Cleanup).
* Reorder object data blocks alphabetically.
* Reorder modifier object data blocks to the modifier order.
* Store/Save the currently selected objects in Blender.
* Select all child objects recursively from the current parent.
* Randomize attributes on selected objects.
* Store the current object rotation as an attribute for retrieval later.
* Set attributes on selected objects.
* Append boolean operation to the name of boolean objects.
* Auto/Advanced rename with syntax and numbering conventions.
* Find and replace object names.
* Object names from parent.
* Set mesh data name from object name.
* Dynamically filled operator menu.

## Guide
### Accessing the main menu.
![AB_Blender_Utilities_Pie_Menu_v2](https://github.com/ArtemyBelzer/AB-Blender-Utilities/assets/143417950/1e80f22e-d4cf-420f-b9c5-c86cb48bbd5b)

There are two ways to access the list of operators in the plugin.
By pressing Alt+E (default key binding).
By pressing right-click and navigating to the "Extra Utilities" submenu.
Go into the "Object" menu in the 3D viewport and navigate to the "Extra Utilities" submenu.

### Alternative Menu layouts & Customization
Users can exclude specific categories from appearing in the plugin's "Quick Menu" (Alt+E). Submenu inclusion/exclusion can be found under the "General" tab in the plugin's properties; an alternative menu layout, a feature to draw operator menus as buttons, and a feature that adds certain utilities to the properties panel are also available.

![AB_Blender_Utilities_Alternative_Menu](https://github.com/ArtemyBelzer/AB-Blender-Utilities/assets/143417950/2df8adb4-52ce-4d3f-942f-8c8136a3d300)

![AB_Blender_Utilities_Menu_Customization](https://github.com/ArtemyBelzer/AB-Blender-Utilities/assets/143417950/346159ec-5c27-49bb-af45-4a7d2113ea40)

### Rebinding keys
![AB_Blender_Utilities_Preferences_Keymaps_Tab](https://github.com/ArtemyBelzer/AB-Blender-Utilities/assets/143417950/02b4e24d-4806-4ece-89e0-1ebb74bc18f2)
You can rebind keys inside Blender preferences by navigating to the plugin in the Add-ons tab. You can rebind the main menu, auto/advanced rename functionality, and the naming pie menu. If you would like to turn off the functioning of these keymaps, please uncheck the box on the left.

### Bulk Asset export
![AB_Blender_Utilities_Quick_Export](https://github.com/ArtemyBelzer/Artemy-Belzers-Blender-Utilities/assets/143417950/f51879e4-5c32-4a20-b7a7-e7ed898d0e77)

The user can select multiple assets in the scene and export them individually. This action also exports child assets. By default, the quick export action ignores assets rendered as a wireframe (viewport display as 'Wire'). You can export multiple selected assets or the currently active asset in the scene. The user can use directories in object names. During export, the quick export operators remove directories from the actual object name + data name.

#### Intermediate directory
To quickly export assets, you need an intermediate directory. To set an intermediate directory, set it by activating the "("Extra Utilities" or the Main Menu)/File/Set quick export path" operator.

Alternatively, the user can set a global, project-independent quick export directory in the "General" tab of the plugin preferences by checking "Use default export path".


Suppose the user wishes to remove any references to an intermediate directory in the project. In that case, the user can click the "Delete quick export attributes from scenes" in the "General" tab of the plugin preferences.

#### Quick Export Settings

The user can customize how the asset gets exported under the "Quick Export" tab of the plugin preferences. The user can pick the native FBX exporter or a custom implementation in the "Exporter Type" dropdown.

#### Quick Export Name Collection

The "Quick Export Name Collection" feature allows the user to export wired objects that begin, end, or have an occurrence of a string in their name. This name collection feature can be helpful when exporting collision objects with a mesh without having to tick "Export Wired" for quick exports. The "Quick Export Name Collection" feature is under the "Quick Export" tab in the addon properties.

### Auto/Advanced Renaming
![AB_Blender_Utilities_Preferences_Naming_Tab_v1 1 0](https://github.com/ArtemyBelzer/AB-Blender-Utilities/assets/143417950/706b1a21-0456-4041-ae09-80352360d325)

Users can set naming splitters and zero padding count under the plugin's "Naming" tab.

![AB_Blender_Utilities_Auto_Advanced_Rename](https://github.com/ArtemyBelzer/Artemy-Belzers-Blender-Utilities/assets/143417950/8c4ce9ac-6a94-47c7-b074-807e9d102261)

The auto-renaming utility is context and argument-based. The naming utility will rename your assets depending on the objects selected. When no argument is present, and multiple objects are selected, the operator renames the assets to "<New Name><Splitter><Count>". i.e. The third selected object in a selection of five after renaming will be "NewObjectName_03".
#### Arguments
The user can supply arguments to the naming utility.
"$name"
"$name" references the current name of the object.
"$type"
"$type" returns the internal object type of an object. You can combine this with "$replace" to replace object types of Blender into some other naming convention. i.e. To rename "MESH" to "SM," use "$replace("MESH", "SM")".
"$active"
"$active" returns the name of the currently active object in the scene.
"$index"
"$index" returns the index of the currently selected object.
"$no_index"
"$no_index" prevents the automatic addition of context-based numbering when renaming multiple objects.
"$replace(str_old, str_new)"
"$replace(str_old, str_new)" finds all occurrences of the first argument and replaces them with the second one.

Usage example:
`$type$replace("MESH", "SM")_Cube`

![AB_Blender_Utilities_Auto_Advanced_Rename_Example](https://github.com/ArtemyBelzer/Artemy-Belzers-Blender-Utilities/assets/143417950/42a6cf37-e531-421e-83f1-baf1dbdb40ec)


## Bulk Attribute/Color/UV Operations
The plugin offers functionality to perform essential bulk attribute, colour, and UV operations on multiple objects. You can set the currently active UV map, rename a colour attribute on various objects, etc.

If the "Deselect Invalid" checkbox is present, the operator will deselect objects that do not contain the attribute post-operation.
![AB_Blender_Utilities_Delete_UV_Channel](https://github.com/ArtemyBelzer/Artemy-Belzers-Blender-Utilities/assets/143417950/184cd50e-5f3c-4233-a53c-206d569bfd96)

![AB_Blender_Utilities_Rename_UV_Channel](https://github.com/ArtemyBelzer/Artemy-Belzers-Blender-Utilities/assets/143417950/2ed05bb0-7acd-469b-ab28-4992690fb127)

![AB_Blender_Utilities_Set_Active_UV_Channel](https://github.com/ArtemyBelzer/Artemy-Belzers-Blender-Utilities/assets/143417950/67a9477a-9477-4192-b663-d7a343cca7af)



##  Clean up unused data blocks (Global Cleanup).
The "Global Cleanup" operator, under the "Cleanup" submenu, removes unused data blocks inside the current project file. The operator will delete any stored meshes/materials/textures/images with no references in the current project.
