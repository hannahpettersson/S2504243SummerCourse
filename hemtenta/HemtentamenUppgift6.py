# Tentamen 2025-08-18 -- 19
print("Uppgift 6 (4)\n")
# Skriv din kod nedan
import matplotlib.pyplot as plt

def total_savings(year, every_year, percent):
    savings_list = []                                                       # En tom lista för alla besparingar varje år
    amount = 0                                                              # Nuvarande beloppet av besparingarna
    increase = 1 + (percent / 100)                                          # Ökningen av besparingarna varje år

    # For-loopen räknar ut besparingarna för varje år
    # och appendar det till listan savings_list
    for i in range(1, year + 1):
        amount = (every_year + amount) * increase                           # Grundbeloppet (every_year) summeras med föregående årets besparingar (amount) och sedan multipliceras med ökningen (increase)
        savings_list.append(amount)
    return savings_list

# main()-funktionen hanterar input som ints
def main():
    years = int(input("Hur många år vill du spara? "))
    every_year = int(input("Hur mycket vill du spara varje år? "))
    percent = int(input("Hur många procent stiger aktien per år? "))
    savings_list = total_savings(years, every_year, percent)                # Anropar funktionen som returnerar en lista med ökningar för varje år

    plt.plot(range(1, years + 1), savings_list, marker = 'o')               # Plottar grafen mellan år 1 och sista året (x-värdet) samt motsvarande y-värde från savings_list och plottas med en cirkelmarkering
    plt.xlabel("År")
    plt.ylabel("Totalt värde (kr)")
    plt.title("Utveckling av aktiesparande")
    plt.xticks(range(1, years + 1))                                         # Intervallet för x-axeln
    plt.show()

main()                                                                      # Kör main()-funktionen