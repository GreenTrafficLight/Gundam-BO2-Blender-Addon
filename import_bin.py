import bpy
import bmesh

import os

from math import *
from mathutils import *
from bpy_extras import image_utils

from .Utilities import *
from .Blender import*
from .Resources import *

def build_bin(filename, data):

    bpy.ops.object.add(type="ARMATURE")
    ob = bpy.context.object
    ob.name = str(filename)

    armature = ob.data
    armature.name = str(filename)

    for index, bfmdlnode in enumerate(data.bfmdlnodes):
        pass


    for index, bfmdlmesh in enumerate(data.bfmdlmeshs):

        bfmdlmesh_empty = add_empty(str(index))
        bfmdlmesh_empty.parent = ob

        for i in range(bfmdlmesh.start_index, bfmdlmesh.start_index + bfmdlmesh.submeshs_count):

            mesh = bpy.data.meshes.new(str(index) + "_" + str(i))
            obj = bpy.data.objects.new(str(index) + "_" + str(i), mesh)

            bpy.context.collection.objects.link(obj)

            obj.parent = bfmdlmesh_empty

            vertexList = {}
            facesList = []
            normals = []

            bm = bmesh.new()
            bm.from_mesh(mesh)

            bfmdlsubmesh = data.bfmdlsubmeshs[i]

            last_vertex_count = 0

            for j in range(len(bfmdlsubmesh.vtx.positions)):

                vertex = bm.verts.new(bfmdlsubmesh.vtx.positions[j])
                
                vertex.index = last_vertex_count + j

                vertexList[last_vertex_count + j] = vertex

            # Set faces
            faces = bfmdlsubmesh.vtx.face_indices
            for j in range(0, len(bfmdlsubmesh.vtx.face_indices)):
                try:
                    face = bm.faces.new([vertexList[faces[j][0] + last_vertex_count], vertexList[faces[j][1] + last_vertex_count], vertexList[faces[j][2] + last_vertex_count]])
                    face.smooth = True
                    facesList.append([face, [vertexList[faces[j][0] + last_vertex_count], vertexList[faces[j][1] + last_vertex_count], vertexList[faces[j][2]] + last_vertex_count]])
                except:
                    pass

            if bfmdlsubmesh.vtx.uvs != []:

                uv_name = "UV1Map"
                uv_layer1 = bm.loops.layers.uv.get(uv_name) or bm.loops.layers.uv.new(uv_name)

                for f in bm.faces:
                    for l in f.loops:
                        if l.vert.index >= last_vertex_count:
                            l[uv_layer1].uv = [bfmdlsubmesh.vtx.uvs[l.vert.index - last_vertex_count][0], 1 - bfmdlsubmesh.vtx.uvs[l.vert.index - last_vertex_count][1]]


            # last_vertex_count += len(bfmdlsubmesh.vtx.positions)

            bm.to_mesh(mesh)
            bm.free()

            # Set normals
            mesh.use_auto_smooth = True

            if normals != []:
                try:
                    mesh.normals_split_custom_set_from_vertices(normals)
                except:
                    pass

    ob.rotation_euler = ( radians(90), 0, 0 )


def main(filepath, files, clear_scene):
    if clear_scene:
        clearScene()

    folder = (os.path.dirname(filepath))

    for i, j in enumerate(files):

        path_to_file = (os.path.join(folder, j.name))

        file = open(path_to_file, 'rb')
        filename =  path_to_file.split("\\")[-1]
        file_extension =  os.path.splitext(path_to_file)[1]
        file_size = os.path.getsize(path_to_file)

        br = BinaryReader(file, "<")
        if file_extension == ".bin":
            bfmdlh = BFMDLH()
            bfmdlh.read(br, filepath)
            build_bin(filename, bfmdlh)


    