# Svarsfil till inlämningsuppgiften i Grundläggande programmering i Python augusti 2025.

# Denna rad används för att namnge CSV-filen i koden. Använd sedan variabeln "filnamn" när du skapar din kod.
#filnamn = input('Vad vill du döpa din CSV-fil till? Avsluta namnet med .csv ' ) or 'exempelCSV.csv'

filnamn = 'skattresultat.csv'
# filnamn = 'exempelCSV.csv'

# Skriver ut filnamnet så att du ser att det blev rätt.
print('Du valde filnamnet', filnamn)

# Hur du kör koden:
# 1. Om du vill köra koden med din fil 'skattresultat.csv' kan du gå vidare till
# steg 2, men om du vill köra med 'exempelCSV.csv' filen bör du kommentera 
# rad 6 och ta bort kommentaren på rad 7.
# 2. Skriv 'python InlAug2025.py' i terminalen
# 3. Välj ett alternativ från startmenyn.
    # s: Spela skattjakten
    # t: Visa topplistan enligt csv-filen på rad 5
    # d: Visa diagrammet på statistiken enligt csv-filen på rad 5
    # q: Avsluta spelet

# Skriv din kod här:

## Del 1

############ IMPORTS ############
import random
import csv
import matplotlib.pyplot as plt
######## SLUT PÅ IMPORTS ########


############# GLOBALA VARIABLER #############
# options är ett bibliotek med alternativ för användaren under startmenyn
# Det är bättre att använda ett bibliotek för att det är lättare att utöka eller minska
options = {
    "1":"Spela Skattjakten",
    "2":"Visa Topplistan",
    "3":"Visa ett diagram på tidigare resultat",
    "4":"Avsluta spelet"
}

min_doors = 1
max_doors = 10
######### SLUT PÅ GLOBALA VARIABLER #########


# En funktion som används för att starta upp startmenyn 
# och printar alternativen.
# options: ett bibliotek för alla olika spelalternativ
def start_menu(options):
    print("\n***STARTMENY***\n")
    for key in options:                                                         # Itererar genom options biblioteket och printar alla olika spelalternativ
        print(f"{key}) {options[key]}")
        print()


# En hjälpfunktion som används för att rita upp alla dörrar som används i spelet.
# max_doors: max antal dörrar som använda i spelet
# used_doors: dörrarna som användaren tidigare har öppnat under spelet
def draw_doors(max_doors, used_doors):
    # Dessa strängar bygger upp den visuella bilden av varje dörr i spelet.
    top = ""
    sides = ""
    number_row = ""
    bottom = ""

    # For-loopen ritar upp dörrarna från dörr 1 till 10. Range börjar från 1 
    # eftersom att vi inte har en dörr som är markerad 0, och går till 
    # max_doors + 1 (10 + 1) för att få alla 10 dörrar. 
    # If-satsen ritar upp dörrarna som användaren inte har öppnat ännu, vilket utökar 
    # visualiseringen för användaren om vilka dörrar som finns kvar att öppna.
    for i in range(1, max_doors + 1):
        if i not in used_doors:
            top += "  ________  "
            sides += " |        | "
            number = str(i).center(8)                                           # Gör siffran i till en sträng, och centrerar den i mitten av dörren
            number_row += f" |{number}| "
            bottom += " |________| "

    print(top)
    print(sides)
    print(number_row)
    print(bottom)


# En funktion som kollar ifall att dörren som användaren vill öppna är en
# dörr som redan är öppen, en dörr där skatten ligger bakom, eller en dörr 
# där ingen skatt ligger bakom. Menyval 1
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
        # treasure_final = treasure_value(treasure, score)
        print("****************************************************************************************************\n")
        print(f"          Grattis! Du har hittat skatten bakom dörr {treasure_door}, efter {score} försök!")
        print("\n****************************************************************************************************")
        # print(f"Din slutgiltiga skatt efter {score} försök: {treasure_final}")
        return True
    else:
        print(f"*****Hoppsan! Ingen skatt hittades bakom dörr {user_input}. Skatten har nu halverats!*****")
        return False


# En funktion som används för att spara användarens uppgifter i csv-filen.
# name: namnet på användaren som angetts i början av spelet
# score: antal försök användaren hade innan de hittade skatten
# file_name: namnet på csv-filen vi kommer skriva till
def save_result(name, score, file_name):
    # Öppnar filen med avseende på att kunna appenda och spara data till filen.
    with open(file_name, 'a') as file:
        writer = csv.writer(file)                                               # Skapar en writer filobjekt som används för att skriva till filen
        writer.writerow([name, score])                                          # Skriver en rad till csv-filen med både namnet och antal försök


# En funktion som används för att printa ut topplistan enligt csv-filen.
# Menyval 2
# file_name: namnet på csv-filen vi kommer läsa data ifrån
def show_leaderboard(file_name):
    # En tom lista som är gjord för att innehålla användarna i csv-filen
    # och deras poäng.
    user_list = []

    # Öppnar upp csv-filen med avseende på att läsa från filen och skapar en reader 
    # där vi kan iterera genom varje rad i filen som en lista av värden.
    # Delimiter innebär att värdena i varje rad skiljas med ett kommatecken.
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')                            # Skapar en reader filobjekt som används för att läsa från filen
        next(csv_reader)                                                        # Hoppar över första raden "Namn,Försök" i csv-filen 

        # Itererar genom varje rad av csv-filen och appendar varje rad till user_list.
        for row in csv_reader:
            user_list.append(row)
    
    user_list.sort(key=lambda x: int(x[1]))                                     # Sorterar user_list beroende på andra värdet i varje element genom x[1] som är en int

    print("\n*****Topplistan*****\n")
    print("\nNamn       | Försök ")
    print("-------------------")
    
    # Itererar genom varje element i user_list och printar ut det som en tabell.
    for row in user_list:
        print(f"{row[0]:<10} |  {row[1]:>5}")


