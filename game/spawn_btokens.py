#spawn_btokens.py

import random,btoken

#fill this list with tuples (x,y), where each tuple is a viable spawn location
#possible_token_locations=[(100,500),(200,500),(300,500),(400,500)]

#this list will store references to your enemy sprites, it will be appended to game objects
#in the topfile



def spawn_btokens(kp,level):

    #n is the number of enemies to spawn
    possible_btoken_locations={1:[(1025,100),(889,500)]}
                            


    if kp<=len(possible_btoken_locations[level]):
                          
        btokens=[]

        for i in range(kp):
            location=random.choice(possible_btoken_locations[level])
            possible_btoken_locations[level].remove(location)
            x=location[0]
            y=location[1]
            new_btoken=btoken.Btoken()
            new_btoken.x=x
            new_btoken.y=y
            new_btoken.update_bounding_box()
            btokens.append(new_btoken)

  
        return btokens
    else:
        print 'not enough locations provided to spawn %i mobs'%(kp)
