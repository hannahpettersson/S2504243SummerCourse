# Tentamen 2025-08-18 -- 19
print("Uppgift 7 (20p)\n")
import csv
import matplotlib.pyplot as plt

file_name = 'fuelprices_day_by_day.csv'

# Skriv din kod nedan
print("Uppgift 7a (3p)\n")
# Skriv din kod nedan

# En funktion som skriver ut en tvådimensionell lista
def twodim_list(filename):
    prices = []                                                                             # Huvudlistan som kommer innehålla listor för varje rad
    
    with open(filename, 'r') as file:                                                       # Öppnar filen med avseende på att läsa från filen med 'r'
        csv_reader = csv.reader(file, delimiter=';')                                        # Skapar en reader som ser till att det som skiljer på datan är en semikolon ';'

        for row in csv_reader:                                                              # Itererar genom varje rad i csv-filen
            sub_list = []
            for price in row:                                                               # Itererar mellan informationen på raden i csv-filen
                sub_list.append(price)                                                      # Lägger till nuvarande datan till sublistan
            prices.append(sub_list)                                                         # Lägger till listan för nuvarande rad till huvudlistan
    
    for row in prices[0:6]:                                                                 # Printar från 1:a indexen i listan till och med 6:e indexen - rubriken + 5 rader med info
        print(row)

# Funktionsanrop
twodim_list(file_name)

# -------
print("Uppgift 7b (5p)\n")
# Skriv din kod nedan

# En funktion som plottar utvecklingen av priset för respektive bensin
def price_development(filename):
    # Fyra listor som kommer innehålla data från respektive spalt i csv-filen
    dates = []
    bensin95 = []
    e85 = []
    diesel = []

    with open(filename, 'r') as file:                                                       # Öppnar filen med avseende på att läsa från filen med 'r'
        csv_reader = csv.reader(file, delimiter=';')                                        # Skapar en reader som ser till att det som skiljer på datan är en semikolon ';'
        next(csv_reader)                                                                    # Hoppar över första raden i csv-filen som är rubrikerna

        # Itererar igenom varje rad i csv-filen och lägger till datan i rätt lista
        # med avseende på vilket index de tillhör.
        # float() gör att vi lägger till en float, och inte en sträng in i listan
        for row in csv_reader:
            if "2021-09-01" <= row[0] <= "2021-10-15":                                      # Säkerställer att vi är inom rätt intervall för grafen
                dates.append(row[0])
                bensin95.append(float(row[1]))
                e85.append(float(row[2]))
                diesel.append(float(row[3]))
    
    
    plt.figure(figsize=(20,10))
    plt.plot(dates, bensin95, marker = 'o', label= 'Bensin 95')                             # Plottar kurvan för Bensin 95
    plt.plot(dates, e85, marker = 'o', label= 'E85')                                        # Plottar kurvan för E85
    plt.plot(dates, diesel, marker = 'o', label= 'Diesel')                                  # Plottar kurvan för Diesel
    plt.legend()                                                                            # Lägger till en legend till grafen och vad kurvorna motsvarar
    plt.xlabel("Datum")
    plt.ylabel("Pris [kr/liter]")
    plt.title("Prisutveckling på drivmedel under perioden 2021-09-01 -- 2021-10-15")
    plt.xticks(rotation = 90)                                                               # Roterar rubrikerna på x-axeln med 90 grader
    plt.show()

# Funktionsanrop
price_development(file_name)

# -------
print("Uppgift 7c (12p)\n")
# Skriv din kod nedan

# Hittar högsta värdet i en lista
def maximum(lst):
    largest = lst[0]
    for n in lst:
        if n > largest:                                                                     # Jämför om nuvarande talet, n, som finns i listan är större än största talet
            largest = n
    return largest

# Hittar lägsta värdet i en lista
def minimum(lst):
    lowest = lst[0]
    for n in lst:
        if n < lowest:                                                                      # Jämför om nuvarande talet, n, som finns i listan är lägre än lägsta talet
            lowest = n
    return lowest

# Hittar summan av en lista
def find_sum(lst):
    total = 0
    for n in lst:
        total += n
    return total

# Hittar medelvärdet av en lista
def average(lst):
    total = find_sum(lst)
    length = len(lst)
    return total / length

# Skapar en lista på alla möjliga intervaller från csv-filen
def p_interval():
    price_lst = []
    for i in range(9, 20):
        lower = i
        upper = i + 0.99
        interval = [lower, upper]                                                           # En lista med både över- och undergränserna till varje intervall
        price_lst.append(interval)
    return price_lst

# Skapar en lista med flera sublistor som innehåller alla värden inom respektive intervall
def price_interval_sort(bensin_lst, interval):
    interval_sorted_prices = []
    for i in range(len(interval)):
        lower_boundary = interval[i][0]                                                     # Index 0 i sublistan från interval-listan
        upper_boundary = interval[i][1]                                                     # Index 1 i sublistan från interval-listan
        current_boundary = []                                                               # Alla värden som ingår i nuvarande intvervall
        for j in bensin_lst:
            if lower_boundary <= j <= upper_boundary:                                       # Kollar om första värdet i listan är inom rätt intervall
                current_boundary.append(j)
        interval_sorted_prices.append(current_boundary)                                     # Lägger till nuvarande intervallet i en prislista för nuvarande bensin
    return interval_sorted_prices

