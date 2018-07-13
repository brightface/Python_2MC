from cs1robots import *

load_world( 'c:/worlds/newspaper.wld' )

hubo = Robot( beepers=1 )
hubo.set_trace( 'blue' )

def moves(n=1):
    for a in range(n):
        hubo.move()

def step_up(n=1):
    for a in range(n):
        hubo.turn_left()
        hubo.move()
        left_turns(3)
        moves(2)
        
def step_down(n=1):
    for a in range(n):
        moves(2)
        hubo.turn_left()
        hubo.move()
        left_turns(3)
        
def left_turns(n=1):
    for a in range(n):
        hubo.turn_left()
        

moves()
step_up(4)

hubo.drop_beeper()

left_turns(2)

step_down(4)
moves()        