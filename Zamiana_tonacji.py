print()
print("//Zamiana tonacji akordów podstawowych zapisanych w notacji Polskiej//")
dur = ["C", "Cis", "D", "Dis", "E", "F", "Fis", "G", "Gis", "A", "B", "H"]
mol = ["c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "b", "h"]
licz = 0
x = int(input("Podaj ilość akordów: "))
i = 0
tab = []
while i < x:
    print("Akord", i + 1, end="")
    z = str(input(": "))
    tab.append(z)
    i += 1
print("Twoje akordy: ")
i = 0
while i < x:
    print(tab[i], end="")
    if i != x - 1:
        print(", ", end="")
    i += 1
print()
print()
tab2 = tab
while licz != 5:
    print()
    print("-" * 50)
    print("Zmniejsz o 1 ton     -   wybierz 1")
    print("Zmniejsz o 0.5 tonu  -   wybierz 2")
    print("Zwiększ  o 0.5 tonu  -   wybierz 3")
    print("Zwiększ  o 1 ton     -   wybierz 4")
    print("Aby zakończyć            wybierz 5")
    licz = int(input("Podaj swój wybór: "))
    if licz == 1:
        a = 0
        moj = 0
        while moj < x:
            i = 0
            while i < 12:
                if tab2[moj] == dur[i]:
                    if i - 2 >= 0:
                        tab2[moj] = dur[i - 2]
                        break
                    else:
                        tab2[moj] = dur[i + 10]
                        break
                elif tab2[moj] == mol[i]:
                    if i - 2 >= 0:
                        tab2[moj] = mol[i - 2]
                        break
                    else:
                        tab2[moj] = mol[i + 10]
                        break
                i += 1
            moj += 1
        print()
        print("Twoje akordy zmniejszone o 1 ton:")
        j = 0
        while j < x:
            print(tab2[j], end="")
            if j != x - 1:
                print(", ", end="")
            j += 1
    elif licz == 2:
        a = 0
        moj = 0
        while moj < x:
            i = 0
            while i < 12:
                if tab2[moj] == dur[i]:
                    if i - 1 >= 0:
                        tab2[moj] = dur[i - 1]
                        break
                    else:
                        tab2[moj] = dur[i + 11]
                        break
                elif tab2[moj] == mol[i]:
                    if i - 1 >= 0:
                        tab2[moj] = mol[i - 1]
                        break
                    else:
                        tab2[moj] = mol[i + 11]
                        break
                i += 1
            moj += 1
        print()
        print("Twoje akordy zmniejszone o 0.5 tonu:")
        j = 0
        while j < x:
            print(tab2[j], end="")
            if j != x - 1:
                print(", ", end="")
            j += 1
    elif licz == 3:
        a = 0
        moj = 0
        while moj < x:
            i = 0
            while i < 12:
                if tab2[moj] == dur[i]:
                    if i + 1 <= 11:
                        tab2[moj] = dur[i + 1]
                        break
                    else:
                        tab2[moj] = dur[0]
                        break
                elif tab2[moj] == mol[i]:
                    if i + 1 <= 11:
                        tab2[moj] = mol[i + 1]
                        break
                    else:
                        tab2[moj] = mol[0]
                        break
                i += 1
            moj += 1
        print()
        print("Twoje akordy zwiększone o 0.5 tonu:")
        j = 0
        while j < x:
            print(tab2[j], end="")
            if j != x - 1:
                print(", ", end="")
            j += 1
    elif licz == 4:
        a = 0
        moj = 0
        while moj < x:
            i = 0
            while i < 12:
                if tab2[moj] == dur[i]:
                    if i + 2 <= 11:
                        tab2[moj] = dur[i + 2]
                        break
                    else:
                        tab2[moj] = dur[i - 10]
                        break
                elif tab2[moj] == mol[i]:
                    if i + 2 <= 11:
                        tab2[moj] = mol[i + 2]
                        break
                    else:
                        tab2[moj] = mol[i - 10]
                        break
                i += 1
            moj += 1
        print()
        print("Twoje akordy zwiększone o 1 ton:")
        j = 0
        while j < x:
            print(tab2[j], end="")
            if j != x - 1:
                print(", ", end="")
            j += 1
    elif licz == 5:
        print("//Zakończono działanie programu//")
        print("-" * 50)
        exit(1)