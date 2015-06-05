import math
from OpenGL.GL import *
from OpenGL.GLUT import *

G = 6.67384e-11
AU = 149.6e9


class Body(object):

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.mass = 0
        self.vx = 0
        self.vy = 0
        self.f = 0
        self.fx = 0
        self.fy = 0

        self.material = {'diffuse': [0.0, 0.0, 0.0, 1.0],
                         'emission': [0.0, 0.0, 0.0, 1.0],
                         'ambient': [0.0, 0.0, 0.0, 1.0]}
        self.radius = 0.05

    def attraction(self, other):
        if other is self:
            raise ValueError(self.name +
                             ": Can't calculate attraction to self")

        dx = other.x - self.x
        dy = other.y - self.y
        d = math.sqrt(dx**2 + dy**2)

        if d == 0:
            raise ValueError(self.name + " intersects with " + other.name)

        self.f = G * self.mass * other.mass / (d**2)
        force_dir = math.atan2(dy, dx)
        self.fx = math.cos(force_dir) * self.f
        self.fy = math.sin(force_dir) * self.f

    def update(self, dt):
        self.vx += self.fx / self.mass * dt
        self.vy += self.fy / self.mass * dt

        self.x += self.vx * dt
        self.y += self.vy * dt

    def render(self):
        glTranslatef(self.x / AU, 0.0, self.y / AU)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.material['diffuse'])
        glMaterialfv(GL_FRONT, GL_EMISSION, self.material['emission'])
        glMaterialfv(GL_FRONT, GL_AMBIENT, self.material['ambient'])
        glutSolidSphere(self.radius, 30, 30)
