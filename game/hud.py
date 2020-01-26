#hud.py

import pyglet,viewport

hud_batch=pyglet.graphics.Batch()
score_batch=pyglet.graphics.Batch()

'''
instantiate all of your labels and or graphic icons here

make sure to set all of their batch attributes to hud_batch

do not draw them in this module

in the topfile, add hud_batch.draw() to the on_draw handler
'''
font_color=(255,255,255,255)
score_counter=0

score_label=pyglet.text.Label(text='Score:0',
                              anchor_x='left',
                              anchor_y='top',
                              x=0,
                              y=viewport.window.height,
                              font_size=24,
                              batch=score_batch)

#lives_label=pyglet.text.Label(text='Lives:3',
                              #anchor_x='right',
                              #anchor_y='top',
                              #x=viewport.window.width,
                              #y=viewport.window.height,
                              #font_size=32,
                              #batch=hud_batch)


#game_over_label=pyglet.text.Label(text='GAME OVER',
                                  #anchor_x='center',
                                  #anchor_y='center',
                                  #x=viewport.h_ctr,
                                  #y=-300,
                                  #font_size=72,
                                  #batch=hud_batch)

time_label=pyglet.text.Label(text='Time:50',
                             anchor_x='center',
                             anchor_y='top',
                             x=viewport.h_ctr,
                             y=viewport.window.height,
                             batch=hud_batch,
                             font_size=24,
                             color=font_color)


