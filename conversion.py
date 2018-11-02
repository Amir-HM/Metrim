import math, time

print("\t\t\033[1;32;40m Hello, welcome to Metrim™")

time.sleep(1)

print("\t Convert imperial units to metric units")

speed_con = "speed"
length_con = "length"
temperature_con = "temperature"

print(speed_con), time.sleep(0.5), print(length_con), time.sleep(0.5), print(temperature_con), time.sleep(0.75)

def speed():
    miles = input("Miles:")
    mil_km = (int(miles)) * 1.609
    print(mil_km)

def length():
    Foot = input("Feet:")
    feet_m = float(Foot) * 30.48
    print(feet_m)

def temp():
    fahrenheit = input("Fahrenheit:")
    fahr_cel = (int(fahrenheit) - 32) * 5/9
    print(fahr_cel)

user_conversion = input("What would you like to convert?")

while True:
    if user_conversion == speed_con:
        print("\t\t   Converting speed!")
        speed()
        break
    elif user_conversion == length_con:
        print("\t\t   Converting length!")
        length()
        break
    elif user_conversion == temperature_con:
        print("\t\t   Converting temperature!")
        temp()
        break
    else:
        user_conversion == speed_con
        print("Invalid pick, please try again.")
        user_conversion = input("Choose your conversion:")
