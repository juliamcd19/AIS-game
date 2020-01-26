#avatar.py

import mob, pyglet, util
from pyglet.window import key


pyglet.resource.path.append('./images')
pyglet.resource.reindex()

avatar_image=pyglet.resource.image('sportscar.png')
util.center_image(avatar_image)

avatar_left_image=pyglet.resource.image('carleft.png')
util.center_image(avatar_left_image)

studentavatar_image=pyglet.resource.image('studentavatar.png')
util.center_image(studentavatar_image)

avatar_pwrup_image=pyglet.resource.image('bat.png')
util.center_image(avatar_pwrup_image)


class Avatar(mob.Mob):

    def __init__(self,*args,**kwargs):
        super(Avatar,self).__init__(avatar_image,x=100,y=550,*args,**kwargs)
        self.key_handler=key.KeyStateHandler()
        self.scale=0.055
        self.spd=200
        

        self.vel_y=0

        self.is_avatar=True
        self.death_timer=0
   
    def update(self,dt):

        self.death_timer-=dt

        dx=0
        dy=0
        
        if self.key_handler[key.RIGHT]:
            self.image=avatar_image
            dx=self.spd*dt
    
            
        if self.key_handler[key.LEFT]:
            self.image=avatar_left_image
            dx=-1*self.spd*dt


        if not self.affected_by_gravity:
           

            if self.key_handler[key.UP]:
                dy=self.spd*dt
                

            if self.key_handler[key.DOWN]:
                dy=-1*self.spd*dt

                
        if self.affected_by_gravity:
            if not self.supported:
                self.vel_y-=self.acc*dt
                dy=self.vel_y*dt

        if self.supported:
            if self.key_handler[key.SPACE]:
                self.jump()

                

        super(Avatar,self).update(dx,dy,dt)


    def handle_collision_with(self,other):
        if self.death_timer<=0:
            if other.is_enemy:
                self.dead=True
                print "OW, i'm dead"
                self.death_timer=2
        elif other.is_pwrup:
            self.power_up()

    def power_up(self):
        self.image=avatar_pwrup_image
        self.speed=400
        pyglet.clock.schedule_once(self.revert,5)

    def revert(self,dt):
        self.image=avatar_image
        self.speed=200
        


    def jump(self):
        self.supported=False
        self.vel_y=600


class Avatar2(mob.Mob):

    def __init__(self,*args,**kwargs):
        super(Avatar2,self).__init__(studentavatar_image,x=31,y=430,*args,**kwargs)
        self.key_handler=key.KeyStateHandler()
        self.scale=0.3
        self.spd=200
        

        self.vel_y=0

        self.is_avatar=True
        self.death_timer=0
   
    def update(self,dt):

        self.death_timer-=dt

        dx=0
        dy=0
        
        if self.key_handler[key.RIGHT]:
            dx=self.spd*dt
    
            
        if self.key_handler[key.LEFT]:
            dx=-1*self.spd*dt


        if not self.affected_by_gravity:
           

            if self.key_handler[key.UP]:
                dy=self.spd*dt
                

            if self.key_handler[key.DOWN]:
                dy=-1*self.spd*dt

                
        if self.affected_by_gravity:
            if not self.supported:
                self.vel_y-=self.acc*dt
                dy=self.vel_y*dt

        if self.supported:
            if self.key_handler[key.SPACE]:
                self.jump()

                

        super(Avatar2,self).update(dx,dy,dt)


    def handle_collision_with(self,other):
        if self.death_timer<=0:
            if other.is_enemy:
                self.dead=True
                print "OW, i'm dead"
                self.death_timer=2
        elif other.is_pwrup:
            self.power_up()

    def power_up(self):
        self.image=avatar_pwrup_image
        self.speed=400
        pyglet.clock.schedule_once(self.revert,5)

    def revert(self,dt):
        self.image=avatar_image
        self.speed=200
        


    def jump(self):
        self.supported=False
        self.vel_y=600
