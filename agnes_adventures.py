#agnes_adventures.py

import pyglet
from game import viewport,world,avatar,hud,spawn_enemies,spawn_tokens
from game import token, hidden_token, util, instructions, car_enemy
from game import spawn_car_enemy, spawn_btokens, btoken, sound_fx
from game import spawn_teachers, teacher

level_timer=50

media_player=pyglet.media.Player()
media_player.queue(sound_fx.intromusic)
media_player.eos_action=media_player.EOS_LOOP

def init():

    global inst, event_stack_size, level, level_timer, score, player_has_binder

    event_stack_size=0
    level=2
    inst=instructions.Instructions_display()
    inst.batch=inst_batch
    viewport.window.push_handlers(inst.key_handler)
    pyglet.clock.schedule_interval(inst.update,1/120.0)
    score=0
    player_has_binder=False


def check_instructions(dt):
    media_player.play()
    if inst.complete:
        pyglet.clock.unschedule(inst.update)
        pyglet.clock.unschedule(check_instructions)
        load_level(level)
    
    
def clear_level():

    global game_objects

    if game_objects:
        for obj in game_objects:
            obj.delete()
        game_objects=[]
    
            

def load_level(level):

    global game_objects, hidden, player, event_stack_size, victory, token
    global tokens_collected, max_tokens, car_enemy, lever_timer, player_has_binder

    while event_stack_size>0:
        viewport.window.pop_handlers()
        event_stack_size-=1

    event_stack_size=0

    
    
    
    game_objects=[]
    reload(world)
    world.generate_world(level)

     
    

    if level==1:
        pyglet.gl.glClearColor(0.75,0.75,0.75,1.0)
        media_player.play()
        player=avatar.Avatar(batch=main_batch)
        game_objects.append(player)
        collectibles=spawn_tokens.spawn_tokens(1,level)
        for collectible in collectibles:
            collectible.batch=main_batch
        game_objects+=collectibles
    
        car_enemies=spawn_car_enemy.spawn_car_enemy(18)
        for car_enemy in car_enemies:
            car_enemy.batch=main_batch
        game_objects+=car_enemies

        if not player_has_binder:
            btokens=spawn_btokens.spawn_btokens(2,1)
            for btoken in btokens:
                btoken.batch=main_batch
            game_objects+=btokens

        level_timer=50
        hud.time_label.color=(255,255,255,255)

    elif level==2:
        pyglet.gl.glClearColor(0.7,0.8,0.75,1.0)
        media_player.pause()
        level_timer=0
        hud.time_label.text='Time:0'
        player=avatar.Avatar2(batch=main_batch)
        game_objects.append(player)
        token=token.Token2(batch=main_batch)
        game_objects.append(token)
        
        teachers=spawn_teachers.spawn_teachers(1,2)
        for teacher in teachers:
            teacher.batch=main_batch
        game_objects+=teachers
        
        
        
        
        

        
    hidden=hidden_token.Hidden_token(batch=main_batch)
    hidden.x=250
    hidden.y=500
    hidden.update_bounding_box()
    game_objects.append(hidden)

    enemies=spawn_enemies.spawn_enemies(4,level)
    for enemy in enemies:
        enemy.batch=main_batch
    game_objects+=enemies



    tokens_collected=0
    max_tokens=1

    
    viewport.window.push_handlers(player.key_handler)

    pyglet.clock.schedule_interval(update,1.0/120.0)



def update(dt):

    global tokens_collected, max_tokens, level, level_timer, score, player_has_binder

    player_dead=False
    victory=False

    if hidden in game_objects:
        if util.distance((player.x,player.y),(hidden.x,hidden.y))<=150:
            hidden.found=True


    if level==1:
        level_timer-=dt
        hud.time_label.text='Time:%s'%(str(int(level_timer)))
        if level_timer<0:
            level+=1
            clear_level()
            load_level(level)
            pyglet.clock.unschedule(update)
        
        if level_timer<11.0:
            hud.time_label.color=(205, 17, 23, 255)

    for i in xrange(len(game_objects)):
        for j in xrange(i+1,len(game_objects)):

            obj_1=game_objects[i]
            obj_2=game_objects[j]

            #make sure objects are not dead

            if not obj_1.dead and not obj_2.dead:
                if obj_1.__class__ is not obj_2.__class__:
                    if obj_1.collides_with(obj_2) or obj_2.collides_with(obj_1):
                        obj_1.handle_collision_with(obj_2)
                        obj_2.handle_collision_with(obj_1)

    for obj in game_objects:
        obj.update(dt)

    #get rid of dead objects

    for to_remove in [obj for obj in game_objects if obj.dead]:

        #remove the object from the batch and the game_objects list
        to_remove.delete()
        game_objects.remove(to_remove)


        if to_remove==player:
            player_dead=True
        
        
        #Adjust the score if the dead item was worth points

        if isinstance(to_remove,btoken.Btoken):
            score+=5
            hud.score_label.text="Score:"+str(score)
            sound_fx.tokensound.play()
            player_has_binder=True
        if level==1:
            if isinstance(to_remove,token.Token):
                tokens_collected+=1
                #sound_fx.pop_sound.play()
                score+=20
                hud.score_label.text='Score:'+str(score)
                if tokens_collected==max_tokens:
                    victory=True
                    sound_fx.level_clear_sound.play()
        if level==2:
            if isinstance(to_remove,token.Token2):
                tokens_collected+=1
                #sound_fx.pop_sound.play()
                score+=20
                hud.score_label.text='Score:'+str(score)
                if tokens_collected==max_tokens:
                    victory=True
                    sound_fx.level_clear_sound.play()
        
        

        '''
        
        #Adjust the score if the dead item was worth points
        if isinstance(to_remove,pwr_up.PwrUp):
            score+=to_remove.pt_value
            hud.score_label.text='Score:'+str(score)
            sound_fx.power_up_sound.play()
            avatar.process_power_up()

        #Adjust the score if the dead item was worth points
        if isinstance(to_remove,enemy.Enemy):
            sound_fx.pop_sound.play()
            score+=to_remove.pt_value
            score_label.text='Score:'+str(score)
        '''
        
        
        
    #check for win/lose conditions

    if player_dead:
        #if len(player_lives)>0:
        pyglet.clock.unschedule(update)
        clear_level()
        load_level(level)
        #else:
        #    hud.game_over_label.y=viewport.v_ctr

    elif victory:
        
        level+=1
        #hud.level_label.text='Level:'+str(level)
        pyglet.clock.unschedule(update)
        clear_level()
        level_timer=0
        load_level(level)
    


        
@viewport.window.event
def on_draw():
    viewport.window.clear()
    if not inst.complete:
        inst_batch.draw()
    else:
        world.tile_batch.draw()
        hud.hud_batch.draw()
        hud.score_batch.draw()
    main_batch.draw()
    

@viewport.window.event
def on_close():
    viewport.window.close()
    quit()



if __name__=='__main__':

    pyglet.gl.glClearColor(.9,.9,.6,1.0)
    inst_batch=pyglet.graphics.Batch()
    main_batch=pyglet.graphics.Batch()
    

    init()
    pyglet.clock.schedule_interval(check_instructions,1/120.0)
    
    pyglet.app.run()
