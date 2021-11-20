# Írj programot, mely beolvas egy pozitív egész számot, és kiírja az egész számokat egymás alá a képernyőre eddig a számig!

szam=int(input("Adj meg egy számot és én kiírom Neked az egész számokat az Általad megadott számig bezárólag!"))
print(szam)

for int in range(szam):
    if (szam//1!=0):
        print(int)