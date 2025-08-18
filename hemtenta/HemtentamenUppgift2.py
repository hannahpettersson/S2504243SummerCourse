# Tentamen 2025-08-18 -- 19
print("Uppgift 2 (2)\n")
# Skriv din kod nedan

def reverse_stairs(number):
    # Yttre for-loopen hanterar tomrummen som ska skrivas ut innan sifforna
    for i in range(1, number + 1):
        to_print = ''

        #Inre for-loopen hanterar strängen med siffrorna som ska skrivas ut
        for j in range(1, i + 1):
            to_print += str(j)                                                  # Lägger till nuvarande siffran omvandlad till en sträng till to_print strängen
        
        current_space = ' ' * (number - i)                                      # En sträng med antal platser som representerar alla tomrum som ska skrivas ut
        print(f"{current_space}{to_print}")                                     # Skriver ut både tomrummen och strängen med siffrorna under denna iterationen


# main() funktionen hanterar input
def main():
    number = int(input("Välj ett heltal: "))
    reverse_stairs(number)

main()                                                                          # kör main()-funktionen
