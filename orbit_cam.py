bl_info = {
    "name": "Orbit Cam",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
from math import radians
from mathutils import Vector

# Delete a specific object if it exists by name
def delete_obj_by_name(name):
    bpy.ops.object.select_all(action='DESELECT')
    print(type(bpy.data.objects))
    if name in bpy.data.objects.keys():
        bpy.data.objects[name].select_set(True)
    bpy.ops.object.delete()

# parent an object
def parent_obj(parent, child):
    a = parent
    b = child
    child.parent = a
    


objects = bpy.data.objects
collections = bpy.data.collections

print(collections)

bpy.ops.collection.create(name='orbit-cam') # Create a collection for the cameras
bpy.context.scene.collection.children.link(bpy.data.collections['orbit-cam'])

bpy.ops.object.add(radius=1.0, type='EMPTY', enter_editmode=False, align='CURSOR', 
    location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))
bpy.context.active_object.name = 'controller'
bpy.data.collections['orbit-cam'].objects.link(bpy.context.active_object)

## print all objects
#for obj in bpy.data.objects:
#    print(obj.name)

bpy.data.objects['controller'].scale = (1, 1, 1)
bpy.ops.object.camera_add(enter_editmode=False, align='CURSOR', 
    location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))
bpy.context.active_object.name = 'cam'
bpy.context.active_object.rotation_euler = (radians(90.0), 0.0, radians(90.0))
bpy.context.active_object.location = (radians(90.0), 0.0, radians(90.0))
bpy.context.active_object.location = Vector((bpy.data.objects['controller'].location[0] + 10, 0, 0))

print(bpy.context.scene.camera)
print(type(bpy.context.active_object))
bpy.context.scene.camera = bpy.context.active_object # Set the created camera to the Scene (active) Camera

## Make the camera's parent the controller
#a = objects['controller']
#b = objects['cam']
#b.parent = a

parent_obj(objects['controller'], objects['cam'])

#default_cube = bpy.data.objects['Cube']
## X, Y, and Z location to set
#default_cube.location = (0.0, 0.0, 0.0)
## Set the keyframe with that location, and which frame.
#default_cube.keyframe_insert(data_path="location", frame=1)

## do it again!
#default_cube.location = (3.0, 2.0, 1.0)
## setting it for frame 10
#default_cube.keyframe_insert(data_path="location", frame=10)


#bpy.ops.mesh.primitive_monkey_add()
#bpy.context.active_object.name = 'monkey'
#monkey = bpy.data.objects['monkey']
#print(type(monkey))
## X, Y, and Z location to set
#monkey.rotation_euler = (0.0, 0.0, 0.0)
## Set the keyframe with that location, and which frame.
#monkey.keyframe_insert(data_path="rotation_euler", frame=1)

## do it again!
#monkey.rotation_euler = (0.0, 0.0, radians(180.0))
## setting it for frame 10
#monkey.keyframe_insert(data_path="rotation_euler", frame=15)

#monkey.rotation_euler = (0.0, 0.0, radians(360.0))
## setting it for frame 10 
#monkey.keyframe_insert(data_path="rotation_euler", frame=30)

controller = bpy.data.objects['controller']
controller.rotation_euler = (0.0, 0.0, 0.0)
controller.keyframe_insert(data_path="rotation_euler", frame=1)
controller.rotation_euler = (0.0, 0.0, radians(180.0))
controller.keyframe_insert(data_path="rotation_euler", frame=15)
controller.rotation_euler = (0.0, 0.0, radians(360.0))
controller.keyframe_insert(data_path="rotation_euler", frame=30)

obj = controller
fcurves = obj.animation_data.action.fcurves
for fcurve in fcurves:
    for kf in fcurve.keyframe_points:
        kf.interpolation = 'LINEAR'

bpy.ops.object.select_all(action='DESELECT')
print(type(bpy.data.objects))
if 'Cube' in bpy.data.objects.keys():
    bpy.data.objects['Cube'].select_set(True)
bpy.ops.object.delete()

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