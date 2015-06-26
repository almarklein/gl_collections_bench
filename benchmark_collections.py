import numpy as np
from vispy import app, gloo


class BaseCanvas(app.Canvas):
    
    def __init__(self):
        app.Canvas.__init__(self, show=True, size=(800, 400))
        
        total = 100 * 1000
        M = 100
        N = int(total / M)
        
        print('Drawing %ix%i points (%ik in total)' % (M, N, total/1000))
        self._init(N, M)
        self.measure_fps()
    
    def create_data(self, n, range):
        t = np.linspace(0, 1, n).astype('float32')
        X = np.linspace(range[0], range[1], n).astype('float32')
        Y = 0.5 + 0.4 * np.sin(t * 6)
        return X, Y
    
    def create_program(self):
        
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
        
        return gloo.Program(VERT, FRAG)
        
    def create_vbos(self, n, range):
        X, Y = self.create_data(n, range)
        
        vbox = gloo.VertexBuffer(X)
        vboy = gloo.VertexBuffer(Y)
        return vbox, vboy
    
    def create_program2(self):
        # More complex shader, trying to strain the GPU, what I did does not seem to help
        VERT = """
            attribute float a_x;
            attribute float a_y;
            varying vec2 v_pos;
            void main() {
                vec2 pos = vec2(a_x, a_y);
                v_pos = pos;
                gl_Position = vec4(pos*2.0-1.0, 0.0, 1.0);
                gl_PointSize = 40.0;
            }"""
        FRAG = """
            uniform vec4 u_color;
            uniform sampler2D texture;
            varying vec2 v_pos;
            void main() {
                float x = 2.0*gl_PointCoord.x - 1.0;
                float y = 2.0*gl_PointCoord.y - 1.0;
                float a = 1.0 - (x*x + y*y);
                for (int i=0; i< 20; i++) {
                    a *= texture2D(texture, v_pos) + texture2D(texture, pow(v_pos, vec2(i)));
                }
                gl_FragColor = vec4(u_color.rgb, a*u_color.a);
            }"""
        
        tex = np.random.normal(0, 1, (100, 100)).astype('float32')
        
        prog = gloo.Program(VERT, FRAG)
        prog['texture'] = tex
        return prog
    
    def on_draw(self, event):
        
        gl = self.context
        
        gl.set_viewport(0, 0, *self.size);
        gl.clear((1, 1, 0, 1));
        gl.set_line_width(2)
        self._draw()
        self.update()


class CanvasMultiProgram(BaseCanvas):
    def _init(self, N, M):
        self._programs = []
        for i in range(M):
            prog = self.create_program()
            vbox, vboy = self.create_vbos(N, (i/M, (i+1)/M))
            prog['a_x'] = vbox
            prog['a_y'] = vboy
            self._programs.append(prog)
    
    def _draw(self):
        for prog in self._programs:
            prog['u_color'] = 0, 0, 0.5, 1
            prog.draw(gloo.gl.GL_LINE_STRIP)


class CanvasMultiBuffer(BaseCanvas):
    def _init(self, N, M):
        self._buffers = []
        self._prog = self.create_program()
        for i in range(M):
            self._buffers.append(self.create_vbos(N, (i/M, (i+1)/M)))
    
    def _draw(self):
        prog = self._prog
        for vbox, vboy in self._buffers:
            prog['u_color'] = 0, 0, 0.5, 1
            prog['a_x'] = vbox
            prog['a_y'] = vboy
            prog.draw(gloo.gl.GL_LINE_STRIP)


class CanvasHeavy(BaseCanvas):
    def _init(self, N, M):
        self._buffers = []
        self._prog = self.create_program2()
        for i in range(M):
            self._buffers.append(self.create_vbos(N, (i/M, (i+1)/M)))
    
    def _draw(self):
        prog = self._prog
        for vbox, vboy in self._buffers:
            prog['u_color'] = 0, 0, 0.5, 1
            prog['a_x'] = vbox
            prog['a_y'] = vboy
            prog.draw(gloo.gl.GL_POINTS)


if __name__ == '__main__':
    c = CanvasMultiBuffer()
    app.run()
