from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0.0, exposure=10)
scene.set_floor(-1.0, (1.0, 1.0, 1.0))
scene.set_background_color((1.0, 1.0, 1.0))
scene.set_direction_light((1, 1, 1), 0.1, (0.2, 0.2, 0.2))

@ti.kernel
def initialize_voxels():
    a = 3;b = 2.7;c = 1.7;d = 2;e = 9;x = 0.1;y = 0.1;z = 0.1;dt = 0.001
    ti.loop_config(serialize=True)
    for i in range(50000):
        nx = (y- a*x +b*y*z);ny = (c*y -x*z +z);nz = (d*x*y - e*z);x += nx * dt;y += ny * dt;z += nz * dt
        scene.set_voxel(vec3(x, z, y)*3.5, 1, vec3(0.9, 0.3, 0.3))

initialize_voxels()
scene.finish()
