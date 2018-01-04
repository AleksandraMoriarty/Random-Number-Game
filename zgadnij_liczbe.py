# To jest gra "Zgadnij jaka to liczba".
import random

wykonaneProby = 0

print('Czesc! Jak masz na imie?')
mojeImie = input()

liczba = random.randint(1, 20)
print('sluchaj, '+ mojeImie+'  mysle o liczbie z przedzialu od 1 do 20')

for wykonaneProby in range(6):
    print('Sprobuj odgadnac.')
    probaOdgadniencia = input()
    probaOdgadniencia = int(probaOdgadniencia)

    if probaOdgadniencia < liczba:
        print('twoja liczba jest za mala.')

    if probaOdgadniencia > liczba:
        print('Twoja liczba jest za duza')

    if probaOdgadniencia == liczba:
        break

if probaOdgadniencia == liczba:
    wykonaneProby = str(wykonaneProby +1)
    print('Swietna Robota'+mojeImie+ '! Udalo ci się zgadnonc w '+ wykonaneProby+'  Probach!')

if  probaOdgadniencia != liczba:
    liczba = str(liczba)
    print('Niestety nie udalo sie.To byla liczba '+liczba)
