getal = int(input("geef een getal"))

#opdracht 1
if getal >= 0:
    print("positief")
    total = 0
    while getal > 1:
        getal -= 1
        total += getal
    print("totaal =" + str(total))
else:
    print("negatief")

#opdracht 2
getal = int(input("geef een getal"))
deeltal = getal

while deeltal >= 1:
    if getal % deeltal == 0:
        print(deeltal)
    deeltal -= 1

#opdracht 3
doing_input = True
offer_list = []

while doing_input:
    #extra, kan je gebruiken om zaken die je app crashen op te vangen
    #code die je probeert uit te voeren
    try:
        offer = float(input("geef een offerteprijs:"))
        if offer > 0:
            offer_list.append(offer)
        elif offer == -1:
            doing_input = False
        else:
            print("prijs mag niet negatief zijn!")
    #error (crash) die je wenst op te vangen
    #error naam is wat je in het rood in je console ziet
    except ValueError:
        print("ongeldige invoer")

try:
    total = 0
    for price in offer_list:
        total += price

    avg = total / len(offer_list)
    print("Bedankt! De gemiddelde prijs is: " + str(avg))
except ZeroDivisionError:
    print("Minstens 1 offerte nodig voor een gemiddelde")
