def Task4 () :


    n = eval(input("Unesite cijeli broj n: "))


    if not isinstance (n,int):
        print("Broj nije cijeli")
        quit()

    if not n>0:
        print("Broj nije pozitivan")
        quit()


    suma = 0
    for i in range (1,n,2):
        suma += i**2

    return suma

print(Task4())