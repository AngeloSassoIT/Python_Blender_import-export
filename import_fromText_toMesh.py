verts = [
        (-1.0, -1.0, -1.0), (-1.0, -1.0, 1.0), (-1.0, 1.0, -1.0),
        (-1.0, 1.0, 1.0), (1.0, -1.0, -1.0), (1.0, -1.0, 1.0),
        (1.0, 1.0, -1.0), (1.0, 1.0, 1.0)
    ]
faces = [
        [0, 1, 3, 2], [2, 3, 7, 6], [6, 7, 5, 4],
        [4, 5, 1, 0], [2, 6, 4, 0], [7, 3, 1, 5]
    ]
    
import bpy
mesh_data = bpy.data.meshes.new("new_mesh")
mesh_data.from_pydata(verts, [], faces)
mesh_data.update()
mesh = bpy.data.objects.new("new_mesh", mesh_data)
bpy.context.scene.collection.objects.link(mesh)
