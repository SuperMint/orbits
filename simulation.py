import math
AU = 149.6e9

class Simulation(object):

    def __init__(self):
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def tick(self, dt):
        for body in self.bodies:
            total_fx = 0
            total_fy = 0

            for other in self.bodies:
                if other is body:
                    continue
                #Check if there are collisions and calculate velocity, mass and radius thereafter (inelastic collisions)
                elif (math.sqrt((body.x-other.x)**2 + (body.y-other.y)**2)/AU<0.1 ):
                    body.vx= (body.mass*body.vx + other.mass*other.vx)/(body.mass+other.mass)
                    body.vy= (body.mass*body.vy + other.mass*other.vy)/(body.mass+other.mass)
                    body.mass=body.mass+other.mass
                    body.radius=body.radius+other.radius
                    self.bodies.remove(other)
                else:
                    body.attraction(other)
                    total_fx += body.fx
                    total_fy += body.fy




            body.fx = total_fx
            body.fy = total_fy

        for body in self.bodies:
            body.update(dt)
