#Nou enpote fonksyon k ap pemet nou jenere nonb aleyatwa a
from random import randrange

#Nou defini varyab n ap itilize yo
nonb_odinate = randrange(1, 100)
genyen = False
chans = 5

#Mesaj byenvini
print("Nan pwogram sa a, w ap gen chans devine yon nonb aleyatwa ant 1 a 100.")
print("Bòn chans\n\n")

#Nou jere lojik jwet la nan bouk sa a
while not genyen and chans > 0:
    print("Ou rete", chans, "chans pou w devine nonb la.")
    nonb_itilizate = int(input("Devine ki nonb odinate a chwazi: "))
    if nonb_itilizate == nonb_odinate:
        genyen = True
    elif nonb_odinate < nonb_itilizate:
        print("Nonb ou dwe devine a pi piti pase sa w antre a.\n\n")
    else:
        print("Nonb ou dwe devine a pi gran pase sa w antre a.\n\n")
    chans -= 1

if genyen:
    print("\n\nBravo, ou jwenn nonb la. Jan w di l la, se te:", nonb_odinate)
else:
    print("Malerezman ou pa rive devine nonb sekrè a. Se te :", nonb_odinate)