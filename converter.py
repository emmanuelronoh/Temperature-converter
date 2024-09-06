def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    
    choice = input("Enter the number of the conversion you want to perform: ")
    
    if choice in ('1', '2', '3', '4', '5', '6'):
        temp = float(input("Enter the temperature: "))
        
        if choice == '1':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp} Celsius is equal to {result} Fahrenheit")
        
        elif choice == '2':
            result = fahrenheit_to_celsius(temp)
            print(f"{temp} Fahrenheit is equal to {result} Celsius")
        
        elif choice == '3':
            result = celsius_to_kelvin(temp)
            print(f"{temp} Celsius is equal to {result} Kelvin")
        
        elif choice == '4':
            result = kelvin_to_celsius(temp)
            print(f"{temp} Kelvin is equal to {result} Celsius")
        
        elif choice == '5':
            result = fahrenheit_to_kelvin(temp)
            print(f"{temp} Fahrenheit is equal to {result} Kelvin")
        
        elif choice == '6':
            result = kelvin_to_fahrenheit(temp)
            print(f"{temp} Kelvin is equal to {result} Fahrenheit")
    
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
