# Tentamen 2025-08-18 -- 19
print("Uppgift 5 (4)\n")
# Skriv din kod nedan
import datetime

# Använder datetime för att hämta ut veckodagen på engelska
def birthday(year, month, date):
    bday = datetime.datetime(year, month, date)
    return bday.strftime("%A")                                  # strftime() returnerar en sträng och "%A" returnerar hela veckodagen

# Kollar vilken dag vi ska översätta från engelska till svenska
def swe_translate(day):
    if day == "Monday":
        return "måndag"
    elif day == "Tuesday":
        return "tisdag"
    elif day == "Wednesday":
        return "onsdag"
    elif day == "Thursday":
        return "torsdag"
    elif day == "Friday":
        return "fredag"
    elif day == "Saturday":
        return "lördag"
    else:
        return "söndag"

# main()-funktionen hanterar input som ints
def main():
    year = int(input("Vilket år är du född? "))
    month = int(input("Vilken månad (1–12)? "))
    date = int(input("Vilken dag? "))
    birthday_eng = birthday(year, month, date)                  # Anropar en funktion som hämtar ut veckodagen på engelska
    birthday_swe = swe_translate(birthday_eng)                  # Anropar en funktion som kommer översätta veckodagen till svenska
    print(f"Du föddes på en {birthday_swe}.")
main()                                                          # kör main()-funktionen