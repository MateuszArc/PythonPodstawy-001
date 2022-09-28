def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()
a_int = input("a = ")
b_int = input("b = ")
c_int = input("c = ")

if not(check_int(a_int) or check_int(b_int) or check_int(c_int)):
    print("To nie są liczby całkowite! Kończymy za karę!")
else:
    a = int(a_int)
    b = int(b_int)
    c = int(c_int)
    if a == 0:
        print("To nie jest równanie kwadratowe! Kończymy za karę!")
    else:
        delta =  b**2 - 4*a*c
        if delta < 0:
            print("Brak rozwiazań!")
        elif delta == 0:
            x1 = x1 = -b/(2*a)
            print("Jest jedno rozwiązanie:", x1)
        elif delta > 0:
            x1 = (-b-delta**0.5)/(2*a)
            x2 = (-b+delta**0.5)/(2*a)
            print("Są dwa rozwiązania:",x1, "i", x2)