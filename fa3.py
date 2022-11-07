import random

def menu():
    keuze = int(input('1: Ik wil weten hoeveel kluizen nog vrij zijn \n'
                      '2: Ik wil een nieuwe kluis \n'
                      '3: Ik wil even iets uit mijn kluis halen \n'
                      '4: Ik geef mijn kluis terug \n'
                      'Voer hier je keuze in: '))
    return keuze

#er zijn in totaal 12 kluisjes
#lezen van teksbestand met kluisjes
#uit bestand halen hoeveel kluisjes bezet zijn
#vrije kluisjes is dus 12 - aantal bezette kluisjes

def aantal_kluizen_vrij():

     kluisnr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
     aantalkluizen = 12
     infile = open('fa_kluizen.txt', 'r')
     lineList = infile.readlines()

     for line in lineList:
         # print(line, end='')
         aantalkluizen = aantalkluizen - 1
     infile.close()

     print(f"\nEr zijn {aantalkluizen} kluizen vrij")
     return aantalkluizen


#lijst aanmaken met kluisnr
#tekstfile uitlezen met infile
#kluisnummer laten invoeren en foutmelding geven als kluis niet beschikbaar is
#code laten invoeren en foutmelding geven als code fout is
#de nieuwe kluis met code in fa_kluizen.txt registreren

def nieuwe_kluis():
    kluisnr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    infile = open('fa_kluizen.txt', 'r')
    kar1 = infile.readlines()
    for line in kar1:
        nr = line.split(';')
#        print(nr)
        if nr[0] in kluisnr:
            kluisnr.remove(nr[0])
    infile.close()

    if len(kluisnr) == 0:
        print(f"Er zijn geen kluizen meer beschikbaar")
        return -2
    else:
        print(f"De beschikbare kluisnummers zijn {kluisnr}")


        kluisnr = random.choice(kluisnr)
        print(f"\nJe nieuwe kluisnummer is {kluisnr}")

        code = input('Maak een pincode voor de kluis: ')
        if len(code) < 4:
            print('Voer een code van minstens 4 tekens in')
            return -1
        elif ';' in code:
            print("Voer een code in zonder gebruik te maken van ';'")
            return -1
        else:
            print(f"Je nieuwe kluis is kluisnummer: {kluisnr} met code: {code} ")

    outfile = open('fa_kluizen.txt', 'a+')
    outfile.write("\n" f"{str(kluisnr)};{str(code)}")
    outfile.close()


    return 1
#lezen kluizen
#gebruiker kluisnr laten invullen
#wachtwoord laten invullen
#melding geven als ww goed of fout is


def kluis_openen():
     infile = open('fa_kluizen.txt', 'r')
     lineList = infile.readlines()
     while True:
         try:
             kluisnummer = int(input("Wat is je kluisnummer?: "))
         except ValueError:
             print("Voer een geldig getal in")
         else:
             break
     code = (input('Voer je code in: '))
     for line in lineList:
         if (str(kluisnummer) + ';' + (code) + '\n') == line:
             wachtwoordGoed = 1
             break
         else:
             wachtwoordGoed = 0
     if wachtwoordGoed == 1:
         print(line)
         print((str(kluisnummer) + ';' + (code) + '\n'))
         print('De kluis is geopend')
     else:
         print('Het wachtwoord is fout')
     return 1

#hoofdprogramma
#geeft keuzemenu
#als keuze = 1 geef aantal vrije kluizen
#als keuze = 2 geef functie voor nieuwe kluis
#als keuze = 3 geef functie voor kluis openen

keuze = menu()
if keuze == 1:
    aantal_kluizen_vrij()
if keuze == 2:
    nieuwe_kluis()
if keuze == 3:
    kluis_openen()