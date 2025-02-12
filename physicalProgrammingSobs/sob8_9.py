import random


def temperature_convertor(tempChange, tempOriginal, unit):
    tempChange = tempChange.lower()
    tempOriginal = tempOriginal.lower()
    unit = float(unit)
    if tempOriginal == "celsius":

        if tempChange == "fahrenheit":
            unit += 33.8
        elif tempChange == "kelvin":
            unit += 274.15
        else:
            print("Incorrect temperature type chosen")

    elif tempOriginal == "fahrenheit":
        if tempChange == "celsius":
            unit -= -17.22
        elif tempChange == "kelvin":
            unit += 255.93
        else:
            print("Incorrect temperature type chosen")

    elif tempOriginal == "kelvin":
        if tempChange == "celsius":
            unit -= 272.15
        elif tempChange == "fahrenheit":
            unit -= -457.87
        else:
            print("Incorrect temperature type chosen")
    else:
        print("Incorrect temperature type chosen")

    return tempChange, unit




run = True
while run:
    choice = int(input("1:Convert Temp, 2: Convert Random Temps, 3:Exit = "))
    if choice == 1:
        tC = str(input("What unit do you want to change to: "))
        tO = str(input("What is the original unit: "))
        tU = float(input("What is the value of the unit: "))
        temperatureType, temperatureUnit = temperature_convertor(tC, tO, tU)
        print("It is", temperatureUnit, temperatureType, "outside")
    elif choice == 2:

        tC = random.randint(1, 4)
        tO = random.randint(1, 4)
        tU = float(random.randint(1, 101))
        if tC == 1:
            tC = "celsius"
        elif tC == 2:
            tC = "kelvin"
        else:
            tC = "fahrenheit"

        if tO == 1:
            tO = "celsius"
        elif tO == 2:
            tO = "kelvin"
        else:
            tO = "fahrenheit"

        temperatureType, temperatureUnit = temperature_convertor(tC, tO, tU)
        print("It is", temperatureUnit, temperatureType, "outside")
    elif choice == 3:
        run = False
        print("Exit")

    else:
        print("choose correct choice")
