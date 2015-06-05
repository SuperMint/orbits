import math

from body import Body
from simulation import Simulation
from renderer import Renderer

##################
# Simulation setup
AU = (149.6e6 * 1000)  # 149.6 million km, in meters.
timestep = 24*3600

sim = Simulation()

sun = Body('Sun')
sun.mass = 1.98892e30
sim.add_body(sun)

mercury = Body('Mercury')
mercury.mass = 3.3e23
mercury.x = 0.387 * AU
mercury.vy = 47362
sim.add_body(mercury)

venus = Body('Venus')
venus.mass = 4.8685e24
venus.x = 0.723 * AU
venus.vy = 35020
sim.add_body(venus)

earth = Body('Earth')
earth.mass = 5.9742e24
earth.x = AU
earth.vy = 29783
sim.add_body(earth)

mars = Body('Mars')
mars.mass = 6.42e23
mars.x = 1.52 * AU
mars.vy = 24077
sim.add_body(mars)

#################
# Rendering setup
interface = Renderer(sim, AU, 800, 600)

sun.material['emission'] = [1.0, 0.7, 0.0, 1.0]
sun.radius = 0.05

mercury.material['diffuse'] = [0.65, 0.65, 0.65, 1.0]
mercury.material['ambient'] = [0.8, 0.8, 0.8, 1.0]
mercury.radius = 0.01915

venus.material['diffuse'] = [0.72, 0.64, 0.44, 1.0]
venus.material['ambient'] = [0.72, 0.64, 0.44, 1.0]
venus.radius = 0.0475

earth.material['diffuse'] = [70/255, 120/255, 200/255, 1.0]
earth.material['ambient'] = [70/255, 120/255, 200/255, 1.0]
earth.radius = 0.05

mars.material['diffuse'] = [216/255, 109/255, 47/255, 1.0]
mars.material['ambient'] = [216/255, 109/255, 47/255, 1.0]
mars.radius = 0.0266

##############
# Program loop
while True:
    sim.tick(timestep)
    print('##############################################################')
    for body in sim.bodies:
        print('{}\tx: {:7.3f}  y: {:7.3f}  vx: {:10.3f}  vy: {:10.3f}'
              .format(body.name, body.x / AU, body.y / AU, body.vx, body.vy))
        print('\tvelocity: {:8.3f} km/s  distance from sun: {:5.3f} AU'
              .format(math.sqrt(body.vx**2 + body.vy**2),
                      math.sqrt(body.x**2 + body.y**2) / AU))
        # render stuff here
        interface.render()
