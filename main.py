import glfw
from OpenGL.GL import *
import numpy as np
import pyrr

from src.primitives.circle import create_circle
from src.core.shader import Shader
from src.scene.orbit_body import OrbitBody


shader = None
planet = None
vertices = None
vao = 0
vbo = 0


def setup():
    global vao, vbo, shader, planet, vertices
    glClearColor(0.1, 0.1, 0.1, 1)

    shader = Shader(
        "src/shaders/circle/vertex_shader.glsl",
        "src/shaders/circle/fragment_shader.glsl"
    )
    planet = OrbitBody(distance=0.7, size=0.08, speed=1.0)
    vertices = create_circle()
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)

    glBindVertexArray(vao)

    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(0)


def render():
    glClear(GL_COLOR_BUFFER_BIT)
    shader.use()

    model_loc = glGetUniformLocation(shader.program, 'model')
    proj_loc = glGetUniformLocation(shader.program, "projection")
    color_loc = glGetUniformLocation(shader.program, "color")

    star_scale = pyrr.matrix44.create_from_scale([0.2, 0.2, 1])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, star_scale)
    glUniform3f(color_loc, 1.0, 0.9, 0.2)
    glDrawArrays(GL_TRIANGLE_FAN, 0, len(vertices)//3)

    planet.update(0.01)
    model, projection = planet.matrix()

    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
    glUniform3f(color_loc, 0.2, 0.6, 1.0)
    glDrawArrays(GL_TRIANGLE_FAN, 0, len(vertices)//3)


def main():
    glfw.init()
    window = glfw.create_window(
        800,
        600,
        "Primeiro Teste de Computação Gráfica",
        None,
        None
    )
    glfw.make_context_current(window)
    setup()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)
    glfw.terminate()


if __name__ == "__main__":
    main()
