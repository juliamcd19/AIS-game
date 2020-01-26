#car_enemy.py

import mob, pyglet, util, random, viewport,enemy
from pyglet.window import key


pyglet.resource.path.append('./images')
pyglet.resource.reindex()

car_enemy_image=pyglet.resource.image('tsquare.png')
util.center_image(car_enemy_image)

class Car_Enemy(mob.Mob):

    def __init__(self,x,y,*args,**kwargs):
        super(Car_Enemy,self).__init__(car_enemy_image,x,y,*args,**kwargs)
        self.scale=1
        self.is_enemy=True

    def update(self,dt):
        pass

    def handle_collision_with(self,other):
        pass


   
