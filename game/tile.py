#tile.py

import pyglet,collidable,util,viewport


pyglet.resource.path.append('./images')
pyglet.resource.reindex()

blue_image=pyglet.resource.image('blue.jpg')
util.set_tile_anchor(blue_image)

green_image=pyglet.resource.image('green.jpg')
util.set_tile_anchor(green_image)

topcar_image=pyglet.resource.image('bcartop.png')
util.set_tile_anchor(topcar_image)

bcar_image=pyglet.resource.image('bcarbottom.png')
util.set_tile_anchor(bcar_image)


tile_mapping={1:blue_image,
              2:green_image,
              3:topcar_image,
              4:bcar_image}

solid_tile_types=[1,2,3,4]

class Tile(collidable.Collidable):
    

    def __init__(self, *args, **kwargs):

        super(Tile, self).__init__(*args, **kwargs)
        

   

       
        
        
