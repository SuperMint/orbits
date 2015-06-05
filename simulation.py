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
                body.attraction(other)
                total_fx += body.fx
                total_fy += body.fy

            body.fx = total_fx
            body.fy = total_fy

        for body in self.bodies:
            body.update(dt)