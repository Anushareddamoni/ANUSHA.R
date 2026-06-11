temp=float(input("enter temparature: "))
unit=input("enter units(K or F or C): ")
if(unit=="C"):
    fahrenheit=(temp*9/5)+32
    kelvin=temp+273.15
    print(f"Temparature in Fahrenheit:{fahrenheit}F ")
    print(f"Temparature in Kelvin:{kelvin}K" )
elif(unit=="F"):
    celsius=(temp-32)*5/9
    kelvin=celsius+273.15
    print(f"Temparature in Celsius:{celsius}C")
    print("Temparature in Kelvin:{kelvin}K")
elif(unit=="K"):
    celsius=(temp-32)*5/9
    fahrenheit=(celsius*9/5)+32
    print(f"Temparature in Celsius:{celsius}C")
    print("Temparature in Fahrenheit:{fahrenheit}F")
else:
    print("invalid unit! use C, F, or K")
        