import os
import sys
try:
    line = str(input("Podaj cenę kolejnego kursu na udemy: "))
    path = input("Podaj ścieżkę do pliku: ")
    with open("last_file.txt", "w", encoding="UTF-8") as last:
        last.append(line)
    value = int(line)
    print("The value saved file is...")
except FileNotFoundError as FNFE:
    print("Error opening file.", FNFE)
except ValueError as VError:
    print("The value entered cannot be converted to a number.", VError)
except:
    print("SORRY, WE HAVE AN ERROR:", sys.exc_info())
else:
    print("Actions completed successfully")