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
        print(True)
    elif animal == 'bear':    
        print(txt_bear)
        print(True)
    elif animal == 'bat':
        print(True)
        print(txt_bat)
    elif animal == '':
        animal = ''
        print(False)    
    else:
        print("Cannot print %s. Correct values for animal is: cat, bat or bear." % animal)
        print(False)    
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
        return delta.days
     
print('Date: 2020-12-20 days to end of year: %d' %( DaysToEndOfYear(2020,12,20)))
     
print('Date: 2020-12-21 days to end of year: %d' %( DaysToEndOfYear(2020,12,21)))
     
print('Date: TODAY days to end of year: %d' %( DaysToEndOfYear()))