from cs1robots import *
import sys

load_world('c:/worlds/small_mission_1_0.wld')


    
    

def find_direction():
    if hubo.on_beeper():
        if hubo.on_beeper():
            while 1:
                if hubo.on_beeper():
                    if hubo.on_beeper():
                        break                    
                    hubo.move() #�� ���ĺ��� ����
                    for k in range(3):
                        if hubo.on_beeper(): #������ ���۰� ������
                            break # continue�� ������ ����. 
                        else: #���۰� ������
                            for m in range(4):
                                hubo.turn_left()
                            hubo.move()
                            for m in range(4):
                                hubo.turn_left()
    



 #even number/ odd number

def find_start_postion():

    a=0 #c ���� �ٸ���?
    
    while hubo.front_is_clear():
        hubo.move()    
        find_direction()
        
        if not hubo.front_is_clear():
            #y���� ���� ������
            if a%2==0:
                hubo.turn_left()
            else:
                for b in range(3):
                    hubo.turn_left()            
            
            if not hubo.front_is_clear():
                break
    
            hubo.move()
            find_direction()                                                
            
            if a%2==0:
                hubo.turn_left()
            else:
                for b in range(3):
                    hubo.turn_left()
            
            a=a+1
                    

hubo=Robot()
find_start_postion()
#if find_direction():
    #sys.exit()

    