#token.py

import collidable, util, pyglet, aabb

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

token_image=pyglet.resource.image('park.png')
util.center_image(token_image)

donut_image=pyglet.resource.image('donutbox.png')
util.center_image(donut_image)


class Token(collidable.Collidable):
    
    def __init__(self, *args, **kwargs):
        super(Token,self).__init__(token_image,*args,**kwargs)
        self.scale=0.13

        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)

    def update(self,dt):
        pass


    def update_bounding_box(self):
        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)
    


    
    def handle_collision_with(self,other):

        if other.is_avatar:
            self.dead=True



class Token2(collidable.Collidable):
    
    def __init__(self, *args, **kwargs):
        super(Token2,self).__init__(donut_image,x=925,y=500,*args,**kwargs)
        self.scale=0.3

        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)

    def update(self,dt):
        pass


    def update_bounding_box(self):
        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)
    


    
    def handle_collision_with(self,other):

        if other.is_avatar:
            self.dead=True
           
