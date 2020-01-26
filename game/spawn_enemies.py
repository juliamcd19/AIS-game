#spawn_enemies.py

import random,enemy

#fill this list with tuples (x,y), where each tuple is a viable spawn location
#possible_enemy_locations=[(100,500),(200,400),(800,200),(100,100)]

#this list will store references to your enemy sprites, it will be appended to game objects
#in the topfile



def spawn_enemies(n,level):

    #n is the number of enemies to spawn
    possible_enemy_locations={1:[(100,500),(200,400),(800,200),(100,100)],
                              2:[(300,300),(100,200),(400,100),(200,400)],
                              3:[(200,200),(300,100),(400,200),(500,300)]}
                              

    if n<=len(possible_enemy_locations[level]):
                          
        enemies=[]

        for i in range(0):
            location=random.choice(possible_enemy_locations[level])
            possible_enemy_locations[level].remove(location)
            x=location[0]
            y=location[1]
            new_enemy=enemy.Enemy()
            new_enemy.x=x
            new_enemy.y=y
            enemies.append(new_enemy)
        

        return enemies
    else:
        print 'not enough locations provided to spawn %i mobs'%(n)

