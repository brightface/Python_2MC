from cs1robots import *


load_world( 'c:/worlds/challenge_mission_1_1.wld' )

def find_path():
    flag5=True
    hubo.set_trace('blue')
    while flag5:
        
            if hubo.front_is_clear(): #���� ���ٸ�
                hubo.move()
                if not hubo.on_beeper():# ���� ���µ� ���۰� ������ �ǵ��ư���.#
                    for k in range(2):
                        hubo.turn_left()
                    hubo.move()
                    for k in range(3):
                        hubo.turn_left()
                else:
                    flag5=False
            
                     #���� ���µ� ���۰� �ִ�.
            else:
                hubo.turn_left()


def find_start_b(flag):
    flag2 = True
    while flag2:
        if hubo.on_beeper():
                hubo.pick_beeper()
                if hubo.on_beeper():
                    hubo.pick_beeper()
                    if hubo.on_beeper():
                        for k in range(2):
                            hubo.drop_beeper()
                        flag2=False
                    else:
                        for k in range(2):
                            hubo.drop_beeper()
                        find_path()
                else:
                    hubo.drop_beeper()
                    find_path()
                    
        else:
            find_path()
            flag2=False   
    

def find_direction(flag):
    
    while flag:
        flag4=True
        if hubo.front_is_clear(): #���� ������ 1�� ��= ���� ������
            hubo.move()    
            find_start_b(flag2)
            # �̰� ����!!
        if not hubo.front_is_clear():
            #y���� ���� ������ 0�� ��= ���� ������
            
                for b in range(3):
                    hubo.turn_left()
                hubo.move()
                find_start_b(flag2)
                for b in range(3):
                    hubo.turn_left()
                while flag4:
                    if hubo.front_is_clear(): #���� ������
                        hubo.move()    
                        find_start_b(flag2)
                        continue
                    if not hubo.front_is_clear(): #���� ������
                        for b in range(3):
                            hubo.turn_left()
                        for b in range(2):
                            hubo.move()
                            find_start_b(flag2)
                        for b in range(3):
                            hubo.turn_left()
                        flag3=True    
                
                        while flag3:
                            if hubo.front_is_clear():
                                hubo.move()
                                find_start_b(flag2)
                                continue
                            if not hubo.front_is_clear(): # ���� ������
                                flag3= False
                                flag4=False
                   
                    
def find_destination():
    hubo.set_trace('blue')
    
    while flag6:
        find_path()
        if hubo.on_beeper():
            hubo.pick_beeper()
            
            if hubo.on_beeper():
                hubo.pick_beeper()
                for k in range(2):
                    hubo.turn_left()
                flag6=False
                hubo.drop_beeper()
                    
            hubo.drop_beeper()
            
            
        
            
    
    
    
hubo = Robot( street = 2 )
flag =True
flag2 = True
flag3 = True
flag4 = True
flag5= True
flag6 = True

hubo.set_trace('blue')
find_direction(flag)

find_destination()
