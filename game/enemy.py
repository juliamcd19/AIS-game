#enemy.py

import mob, pyglet, util, random, viewport
from pyglet.window import key


pyglet.resource.path.append('./images')
pyglet.resource.reindex()

enemy_image=pyglet.resource.image('w_critter.png')
util.center_image(enemy_image)

class Enemy(mob.Mob):

    def __init__(self,*args,**kwargs):
        super(Enemy,self).__init__(enemy_image,*args,**kwargs)
        self.scale=0.15
        self.spd=200
        self.x=0
        self.y=0
        self.is_enemy=True
        
        self.vel_x=random.random()*self.spd
        if random.randint(0,1):self.vel_x*=-1
        self.vel_y=random.random()*self.spd
        if random.randint(0,1):self.vel_y*=-1

        pyglet.clock.schedule_interval(self.change_velocity,3)
   
    def update(self,dt):

        dx=self.vel_x*dt
        dy=self.vel_y*dt
        
        
        if self.affected_by_gravity:
            if not self.supported:
                self.vel_y-=self.acc*dt
                dy=self.vel_y*dt

        
        super(Enemy,self).update(dx,dy,dt)

    def change_velocity(self,dt):

        self.vel_x=random.random()*self.spd
        if random.randint(0,1):self.vel_x*=-1
        self.vel_y=random.random()*self.spd
        if random.randint(0,1):self.vel_y*=-1

    def check_bounds(self):
 
        min_x=self.width//2
        max_x=viewport.window.width-(self.width//2)
        min_y=self.height//2
        max_y=viewport.window.height-(self.height//2)

        if self.x<=min_x or \
           self.x>=max_x: self.vel_x*=-1
        if self.y<=min_y or \
           self.y>=max_y: self.vel_y*=-1

    def handle_collision_with(self,other):
        pass


   