# En hjälpfunktion som räknar frekvensen av ett visst antal försök (n) 
# förekommer i listan.
# list: listan med varje försök från alla spelare från topplistan
# n: nuvarande antal försök vi vill räkna frekvensen av
def counter(list, n):
    count = 0                                                                   # En tom counter
    for try_value in list:                                                      # Try_value är nuvarande antal på försöket vi vill räkna frekvensen av
        if try_value == n:
            count = count + 1                                                   # Ökar countern med 1 varje gång try_value matchar n
    return count


# En funktion som används för att rita upp ett diagram på statistiken av antal
# försök det krävdes för alla spelare som finns i csv-filen.
# file_name: namnet på csv-filen där vi kommer läsa data ifrån
def show_diagram(file_name):
    try_list = []                                                               # En tom lista med antal försök från varje spelare enligt .csv-filen

    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)                                           # Skapar en reader filobjekt som används för att läsa från filen
        next(csv_reader)                                                        # Hoppar över första raden "Namn,Försök" i csv-filen

        for row in csv_reader:
            user_try = int(row[1])                                              # Hämtar ut nuvarande användarens antal försök från raden genom att ta idex 1
            try_list.append(user_try)                                           # Appendar nuvarande användarens försök till listan med alla försök
    
    counts = []                                                                 # En tom lista som kommer innehålla antal spelare det för försök 1-10

    # Denna for loop räknar hur många spelare som har behövt 1 till 10
    # försök för att avsluta spelet.
    for i in range(1, 11):
        counts.append(counter(try_list, i))                                     # Appendar summan av i försök till counts listan.
    
    plt.bar(range(1, 11), counts)                                               # Plottar ett diagram där x-axeln kommer representera 1-10 och y-axeln antal spelare
    plt.xlabel('Försök')                                                        # X-axeln i stapeldiagrammet
    plt.ylabel('Antal spelare')                                                 # Y-axeln i stapeldiagrammet
    plt.title('Statistik: Hur många försök har spelarna behövt')                # Titel på stapeldiagrammet
    plt.xticks(range(1, 11))                                                    # Visar att x-axeln kommer bestå av värdena 1-10
    plt.show()                                                                  # Öppnar upp diagrammet


# En quit-funktion som används för att avsluta spelet. Menyval 4
def quit_game():
    print("\n************************************************************\n")
    print(f"      Tack för att du spelade Templets Tio Dörrar!")
    print("\n************************************************************\n")
    return False                                                                # Returnerar False för att avsluta while-loopen i main() funktionen


# En main funktion som hanterar all user input och hanterar
# vad användaren vill göra i spelet.
def main():
    print(f"\n*****Välkommen till Templets Tio Dörrar! Skatten finns bakom en av dörrarna!*****\n")
    while True:                                                                 # En while-loop för att användaren ska kunna fortsätta spelet tills den vill avsluta spelet
        start_menu(options)
        user_input = input("Välj ett alternativ: ").lower()                     # .lower() tillåter både stora och små bokstäver att användas

        if user_input == "1":
            treasure_door = random.randint(1, 10)                               # Väljer en slumpmässig dörr mellan 1 och 10, där skatten befinner sig bakom
            used_doors = []                                                     # En lista där alla valda dörrar kommer appendas till, för felhantering
            
            while True:
                draw_doors(max_doors, used_doors)                               # Ritar upp dörrarna som användaren kan välja att öppna. 
                print()
                
                try:
                    user_input = int(input("Vilken dörr vill du öppna? "))      # Konverterar strängen som är användarens input till en int för att välja en dörr
                    print()
                except:                                                         # Felhantering om användaren inte väljer en giltig dörr
                    print("Välj ett heltal mellan 1 och 10.\n")
                    break

                found = treasure_hunt(treasure_door, used_doors, user_input)    # Kollar om användaren har hittat rätt dörr

                if found:                                                       # If-satsen körs om användaren har hittat rätt dörr, annars fortsätter while-loopen
                    score = len(used_doors)                                     # Antal försök innan användaren hittade rätt dörr
                    name = input("Vad heter du? ")
                    save_result(name, score, filnamn)
                    break                                                       # Avslutar denna while-loop för att användaren kan komma tillbaka till startmenyn
        elif user_input == "2":
            show_leaderboard(filnamn)                                           # Anropar och kör topplista-funktionen
        elif user_input == "3":
            show_diagram(filnamn)                                               # Anropar och kör diagram-funktionen
        elif user_input == "4":
            return quit_game()                                                  # Anropar och kör quit-funktionen
        else:                                                                   # Hanterar felaktig inmatning
            print("\n**************************\n")
            print("Ogiltigt val, försök igen!")
            print("\n**************************\n")


main()                                                                          # Anropar och kör main-funktionen för att påbörja spelet