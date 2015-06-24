import numpy as np
from vispy import app, gloo


class Canvas(app.Canvas):
    
    def __init__(self):
        app.Canvas.__init__(self, show=True, size=(800, 400))
        
        total = 100 * 1000
        M = 200
        N = int(total / M)
        
        print('Drawing %ix%i points (%ik in total)' % (M, N, total/1000))
        
        self._programs = []
        for i in range(M):
            prog = self.create_program(N, (i/M, (i+1)/M))
            self._programs.append(prog)
        
        self.measure_fps()
    
    def create_data(self, n, range):
        t = np.linspace(0, 1, n).astype('float32')
        X = np.linspace(range[0], range[1], n).astype('float32')
        Y = 0.5 + 0.4 * np.sin(t * 6)
        return X, Y
    
    def create_program(self, n, range):
        
        VERT = """
            attribute float a_x;
            attribute float a_y;
            varying vec2 v_texcoord;
            void main() {
                vec2 pos = vec2(a_x, a_y);
                gl_Position = vec4(pos*2.0-1.0, 0.0, 1.0);
                v_texcoord = pos;
            }"""
        FRAG = """
            uniform vec4 u_color;
            varying vec2 v_texcoord;
            void main() {
                gl_FragColor = u_color;
                gl_FragColor.a = 1.0;
            }"""
        
        X, Y = self.create_data(n, range)
        
        prog = gloo.Program(VERT, FRAG)
        vbox = gloo.VertexBuffer(X)
        vboy = gloo.VertexBuffer(Y)
        prog['a_x'] = vbox
        prog['a_y'] = vboy
        return prog
    
    def on_draw(self, event):
        
        gl = self.context
        
        gl.set_viewport(0, 0, *self.size);
        gl.clear((1, 1, 0, 1));
        gl.set_line_width(2)
        for prog in self._programs:
            prog['u_color'] = 0, 0, 0.5, 1
            prog.draw(gloo.gl.GL_LINE_STRIP)
        self.update()


if __name__ == '__main__':
    c = Canvas()
    app.run()
