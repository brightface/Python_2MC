from cs1robots import *

load_world( 'c:/worlds/add34.wld' )

hubo = Robot( street = 2 )


while hubo.front_is_clear():
    hubo.move()

flag = True

l= 0 # 올림한 수

while flag:
    k=0 # n1+n2
    n1=0
    n2=0       
    while 1:    
        if hubo.on_beeper():
            hubo.pick_beeper()
            n1=n1+1
        else :
            break
    
    for a in range(3):
            
        hubo.turn_left()
    hubo.move()
    
    while 1:    
        if hubo.on_beeper():
            hubo.pick_beeper()
            n2=n2+1
        else :
            break
        
    k=n1+n2+l
    
    if k>=10:
        l=1
        k=k-10
    else:
        l=0
        
    for s in range(k):
        hubo.drop_beeper()
    
    for s in range(3):
        hubo.turn_left()
    
    if n1==0 and n2==0 and k==0:
        flag =False
        continue        
    hubo.move()
    
   
    
    for s in range(3):
        hubo.turn_left()
    
    hubo.move()
    
    for s in range(3):
        hubo.turn_left()
        
       
   
          
    
   
    

    



    
        
    
    
    