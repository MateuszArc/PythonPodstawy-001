Tax2 = (2, 6, 9, 55)

print(Tax2[-1])
print(Tax2.index(9))
print(Tax2.count(2))
print(max(Tax2))

#print(Tax2.revert())
TaxList2 = list(Tax2)
TaxList2.append(99)

NewTax2 = tuple(TaxList2)

print(Tax2)
print(TaxList2)
print(NewTax2)

(tax1, tax2, tax3, tax4) = Tax2
print(tax1, tax2, tax3, tax4)

a = 2
b = 20
print("a =", a, "\tb = ", b)

#temp = a
#a = b
#b = temp

(a,b) = (b,a)

print("a =", a, "\tb = ", b)