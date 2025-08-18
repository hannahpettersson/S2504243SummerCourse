# Tentamen 2025-08-18 -- 19
print("Uppgift 1 (2)\n")
# Skriv din kod nedan

# Räknar och returnerar längden av listan som är given från sentence.split() 
def word_count(sentence):
    return len(sentence)

# Räknar alla karaktärer som finns i listan utan alla mellanslag
def character_count(sentence):
    count = 0                                                                   # En tom counter för antal bokstäver
    delimiter = ' '                                                             # Mellanslaget som vi ska bortse ifrån

    # Loopar igenom alla karaktärer i strängen och räknar
    # alla mellanslag
    for i in sentence:
        if i != delimiter:                                                      # Om nuvarande karaktär inte är ett mellanslag så utökas countern
            count += 1
        else:                                                                   # Annars fortsätter vi till nästa karaktär i strängen
            continue
    return count

# main()-funktionen hanterar input
def main():
    sentence = input("Skriv en mening: ")
    print(f"Antal ord: {word_count(sentence.split())}")                         # .split() tar bort alla mellanslag och returnerar en lista med alla ord i meningen
    print(f"Antal bokstäver (utan mellanslag): {character_count(sentence)}")

main()                                                                          # kör main()-funktionen