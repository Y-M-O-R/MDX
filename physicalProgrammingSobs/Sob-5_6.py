"""Yousuf Rahman M0103661
This is a program that records temperature Data, 
and informs you of any relevant information about this temperature
if you wish to modify this code edit the tempHistory List or change the if/elif/else conditions"""

tempChange = []  # current temperature records
tempHistory = [15, 24, 33, 29, 17]  # temperature averages of the past
runCode = True  # loops run while this condition is true
while runCode:
    temp = int(input("What is the temperature(c*)="))  # user enters current temperature data
    tempChange.append(temp)
    if temp >= 100:
        print("it is boling")

    elif temp == 0:
        print("it is freezing")

    else:
        if temp > 0:
            print("Temperature =", temp, "degrees celcius")
        else:  # if temp is negative we can exit the code
            runCode = False
            print("Exit")

    for tCurrent in tempChange:  # compare the recent recorded temperatures against temperature averages of the past
        for tPast in tempHistory:
            if tCurrent == tPast: # data matches past temperature
                print(tempPast, "is an Average temperature")
