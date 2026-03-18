import glfw
from OpenGL.GL import *


def setup() -> None:
    glClearColor(1, 1, 1, 1)


def render() -> None:
    glClear(GL_COLOR_BUFFER_BIT)


def app() -> None:
    glfw.init()
    window = glfw.create_window(
        700,
        500,
        'Primeiro Teste de Computação Gráfica',
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


if __name__ == '__main__':
    app()
