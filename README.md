# Projekt 2

# Instrukcja jak uruchomić aplikację

## Krok 1: Pobierz repozytorium z gita

Upewnij się, że masz zainstalowanego gita na swoim komputerze. Następnie otwórz terminal (lub wiersz poleceń) i wykonaj
poniższe polecenie, aby pobrać repozytorium:

```
git clone https://github.com/rajdun/projekt2.git
```

## Krok 2: Przejdź do folderu projektu

Przejdź do folderu z projektem za pomocą polecenia:

```
cd projekt2
```

## Krok 3: Utwórz wirtualne środowisko

Utwórz wirtualne środowisko, aby zainstalować wszystkie wymagane pakiety:

```
python -m venv venv
```

Aktywuj wirtualne środowisko:

Na systemie Windows:

```
venv\Scripts\activate
```

Na systemach Unix (Linux/MacOS):

```
source venv/bin/activate
```

## Krok 4: Zainstaluj wymagane pakiety

Zainstaluj wymagane pakiety z pliku requirements.txt:

```
pip install -r requirements.txt
```

## Krok 5: Uruchom migracje

Uruchom migracje, aby utworzyć strukturę bazy danych:

```
python manage.py migrate
```

## Krok 6: Wczytaj podstawowe dane

Wczytaj informacje o grupach i ich uprawnieniach.

```
python manage.py loaddata group_permissions.json
```

## Krok 7: Stwórz superusera

Stwórz superusera, aby mieć dostęp do panelu administracyjnego Django:

```
python manage.py createsuperuser
```

Podczas tworzenia superusera zostaniesz poproszony o podanie nazwy użytkownika, adresu e-mail i hasła.

## Krok 8: Uruchom serwer

Uruchom serwer Django za pomocą polecenia:

```
python manage.py runserver
```

## Krok 9: Otwórz stronę w przeglądarce

Serwer powinien działać na porcie 8000. Otwórz przeglądarkę i wpisz następujący adres:

```
http://localhost:8000
```

# Korzystanie z aplikacji

Za pomocą konta superusera można zalogować się na witrynę. Pojawi się panel administratora.
Można w nim skonfigurować profile użytkowników (m.in. ich stan konta), kartotekę towarów (Inventory), użytkowników i
grupy.

Żeby normalny użytkownik (nie administrator) mógł dodawać i edytować towary musi byćw grupie INVENTORY i trzeba na nim
zaznaczyć "W Zespole" w panelu administratora.
