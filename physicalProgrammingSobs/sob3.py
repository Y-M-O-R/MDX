import time
btnPress = 0
dayNight = "day"
light_condition=0
def traffic_light_go(lC, dayNight):
    if dayNight=="day":
        if lC == 0:
            print("Red")
            print(lC)
            time.sleep(1)
        elif lC==1:
            print("Yellow")
            time.sleep(1)
        else:
            print("Green")
            time.sleep(1)

    else:
        if lC == 0:
            print("Red")
            print(lC)

            time.sleep(0.5)
        elif lC == 1:
            print("Yellow")
            time.sleep(1)
        else:
            print("Green")
            time.sleep(5)

def traffic_light_stop(lC):
    if lC == 0:
        print("Red")
        time.sleep(5)
    elif lC == 1:
        print("Red")
        time.sleep(10)
    else:
        print("Red")
        time.sleep(15)


while True:
    dayNight = str(input("Day/Night: ")).lower()
    btnPress = int(input("Is button pressed: "))
    light_condition+=1
    print(light_condition)
    if light_condition >=3:
        light_condition=0


    if dayNight == "day":

        if btnPress == 0:
            traffic_light_go(light_condition, dayNight)
            print("go")
        else:
            traffic_light_stop(light_condition)
            print("stop")
    else: # night
        if btnPress == 0:# go
            traffic_light_go(light_condition, dayNight)
            print("go2")
        else:# stop
            traffic_light_stop(light_condition)

            print("stop2")


