#teacher.py

import mob, pyglet, util, random, viewport
from pyglet.window import key


pyglet.resource.path.append('./images')
pyglet.resource.reindex()

teacher_image=pyglet.resource.image('esher.png')
util.center_image(teacher_image)

class Teacher(mob.Mob):

    def __init__(self,*args,**kwargs):
        super(Teacher,self).__init__(teacher_image, *args,**kwargs)
        self.scale=.65
        self.vel_x=200
        self.is_boss=False
        self.is_enemy=True
        
         
 

        #pyglet.clock.schedule_interval(self.change_velocity,3)
   
    def update(self,dt):

        dx=self.vel_x*dt
        dy=0
        
        super(Teacher,self).update(dx,dy,dt)

    def change_velocity(self,dt):
        if self.x<=self.min_x :
            self.x=self.min_x
            self.vel_x*=-1
        if self.x>=self.max_x:
            self.x=self.max_x
            self.vel_x*=-1

    def check_bounds(self):  

        if self.x<=self.min_x :
            self.x=self.min_x
            self.vel_x*=-1
        if self.x>=self.max_x:
            self.x=self.max_x
            self.vel_x*=-1

    def handle_collision_with(self,other):
        pass


   
