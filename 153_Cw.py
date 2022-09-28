def PrintAnimal():
    
        # this function prints a cat ascii-art
    txt_cat = r'''
    |\---/|
    | o_o |
     \_^_/'''
        

    
    # this function prints a bear ascii-art
    txt_bear = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
    


    # this function prints a bat ascii-art
    txt_bat = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/  
         '''
    
    animal = input("Choose pet to print: cat, bear, bat: ")    
    
    if animal == 'cat':    
        print(txt_cat)
    elif animal == 'bear':    
        print(txt_bear)
    elif animal == 'bat':
        print(txt_bat)
    elif animal == '':
        animal = ''    
    else:
        print("Cannot print %s. Correct values for animal is: cat, bat or bear." % animal)
    return

PrintAnimal()
print("-----------")

from datetime import date
     
def DaysToEndOfYear(year = date.today().year,
                        month = date.today().month,
                        day = date.today().day):
        
        date_today = date(year,month,day)
        date_end_year = date(year, 12, 31)
        delta = date_end_year - date_today
        print('Counting from ', date_today,'days remaining', delta.days)
     
DaysToEndOfYear(2020,12,20)
DaysToEndOfYear(day = 23, month =12, year = 2023)
DaysToEndOfYear()
DaysToEndOfYear(year=2020)
DaysToEndOfYear(year=2020, month=10)
DaysToEndOfYear(day=1)


