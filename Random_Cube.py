
import bpy
from random import randint,random

bpy.ops.collection.create(name="CubeXGroup")
 
#group = bpy.data.collection['CubeXGroup']

def main():
    start_pos=(0,0,0)
    for i in range(77):
        add_box(i);
   
def add_box(i):
    #generate our object
    bpy.ops.mesh.primitive_cube_add(location = [ randint(-10,10) for axis in 'xyz'])
    #Select the active object (last added is always the active one
    obj = bpy.context.active_object
    object_random_location_animation(obj,-10,10)
    object_random_color(obj,i)
    obj.select_set(state = True)
    bpy.data.collections["CubeXGroup"].objects.link(obj)

#End AddBox

def object_random_location_animation(obj,min,max):
    positions =  []
    for i in range(0,9):
        positions.append([ randint(min,max) for axis in 'xyz'])
        
    frame_num = 0
    for position in positions:
        bpy.context.scene.frame_set(frame_num)
        obj.location = position
        obj.keyframe_insert(data_path="location",index = -1)
        frame_num +=30
#End object_random_location_animation

def  object_random_color(obj,i):
    material = bpy.data.materials.new(name = "RandomMaterial" + str(i))
    obj.data.materials.append(material)
    bpy.context.object.active_material.diffuse_color = (random(),random(), random(),1)
   # bpy.context.object.active_material.name = "Object Material"
    #inputs[0].default_value = (random(),random(), random(), 1)
    #NOTE: Colours may be very interesting or not so great
    #You can select colours from a list of predefined colours
#End  object_random_color

main(); 