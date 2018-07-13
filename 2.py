from cs1robots import *

load_world( 'c:/worlds/harvest3.wld' )

hubo = Robot( beepers = 10 )
hubo.set_trace( 'blue' )

hubo.move()

for w in range(6):
    for a in range(5):
        if not hubo.on_beeper():
            hubo.drop_beeper()
        hubo.move()
    
    if not hubo.front_is_clear(): #벽이 있으면
        hubo.turn_left()
        if not hubo.on_beeper():
            hubo.drop_beeper()        
        hubo.move()
        
        hubo.turn_left()
        
    else : # 벽이 없으면
        for j in range(3):
            hubo.turn_left()
        
        if not hubo.on_beeper():
            hubo.drop_beeper()            
        hubo.move()
        
        for j in range(3):
            hubo.turn_left()
    
    
    