bl_info = {
    "name": "Orbit Cam",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
from math import radians
from mathutils import Vector

objects = bpy.data.objects


bpy.ops.object.add(radius=1.0, type='EMPTY', enter_editmode=False, 
    align='CURSOR', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))
bpy.context.active_object.name = 'controller'
bpy.ops.object.camera_add(enter_editmode=False, align='CURSOR', 
    location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))
bpy.context.active_object.name = 'cam'
bpy.context.active_object.rotation_euler = (radians(90.0), 0.0, radians(90.0))
bpy.context.active_object.location = (radians(90.0), 0.0, radians(90.0))
bpy.context.active_object.location = Vector((bpy.data.objects['controller'].location[0] + 10, 0, 0))

print(bpy.context.scene.camera)

bpy.context.scene.camera = bpy.context.active_object # Set the created camera to the Scene (active) Camera

# Make the camera's parent the controller
a = objects['controller']
b = objects['cam']
b.parent = a

#cam.rotation = (radians(-180.0), 0.0, 0.0)

#class ObjectOrbitCam(bpy.types.Operator):
#    """Object Orbit Cam"""
#    bl_idname = "object.orbit_cam"
#    bl_label = "Orbit Cam"
#    bl_options = {'REGISTER', 'UNDO'}

##    total: bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)

#    def execute(self, context):
#        scene = context.scene # Get the current scene
#        cursor = scene.cursor.location # Get the 3D cursor location
#        obj = context.active_object # Get the active object (assume we have one)
#        
#        
#        # Create a plain axes empty that will act as a controller that will be 
#        # placed at the center of the active object
#        
#        # Create a camera, make it a child of the empty, reset it so that it
#        # faces towards the controller, and make it the active camera
#        
#        # Add controls for pitch, roll, yaw for the camera view
#        

##        for i in range(self.total):
##            obj_new = obj.copy()
##            scene.collection.objects.link(obj_new)
##            
##            # Now place the object in between the cursor
##            # and the active object based on 'i'
##            factor = i / self.total
##            # Now we can place the object
##            obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))

#        return {'FINISHED'}


#def menu_func(self, context):
#    self.layout.operator(ObjectOrbitCam.bl_idname)

## store keymaps here to access after registration
#addon_keymaps = []


#def register():
#    bpy.utils.register_class(ObjectOrbitCam)
#    bpy.types.VIEW3D_MT_object.append(menu_func)

#    # handle the keymap
#    wm = bpy.context.window_manager
#    # Note that in background mode (no GUI available), keyconfigs are not available either,
#    # so we have to check this to avoid nasty errors in background case.
#    kc = wm.keyconfigs.addon
#    if kc:
#        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
#        kmi = km.keymap_items.new(ObjectOrbitCam.bl_idname, 'T', 'PRESS', ctrl=True, shift=True)
#        kmi.properties.total = 4
#        addon_keymaps.append((km, kmi))

#def unregister():
#    # Note: when unregistering, it's usually good practice to do it in reverse order you registered.
#    # Can avoid strange issues like keymap still referring to operators already unregistered...
#    # handle the keymap
#    for km, kmi in addon_keymaps:
#        km.keymap_items.remove(kmi)
#    addon_keymaps.clear()

#    bpy.utils.unregister_class(ObjectOrbitCam)
#    bpy.types.VIEW3D_MT_object.remove(menu_func)


#if __name__ == "__main__":
#    register()