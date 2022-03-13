Last Error:

Traceback (most recent call last):
  File "D:\Projects\TSI-dev\TSI\FIRST\PSO\main.py", line 10, in <module>
    fit_list, best_pos = swarm.run()
  File "D:\Projects\TSI-dev\TSI\FIRST\PSO\Swarm.py", line 40, in run
    part.update(self.w, self.c1, self.c2, self.G_best)
  File "D:\Projects\TSI-dev\TSI\FIRST\PSO\Particle.py", line 77, in update
    self.__update_velocities(w, c1, c2, G_best)
  File "D:\Projects\TSI-dev\TSI\FIRST\PSO\Particle.py", line 53, in __update_velocities
    if self.max_velocity[i] > self.V_velocities[i] > self.min_velocity[i]:
TypeError: 'float' object is not subscriptable