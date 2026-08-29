import moderngl_window as mglw
import numpy as np


class GraphicsDemo(mglw.WindowConfig):
    gl_version = (3, 3)
    title = "ModernGL Triangle Demo"
    window_size = (800, 600)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.prog = self.ctx.program(
            vertex_shader='''
                #version 330
                in vec2 in_vert;
                in vec3 in_color;
                out vec3 v_color;
                void main() {
                    gl_Position = vec4(in_vert, 0.0, 1.0);
                    v_color = in_color;
                }
            ''',
            fragment_shader='''
                #version 330
                in vec3 v_color;
                out vec4 f_color;
                uniform float time;
                void main() {
                    // Animate color channels using sine/cosine of elapsed time
                    f_color = vec4(v_color.r * sin(time), v_color.g, v_color.b * cos(time), 1.0);
                }
            '''
        )

        # Three vertices, each with a 2D position (x, y) and an RGB color
        vertices = np.array([
            0.0,  0.8,   1.0, 0.0, 0.0,
           -0.8, -0.8,   0.0, 1.0, 0.0,
            0.8, -0.8,   0.0, 0.0, 1.0,
        ], dtype='f4')

        self.vbo = self.ctx.buffer(vertices)
        self.vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert', 'in_color')

    def render(self, time, frame_time):
        # Note: moderngl_window calls this method "render", not "on_render" —
        # using the wrong name means the frame is never drawn.
        self.ctx.clear(0.1, 0.1, 0.1)

        if 'time' in self.prog:
            self.prog['time'].value = time

        self.vao.render()


if __name__ == '__main__':
    mglw.run_window_config(GraphicsDemo)
