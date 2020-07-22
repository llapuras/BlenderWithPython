import bpy
import math as m

n=80
r=4
z=0

# delete everything in the scene
def clear_scene():
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)


clear_scene()

for i in range(1,n+1):
    angle=((i-1)*4*m.pi)/n
    x=r*m.cos(angle)
    y=r*m.sin(angle)
    bpy.ops.mesh.primitive_cube_add(location=(x,y,z))
    bpy.ops.transform.resize(value=(2,1,0.2))
    bpy.ops.transform.rotate(value=angle)
    z+=0.4
    
a=z/2
bpy.ops.mesh.primitive_cylinder_add(radius=r-1, depth=z, location=(0,0,a))
