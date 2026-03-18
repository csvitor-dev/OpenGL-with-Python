from OpenGL.GL import *
from utils.filesystem import read_file


class Shader:
    def __init__(self, vertex_path, fragment_path):
        vertex_src = read_file(vertex_path)
        fragment_src = read_file(fragment_path)

        program = glCreateProgram()

        vs = self._compile(vertex_src, GL_VERTEX_SHADER)
        fs = self._compile(fragment_src, GL_FRAGMENT_SHADER)

        glAttachShader(program, vs)
        glAttachShader(program, fs)
        glLinkProgram(program)

        if not glGetProgramiv(program, GL_LINK_STATUS):
            raise RuntimeError(glGetProgramInfoLog(program))
        glDeleteShader(vs)
        glDeleteShader(fs)

        self.program = program

    def _compile(self, source, shader_type):
        shader = glCreateShader(shader_type)

        glShaderSource(shader, source)
        glCompileShader(shader)

        if not glGetShaderiv(shader, GL_COMPILE_STATUS):
            raise RuntimeError(glGetShaderInfoLog(shader))
        return shader

    def use(self):
        glUseProgram(self.program)
