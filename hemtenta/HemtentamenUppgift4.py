# Tentamen 2025-08-18 -- 19
print("Uppgift 4 (4)\n")
# Skriv din kod nedan

# Kollar vilken utskrift ska skrivas ut
def fizz_buzz(end, fizz, buzz):
    # Modulo (%) används i denna loop för att 
    # kolla ifall siffran i är jämt delbart
    # med våra fizz och buzz siffror
    for i in range(1, end + 1):                 # Intervallet täcker till och med slutsiffran som användaren ger
        if i % fizz == 0 and i % buzz == 0:     # Hanterar detta först för att säkerställa att rätt utskrift skrivs ut om det uppfyller båda krav för "FizzBuzz"
            print("FizzBuzz")
        elif i % fizz == 0:
            print("Fizz")
        elif i % buzz == 0:
            print("Buzz")
        else:
            print(i)

# main()-funktionen hanterar input som ints och inte strängar
def main():
    end = int(input("Skriv ett slutvärde: "))
    fizz = int(input("Vilket tal ska ge Fizz?: "))
    buzz = int(input("Vilket tal ska ge Buzz?: "))

    fizz_buzz(end, fizz, buzz)

main()                                          # kör main()-funktionen