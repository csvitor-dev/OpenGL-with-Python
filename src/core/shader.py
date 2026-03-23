from OpenGL.GL import *
import OpenGL.GL.shaders as gls
from utils.filesystem import read_file


class Shader:
    def __init__(self, scope: str):
        vertex_src = read_file(self.__path(scope, 'vertex'))
        fragment_src = read_file(self.__path(scope, 'fragment'))

        vs = gls.compileShader(vertex_src, GL_VERTEX_SHADER)
        fs = gls.compileShader(fragment_src, GL_FRAGMENT_SHADER)
        program = gls.compileProgram(vs, fs)
        glDeleteShader(vs)
        glDeleteShader(fs)

        self.program = program

    def __path(self, scope: str, type: str) -> str:
        return f'src/shaders/{scope}/{type}_shader.glsl'

    def use(self):
        glUseProgram(self.program)
