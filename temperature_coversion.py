# degrees conversion
def celsius_to_fahrenheit(celsius):
    return(celsius*9/5)+32
def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit-32)*5/9
temp=float(input("eneter the temperature values: "))
unit=input("in celsius(c) or fahrenheit(F)").strip().upper()
if unit=="C":
    converted_temp=celsius_to_fahrenheit(temp)
    print(f"{temp}°C is equal to {converted_temp:.2f}°F")
elif unit=="F":
    converted_temp=fahrenheit_to_celsius(temp)
    print(f"{temp}°F is equal to {converted_temp:.2f}°C")
else:
    print("invalid input")