# Svarsfil till inlämningsuppgiften i Grundläggande programmering i Python augusti 2025.

# Denna rad används för att namnge CSV-filen i koden. Använd sedan variabeln "filnamn" när du skapar din kod.
#filnamn = input('Vad vill du döpa din CSV-fil till? Avsluta namnet med .csv ' ) or 'exempelCSV.csv'
filnamn = 'skattresultat.csv'
# Skriver ut filnamnet så att du ser att det blev rätt.
print('Du valde filnamnet', filnamn)

# Hur du kör koden:

# Skriv din kod här:

## Del 1

# Imports
import random
import csv
import matplotlib.pyplot as plt
# Slut på imports

# Globala Variabler
treasure = 50000

# options är ett bibliotek med alternativ för användaren under startmenyn
# Det är bättre att använda ett bibliotek för att det är lättare att utöka eller minska
options = {
    "s":"Spela Skattjakten",
    "t":"Visa Topplistan",
    "r":"Visa tidigare resultat",
    "q":"Avsluta spelet"
}

min_doors = 1
max_doors = 10
# Slut på globala variabler

# start_menu(options) är en funktion som används för att starta upp startmenyn 
# och printar alternativen.
# options: ett bibliotek för alla olika spelalternativ
def start_menu(options):
    print("\n***STARTMENYN***\n")
    for key in options:                                                         # Itererar genom options biblioteket och printar alla olika spelalternativ
        print(f"{key}) {options[key]}")
        print()

# draw_doors(max_doors, used_doors) är en hjälpfunktion som används för att rita upp alla 
# dörrar som används i spelet.
# max_doors: max antal dörrar som använda i spelet
# used_doors: dörrarna som användaren tidigare har öppnat under spelet
def draw_doors(max_doors, used_doors):
    top = ""
    sides = ""
    number_row = ""
    bottom = ""

    for i in range(1, max_doors + 1):
        if i not in used_doors:
            top += "  ________  "
            sides += " |        | "
            number = str(i).center(8)
            number_row += f" |{number}| "
            bottom += " |________| "

    print(top)
    print(sides)
    print(number_row)
    print(bottom)

# treasure_hunt(treasure_door, used_doors, user_input) är en funktion som kollar ifall att 
# dörren som användaren vill öppna är en dörr som redan är öppen, en dörr
# där skatten ligger bakom, eller en dörr där ingen skatt ligger bakom.
# treasure_door: dörren som slumpmässigt valdes, där skatten ligger bakom
# used_doors: en array av dörrar som användaren tidigare har valt
# user_input: användarens input, vilken dörr användaren har valt att öppna
def treasure_hunt(treasure_door, used_doors, user_input):
    if user_input in used_doors:
        print("Du kan inte välja en dörr som du redan har öppnat! Välj en annan dörr!")
        return False
    used_doors.append(user_input)                                               # Lägger till senast valda dörr i en array av använda dörrar
    if user_input == treasure_door:
        score = len(used_doors)
        treasure_final = treasure_value(treasure, score)
        print(f"*****Grattis! Du har hittat skatten bakom dörr {treasure_door}, efter {score} försök!*****")
        print(f"Din slutgiltiga skatt efter {score} försök: {treasure_final}")

        return True
    else:
        print(f"*****Hoppsan! Ingen skatt hittades bakom dörr {user_input}, skatten halveras!*****")
        return False

# treasure_value(treasure, score) är en hjälpfunktion som använda för att 
# räkna ut skatten som har halverats efter varje felaktig försök.
# treasure: skatten som användaren vill hitta bakom en slumpmässig dörr
# score: antal försök användaren hade för att hitta rätt dörr
def treasure_value(treasure, score):
    exp = pow(2, score)
    if score == 1:
        return treasure
    else:
        return treasure / exp


# save_result(name, score, file_name) är en funktion som används för att spara 
# användarens uppgifter i csv-filen.
# name: namnet på användaren som angetts i början av spelet
# score: antal försök användaren hade innan de hittade skatten
# file_name: namnet på csv-filen vi kommer skriva till
def save_result(name, score, file_name):
    try:
        with open(file_name, 'r') as file:
            file_exists = True
    except FileNotFoundError:
        file_exists = False
    
    with open(file_name, 'a') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Namn", "Försök\n"])
        writer.writerow([name, score])

# Funktionen använder exempelCSV.csv-filen
# def show_leaderboard():
#     data_list = []
#     try:
#         with open('exempelCSV.csv', 'r', encoding='utf-8') as file:
#             csv_reader = csv.reader(file, delimiter=',')
#             next(csv_reader)

#             for row in csv_reader:
#                 data_list.append(row)
        
#         data_list.sort(key=lambda x: int(x[1]))

#         print("\n*****Topplistan*****\n")
#         print("\nNamn       | Försök ")
#         print("-------------------")

#         for row in data_list:
#             print(f"{row[0]:<10} |  {row[1]:>5}")

#     except FileNotFoundError: 
#         print("*****Ingen resultatfil hittades.*****")

# show_leaderboard(file_name) är en funktion som används för att printa ut 
# topplistan enligt csv-filen.
# file_name: namnet på csv-filen som användaren angett innan spelet påbörjades
def show_leaderboard(file_name):
    data_list = []
    try:
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            next(csv_reader)

            for row in csv_reader:
                data_list.append(row)
        
        data_list.sort(key=lambda x: int(x[1]))

        print("\n*****Topplistan*****\n")
        print("\nNamn       | Försök ")
        print("-------------------")

        for row in data_list:
            print(f"{row[0]:<10} |  {row[1]:>5}")

    except FileNotFoundError: 
        print("*****Ingen resultatfil hittades.*****")


# quit_game(name) är en quit-funktion som används för att avsluta spelet
# name: namnet på spelaren
def quit_game(name):
    print("\n************************************************************\n")
    print(f"   Tack för att du spelade Templets Tio Dörrar, {name}!")
    print("\n************************************************************\n")
    return False

# main() är en main funktion som hanterar all user input och hanterar
# vad användaren vill göra i spelet.
def main():
    name = input("Vad heter du? ")
    print(f"\n*****Välkommen till Templets Tio Dörrar, {name}! Skatten med värde {treasure} finns bakom en av dörrarna!*****\n")
    while True:
        start_menu(options)
        user_input = input("Välj ett alternativ: ").lower()                     # .lower() Tillåter både stora och små bokstäver att användas

        if user_input == "s":
            treasure_door = random.randint(1, 10)                               # Väljer en slumpmässig dörr mellan 1 och 10, där skatten befinner sig bakom
            used_doors = []                                                     # En lista där alla valda dörrar kommer appendas till, för felhantering
            while True:
                draw_doors(max_doors, used_doors)
                print()
                user_input = int(input("Vilken dörr vill du öppna? "))
                print()
                if user_input < min_doors or user_input > max_doors:            # Kollar ifall att den valda dörren är en giltig dörr
                    print("Ogiltigt dörrnummer! Välj mellan 1 och 10.")
                    continue
                found = treasure_hunt(treasure_door, used_doors, user_input)
                if found:                                                       # If-satsen körs om användaren har hittat rätt dörr, annars fortsätter while-loopen
                    score = len(used_doors)
                    save_result(name, score, filnamn)
                    break
        elif user_input == "t":
            show_leaderboard(filnamn)
        elif user_input == "r":
            print("This calls the function that shows previous results")
        elif user_input == "q":
            return quit_game(name)
        else:
            print("\n**************************\n")
            print("Ogiltigt val, försök igen!")
            print("\n**************************\n")

main()
