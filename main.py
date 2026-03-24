import glfw
from OpenGL.GL import *
import numpy as np
import pyrr

from src.primitives.circle import Circle
from src.core.shader import Shader
from src.scene.orbit_body import OrbitBody


def framebuffer_size_callback(window, width, height):
    glViewport(0, 0, width, height)


def setup() -> dict:
    glClearColor(0.1, 0.1, 0.1, 1)

    shader = Shader('circle')
    planet = OrbitBody(distance=0.7, size=0.08, speed=1.0)
    circle = Circle()
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)

    glBindVertexArray(vao)

    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, circle.vertices.nbytes,
                 circle.vertices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(0)

    return {
        'vao': vao,
        'vbo': vbo,
        'shader': shader,
        'planet': planet,
        'circle': circle,
    }


def render(context: dict):
    glClear(GL_COLOR_BUFFER_BIT)
    context['shader'].use()

    model_loc = glGetUniformLocation(context['shader'].program, 'model')
    proj_loc = glGetUniformLocation(context['shader'].program, 'projection')
    color_loc = glGetUniformLocation(context['shader'].program, 'color')

    star_scale = pyrr.matrix44.create_from_scale([0.2, 0.2, 1])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, star_scale)
    glUniform3f(color_loc, 1.0, 0.9, 0.2)
    glDrawArrays(GL_TRIANGLE_FAN, 0, len(context['circle'].vertices)//3)

    context['planet'].update(0.01)
    model, projection = context['planet'].matrix()

    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
    glUniform3f(color_loc, 0.2, 0.6, 1.0)
    glDrawArrays(GL_TRIANGLE_FAN, 0, len(context['circle'].vertices)//3)


def main():
    glfw.init()
    window = glfw.create_window(
        800,
        600,
        "Primeiro Teste de Computação Gráfica",
        None,
        None
    )
    width, height = glfw.get_framebuffer_size(window)
    glfw.make_context_current(window)
    glViewport(0, 0, width, height)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)

    context = setup()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render(context)
        glfw.swap_buffers(window)
    glfw.terminate()


if __name__ == "__main__":
    main()
