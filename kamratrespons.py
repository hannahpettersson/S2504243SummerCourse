import csv
import random
import matplotlib.pyplot as plt

while True:
    filnamn = input('Vad vill du döpa din CSV-fil till? Avsluta namnet med .csv ' )
    if filnamn.endswith('.csv'):
        break
    else:
        print("Fel: Filnamnet måste avslutas med .csv")

print('Du valde filnamnet', filnamn) # Skriver ut filnamnet så att du ser att det blev rätt.

def fil_finns(filnamn):
    try:
        with open(filnamn, 'r'):
            return True
    except FileNotFoundError:
        return False

def skapa_fil_om_den_saknas():
    if not fil_finns(filnamn):
        with open(filnamn, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Namn", "Försök"])

def meny_val():
    meny = ["Spela Skattjakten", "Visa topplista", "Visa diagram över tidigare resultat", "Avsluta spelet"]

    print("Alternativ 1: ", meny[0])
    print("Alternativ 2: ", meny[1])
    print("Alternativ 3: ", meny[2])
    print("Alternativ 4: ", meny[3])
    while True:
        try:
            alternativ = int(input("Välj ett alternativ genom att skriva in en siffra, 1-4: ")) #Välj en dörr
            if alternativ < 1 or alternativ > 4: #Kontroll, 1-4
                raise ValueError
            return alternativ
        except ValueError: #Fångar upp felaktig inmatning
                print("Felaktig inmatning, vänligen mata in en siffra mellan 1 och 4.") 
                continue #Spelet fortsätter

def spela_skattjakten():
    print("Du har valt att spela Skattjakten!")
    winner_door = random.randint(1, 10)  # slumpa fram en dörr mellan 1 och 10
    guesses = 0
    kontroll = [] #Tom lista för kontroll
    while True:
        try:
            door = int(input(f"Välj en dörr genom att skriva in en siffra, 1-10: "))
            if door < 1 or door > 10: #Kontroll, siffra mellan 1-10
                raise ValueError(f"Vänligen mata in en siffra mellan 1 och 10.")
            if door in kontroll: #Kontroll, samma dörr som tidigare
                raise ValueError(f"Redan öppnad dörr.")
            kontroll.append(door)
            guesses += 1 #Räknar antal gissningar
            if door == winner_door:
                print(f"Gratulationer du har hittat skatten bakom dörr nr.{door}, efter {guesses} försök!")
                Namn = input("Skriv ditt namn: ")
                with open(filnamn, 'a', newline='') as f_w:
                    csv_writer = csv.writer(f_w)
                    csv_writer.writerow([Namn, guesses]) #Namn och Antal försök läggs in i CSV-filen
                break #Återgå till MENY
            else:
                print(f"Fel dörr, vänligen försök igen!")
        except ValueError as e:
            print(f"Felaktig inmatning: {e}") #ValueError fångas upp

def visa_topplista():
    with open(filnamn, 'r') as f_r:
        reader = csv.reader(f_r)
        header = next(reader) #Header tilldelas rubriken "Namn" och "Försök"
        print(f"{header[0]:<10}{header[1]:>10}")
        print('-'*20)
        topplista = [] #Lokal tom lista
        for rad in reader:
                topplista.append((rad[0], int(rad[1]))) #kopierar csv-filen till lokal lista
        topplista.sort(key = lambda x: x[1]) #Sorterar listan utifrån andra kolumnen [1] 
        for rad in topplista:
                print(f"{rad[0]:<10}{rad[1]:>10}") #Skriver ut topplistan, rad för rad

def visa_diagram():
    with open(filnamn, 'r') as f_r:
        reader = csv.reader(f_r)
        next(reader) #Fångar upp rubriken
        rader = list(reader) #Kopierar csv för att kunna använda for-loop flera gånger
        
        räknare = {} #lokal dict
        for rad in rader:
            antal_försök = rad[1] #Pekar på andra kolumnen
            if antal_försök in räknare:
                räknare[antal_försök] += 1 #Om flera spelare har samma antal försök adderas 1 till dict
            else:
                räknare[antal_försök] = 1  #Om inte skapas en ny rad i dict med antal försök
    x = sorted(räknare.keys()) #X ska ange antal försök som visas i kolumn 2, sorterar för att hålla koll
    y = [räknare[k] for k in x] #Y ska ange antal spelare

    plt.grid(linestyle = 'dashed') #grid
    plt.title('Statistik: Hur många försök har spelare behövt') #Titel
    plt.xlabel('Antal försök') #x-axel rubrik
    plt.ylabel('Antal spelare') #y-axel rubrik
    ax = plt.gca() #Hämtar axlar
    ax.spines['right'].set_visible(False) #Tar bort höger spine
    ax.spines['top'].set_visible(False) #Tar bort överste spine
    plt.bar(x, y, color = 'orange') #orange staplar
    plt.yticks(range(0, max(y)+1, 1)) #y-axeln ska gå upp till max-antal spelare, ersätter plt.ylim
    print(f"Stäng diagrammet för att återgå till menyn")
    plt.show() #Visa diagrammet 

#HUVUDPROGRAM
def main():
    skapa_fil_om_den_saknas()
    while True:
        alternativ = meny_val()
        if alternativ == 1:
            spela_skattjakten()
        elif alternativ == 2:
            visa_topplista()
        elif alternativ == 3:
            visa_diagram()
        elif alternativ == 4:
            print(f"Tack för att du spela! Resultatet är sparat i filen: {filnamn}")
            break
main()