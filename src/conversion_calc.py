"""
Natalie Ferraro conversion_calc.py
conversion_calc.py is a type conversion calculator that converts a user's input from imperial to metric or viceversa.
"""

conversion = input("What conversion would you like to perform (i -> m == i || m -> i == m)\n")

imperial = "i"
metric = "m"

length = "l"
weight = "w"
temp = "t"
volume = "v"

while True:
    con_type = input("What type of conversion would you like to perform (length = l || weight = w || volume == v) || temp == t)\n")
    if conversion == imperial:
        if con_type == length:
            user_input = input("Enter the length in inches\n")
            centimeters = float(user_input)*2.54
            print("centimeters = ", centimeters)
        elif con_type == weight:
            user_input = input("Enter the weight in pounds\n")
            kilograms = float(user_input)/2.205
            print("kilograms = ", kilograms)
        elif con_type == temp:
            user_input = input("Enter the temp in fahrenheit\n")
            celcius = (float(user_input)-32)*5/9
            print("celcius = ", celcius)
        else:
            user_input = input("Enter the volume in ounces\n")
            milliliters = float(user_input)*28.4
            print("milliliters = ", milliliters)
    #conversion from imperial to metric

    elif conversion == metric:
        if con_type == length:
            user_input = input("Enter the length in centimeters\n")
            inches = float(user_input)/2.54
            print("inches = ", inches)
        elif con_type == weight:
            user_input = input("Enter the weight in kilograms\n")
            pounds = float(user_input)*2.205
            print("pounds = ", pounds)
        elif con_type == temp:
            user_input = input("Enter the temp in celcius\n")
            fahrenheit = (float(user_input)*9/5)+32
            print("fahrenheit = ", fahrenheit)
        else:
            user_input = input("Enter the volume in milliliters\n")
            ounces = float(user_input)/28.4
            print("ounces = ", ounces)
    #conversion from metric to imperial

    else:
        exit_mod = print("Exiting module")
        exit()