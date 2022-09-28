from cmath import cos


text = 'To jest głupi tekst'
print(text.endswith('kst.'))
print(text.islower())
print(text.upper())
print(text.upper().isupper())
print(text.find('jest', 3))
print(text.replace('To', 'Xd').replace('jest głupi', 'hasta la vista, babe').replace('tekst', 'terminated'))
print(text.split(' '))
cosjakliczba = '200 673 730'
print(cosjakliczba.isdigit())
print(cosjakliczba.isdecimal())
print(cosjakliczba.isalpha())
print(cosjakliczba.isalnum())