import bpy
import random

verts = []
faces = []

amp = 1
scale = 1

numX = 10
numY = 10

for i in range (0, numX):
    for j in range (0, numY):
        x = scale * i
        y = scale * j
        z = random.random()*amp*i
        
        vert = (x,y,z)
        verts.append(vert)

count = 0
for i in range (0, numY * (numX -1)):
    if count < numY-1:
        a = i
        b = i +1
        c = (i+numY)+1
        d = (i+numY)
        
        face = (a,b,c,d)
        faces.append(face)
        count = count + 1
    else:
        count = 0

#create mesh and object
mesh = bpy.data.meshes.new("randomwave")
object = bpy.data.objects.new("randomwave",mesh)
 
#set mesh location
object.location = [0,0,0]
bpy.context.scene.collection.objects.link(object) 
 
#create mesh from python data
mesh.from_pydata(verts,[],faces)
mesh.update(calc_edges=True)