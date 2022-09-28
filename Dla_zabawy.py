user = input("Nazwa użytkownika: ")
print("Witaj", user, "w MatSmart! To mobilna aplikacja. zaraz będziesz musiał wpisać hasło, aby wypróbować możliwości programu!")
        
password = "MatArc3b2022@Mine.pl"
password = input("Wpisz hasło:")
while password != password:
    if password == password: 
            print("hasło zaakceptowane!")
            break
print(("Wysyłam cię do lobby!"))
lobby = input("Napisz coś: ")
while lobby != '':
    aplications = ["Asystent Mat", "MatAps"]
    lobby = input("Co mam zrobić: 1 - Otwórz MatAps i zainstaluj aplikację, 2 - usuń aplikację 3 - włącz jakąś aplikację, 4 - Wyświetl moje aplikacje. A jeśli chcesz wyłączyć program, nic nie wpisz i naciśnij enter: ")
    if lobby == '1':
        print("Włączam MatAps!")
        MatApsLobby = "FFFF"
        while MatApsLobby != "":
            MatApsLobby = input("Witaj w MatAps. Tutaj możesz zainstalować aplikację do swojego urządzenia. Jaki rodzaj aplikacji chcesz wybrać: 1 - Gry,czy 2 - narzędzia Jeśli chcesz wyjść, to zostaw pusty napis:")
            if MatApsLobby == "1":
                print("Pokazuję gry:")
                a = input("Wybierz: 1 - Zgadnij Liczbę")
                if a == "1":
                    print("Ok. Aby wyjść po tej wiadomości naciśnij enter!")
                    aplications.append(a)