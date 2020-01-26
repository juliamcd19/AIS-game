#spawn_teachers.py

import random,teacher

#fill this list with tuples (x,y), where each tuple is a viable spawn location
#possible_enemy_locations=[(100,500),(200,400),(800,200),(100,100)]

#this list will store references to your enemy sprites, it will be appended to game objects
#in the topfile



def spawn_teachers(n,level):

    #n is the number of enemies to spawn
    possible_teacher_locations={2:[(475,60,475,700),(625,300,625,875),(400,605,400,630)]}
                              

    if n<=len(possible_teacher_locations[level]):
                          
        teachers=[]

        for i in range(3):
            location=random.choice(possible_teacher_locations[level])
            possible_teacher_locations[level].remove(location)
            x=location[0]
            y=location[1]
            min_x=location[2]
            max_x=location[3]
            new_teacher=teacher.Teacher()
            new_teacher.x=x
            new_teacher.y=y
            new_teacher.min_x=min_x
            new_teacher.max_x=max_x
            teachers.append(new_teacher)
        

        return teachers
    else:
        print 'not enough locations provided to spawn %i mobs'%(n)
