a=input("Podaj swoja liczbe A: ")
b=input("Podaj swoja liczbe B: ")
c=input("Podaj swoja liczbe C: ")
if (int(a)>0 and int(a)<=10) :
    if(int(a)>int(b)):
        print("A nalezy do przecialu i A>B")
    elif(int(b)>int(c)):
        print("A nalezy do przecialu i B>C")
    else:
        print("A nalezy do przecialu ale drugi warunek nei ejst spelniony")
else :
    print ("Oba warunki nie sa spelnione")