# Räknar ut procenten av alla tal för denna intervall 
def percent(lst, interval):
    total = len(lst)                                                                        # Antal olika priser i bensinlistan
    interval_len = len(interval)                                                            # Längden av nuvarande intervall
    return (interval_len / total) * 100

# Hittar datumet då första priset inom intervallet uppstår
def find_first_date(price_lst, lst, fuel_idx, index):
    current_interval = lst[index]                                                           # Hämtar ut intervallet vi söker information ifrån med index                           
    if len(current_interval) == 0:                                                          # Om intervallet är tomt
        return '-'
    
    for row in price_lst:                                                                   # price_lst är en lista med varje rad från csv-filen
        if float(row[fuel_idx]) == current_interval[0]:                                     # Kollar om indexen på nuvarande rad är första siffran i current_interval
            return row[0]                                                                   # Returnerar datumet för den siffran

def development_table(filename):
    price_interval = p_interval()
    # Data listor som kommer innehålla data från respektive bensin spalt i csv-filen
    bensin95 = []
    e85 = []
    diesel = []

    rows = []                                                                               # Listan kommer innehålla varje rad i csv-filen

    with open(file_name, 'r') as file:                                                      # Öppnar filen med avseende på att läsa från filen med 'r'
        csv_reader = csv.reader(file, delimiter=';')                                        # Skapar en reader som ser till att det som skiljer på datan är en semikolon ';'
        next(csv_reader)                                                                    # Hoppar över första raden i csv-filen som är rubrikerna

        # Itererar igenom varje rad i csv-filen och lägger till datan i rätt lista
        # med avseende på vilket index de tillhör.
        # float() gör att vi lägger till en float, och inte en sträng in i listan
        for row in csv_reader:
            bensin95.append(float(row[1]))
            e85.append(float(row[2]))
            diesel.append(float(row[3]))
            rows.append(row)

    # Sorterar priserna för varje bensinsort inom olika intervaller
    bensin95_intervals = price_interval_sort(bensin95, price_interval)
    e85_intervals = price_interval_sort(e85, price_interval)
    diesel_intervals =price_interval_sort(diesel, price_interval)

    print("-------------------------------------------------------------------")
    print("PRISUTVECKLING PÅ DRIVMEDEL UNDER PERIODEN 2015-01-01 -- 2021-10-15")
    print("-------------------------------------------------------------------")

    # Dessa tre for-loopar loopar igenom varje prisintervall och skriver ut datan för dem
    print(f"Prisintervall [kr/liter]       % Bensin av mätperiod:          Datum:\n")
    for i in range(len(price_interval)):
        print(f"{price_interval[i]}                             {percent(bensin95, bensin95_intervals[i]):.2f}                  {find_first_date(rows, bensin95_intervals, 1, i)}") # datum först: 2015-01-01

    print(f"\nPrisintervall [kr,/liter]       % e85 av mätperiod:          Datum:\n")
    for i in range(len(price_interval)):
        print(f"{price_interval[i]}                             {percent(e85, e85_intervals[i]):.2f}                    {find_first_date(rows, e85_intervals, 2, i)}")

    print(f"\nPrisintervall [kr/liter]       % diesel av mätperiod:          Datum:\n")
    for i in range(len(price_interval)):
        print(f"{price_interval[i]}                             {percent(diesel, diesel_intervals[i]):.2f}                  {find_first_date(rows, diesel_intervals, 3, i)}")
    
    print()

def price_table():
    # Data listor som kommer innehålla data från respektive bensin spalt i csv-filen
    bensin95 = []
    e85 = []
    diesel = []

    with open(file_name, 'r') as file:                                                      # Öppnar filen med avseende på att läsa från filen med 'r'
        csv_reader = csv.reader(file, delimiter=';')                                        # Skapar en reader som ser till att det som skiljer på datan är en semikolon ';'
        next(csv_reader)                                                                    # Hoppar över första raden i csv-filen som är rubrikerna

        # Itererar igenom varje rad i csv-filen och lägger till datan i rätt lista
        # med avseende på vilket index de tillhör.
        # float() gör att vi lägger till en float, och inte en sträng in i listan
        for row in csv_reader:
            bensin95.append(float(row[1]))
            e85.append(float(row[2]))
            diesel.append(float(row[3]))
    
    # Lägsta-, högsta- samt medelpris på vardera bensinsort
    low_ben = minimum(bensin95)
    high_ben = maximum(bensin95)
    avg_ben = average(bensin95)

    low_e85 = minimum(e85)
    high_e85 = maximum(e85)
    avg_e85 = average(e85)

    low_diesel = minimum(diesel)
    high_diesel = maximum(diesel)
    avg_diesel = average(diesel)

    print(f"Bensin 95     [kr/liter]\
          \nHögsta pris:  {high_ben}\
          \nLägsta:       {low_ben}\
          \nMedelpris:    {avg_ben:.2f}\n")                                                     # .2f ger ett flyttal med 2 decimaler
    print(f"E85           [kr/liter]\
          \nHögsta pris:  {high_e85}\
          \nLägsta:       {low_e85}\
          \nMedelpris:    {avg_e85:.2f}\n")
    print(f"Diesel        [kr/liter]\
          \nHögsta pris:  {high_diesel}\
          \nLägsta:       {low_diesel}\
          \nMedelpris:    {avg_diesel:.2f}\n")

# Funktionsanrop
development_table(file_name)
price_table()
