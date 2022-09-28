import os
import time

dir = input("Wprowadź ścieżkę dostępu do katalogu:")
if not os.path.isdir(dir):
    print("Napis nie wskazuje na katalog!")
else:
    file = input("Podaj nazwę pliku:")
    path = os.path.join(dir, file)
    if not os.path.isfile(path):
        print("plik wskazywany przez path nie istnieje", path)
    else:
        print("Poniżej będą wyświetlane właściwości pliku path:")
        print("\nData ostatniej modyfikacji:",os.path.getmtime(path))
        print("\nRozmiar pliku w bitach:", os.path.getsize(path))
        print('Bieżący katalog: ', os.getcwd())
        print('Ścieżka względna do pliku:', os.path.relpath(path))