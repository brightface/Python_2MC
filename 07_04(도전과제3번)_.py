from cs1robots import *

load_world('c:/worlds/harvest1.wld')

hubo = Robot()

hubo.set_trace('blue')
 #even number/ odd number

a=0 #c 언어랑 다른가?
while hubo.front_is_clear():
    hubo.move()    
    if hubo.on_beeper():
        hubo.pick_beeper()
    
    if not hubo.front_is_clear():
        #y축의 벽이 있으면
        if a%2==0:
            hubo.turn_left()
        else:
            for b in range(3):
                hubo.turn_left()            
        
        if not hubo.front_is_clear():
            break

        hubo.move()
        if hubo.on_beeper():
            hubo.pick_beeper()                                                
        
        if a%2==0:
            hubo.turn_left()
        else:
            for b in range(3):
                hubo.turn_left()
        
        a=a+1
                    
    