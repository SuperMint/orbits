from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Renderer(object):

    def __init__(self, simulation, scale, width, height):
        self.sim = simulation
        self.scale = scale
        self.window = 0

        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(width, height)
        self.window = glutCreateWindow('Orbit Renderer')

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, (width / height), 0.001, 50.0)
        glMatrixMode(GL_MODELVIEW)
        gluLookAt(0, 2.5, 2.5,
                  0, 0, 0,
                  0, 1, 0)
        glPushMatrix()

        light_position = [0.0, 0.0, 0.0, 1.0]
        light_colour = [1.0, 1.0, 1.0, 1.0]
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_colour)
        glLightfv(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.5)
        glLightfv(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.2)
        glEnable(GL_LIGHT0)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMaterialfv(GL_FRONT, GL_EMISSION, [0.0, 0.0, 0.0, 1])
        glMaterialfv(GL_FRONT, GL_AMBIENT, [0.0, 0.0, 0.0, 1])
        glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0, 0.0, 0.0, 1])

        # Draw reference grid
        gridsize = 100
        blocksize = 0.25
        glMaterialfv(GL_FRONT, GL_EMISSION, [0.1, 0.1, 0.1, 1])
        glBegin(GL_LINES)
        for i in range(-gridsize, gridsize):
            glVertex3f(-gridsize / 10, 0.0, i * blocksize)
            glVertex3f(gridsize / 10, 0.0, i * blocksize)
        for i in range(-gridsize, gridsize):
            glVertex3f(i * blocksize, 0.0, -gridsize)
            glVertex3f(i * blocksize, 0.0, gridsize)
        glEnd()

        # Draw bodies
        for body in self.sim.bodies:
            glPushMatrix()
            body.render()
            glPopMatrix()

        glutSwapBuffers()
