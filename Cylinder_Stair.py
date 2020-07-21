import bpy
import math as m

n=80
r=4
z=0

for i in range(1,n+1):
    angle=((i-1)*4*m.pi)/n
    x=r*m.cos(angle)
    y=r*m.sin(angle)
    bpy.ops.mesh.primitive_cube_add(location=(x,y,z))
    bpy.ops.transform.resize(value=(2,1,0.2))
    z+=0.4
    
a=z/2
bpy.ops.mesh.primitive_cylinder_add(radius=r-1, depth=z, location=(0,0,a))
