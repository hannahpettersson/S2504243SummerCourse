# Tentamen 2025-08-18 -- 19
print("Uppgift 3 (4)\n")
# Skriv din kod nedan

# 32°F är basen för Fahrenheit och då lägger man 
# till temperaturen gånger med omvandligen för 1°C
def cel_fahr(temp):
    return 32 + (temp * (9 / 5))

# Vi tar bort basen för Fahrenheit och dividerar 
# med omvandlingen för 1°C
def fahr_cel(temp):
    return (temp - 32) / (9 / 5)
        

# main()-funktionen hanterar input
def main():
    while True:                                                     # Tillåter oss fortsätta göra omvandlingar tills användaren väljer att avsluta
        user_input = int(input("Vill du omvandla (1) Celsius till Fahrenheit eller (2) Fahrenheit till Celsius?: "))
        if user_input == 1:
            temp = int(input("\nAnge temperaturen i Celsius: "))    # Omvandlar strängen till en int för att kunna använda inputen i beräkningar
            new_temp = cel_fahr(temp)
            print(f"{temp}°C är {new_temp}°F")
        elif user_input == 2:
            temp = int(input("\nAnge temperaturen i Fahrenheit: ")) # Omvandlar strängen till en int för att kunna använda inputen i beräkningar
            new_temp = fahr_cel(temp)
            print(f"{temp}°C är {new_temp}°F")
        else:
            continue
        cont = input("\nVill du göra en ny omvandling? (j/n): ")    # Kollar om användaren vill fortsätta omvandla
        if cont == 'j':
            continue
        else:
            print("\nTack för att du använde temperaturomvandlaren!")
            return False

main()                                                              # kör main()-funktionen
