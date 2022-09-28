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
    return

PrintAnimal()
print("-----------------------------------------")
def DaysToEndOfYear(year, month, day):
    from datetime import date
     
    date_today = date(year,month,day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)
     
DaysToEndOfYear(2020,12,20)
DaysToEndOfYear(2021,12,21)
DaysToEndOfYear(year = 2022, month = 12, day = 22)
DaysToEndOfYear(day = 23, month =12, year = 2023)