import bpy

save_to_file = '/home/dot/Scrivania/file.txt'

vertices = [(vert.co.x, vert.co.y, vert.co.z) for vert in bpy.context.object.data.vertices]

faces = [[vert for vert in polygon.vertices] for polygon in bpy.context.object.data.polygons]

with open(save_to_file, 'w') as file:
    file.write('verts = ' + str(vertices) + '\n' + 'faces = ' + str(faces) + '\n')
    file.close() 
