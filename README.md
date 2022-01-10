# Aplikacja webowa typu "translator"
## Programowanie usług w chmurze

Autorzy:
- Rafał Latoszek 317718
- Joanna Borowska 291059
- Justyna Łapińska 291086
- Karol Stasiak 291107
- Dzmitry Kaliada 293642

## Cel projektu
Celem projektu było wykonanie kompletnego przykładu prostego systemu, który może składać się z gotowych usług, usług napisanych przez studentów oraz aplikacji, która wykorzystuje usługi w chmurze. System miał być uruchomiony na wybranej platformie chmurowej jako PaaS (Platform as a Service).

## Wymagania wstępne
### Tematyka projektu
Jako temat projektu została wybrana aplikacja webowa typu “translator”. Ma ona w ogólności pozwalać użytkownikowi na translację wprowadzonego tekstu, analizę tekstu oraz konwersję tekstu na mowę.
<br>
Szczegółowe wymagania dotyczące funkcjonalności zostały zebrane w zbiór przypadków użycia, przedstawiony na poniższym diagramie. 
### Założenia funkcjonalne
![alt text](https://github.com/borowskj/PUCH/blob/master/images/use_cases2.png?raw=true)

Użytkownik ma mieć możliwość przetłumaczenia wprowadzonego tekstu na wybrany język. Język tłumaczenia powinien zostać automatycznie wykryty przez system. Dla przetłumaczonego tekstu powinna zostać dostarczona opcja wygenerowania i odsłuchania odczytu tekstu. Kolejną umożliwioną funkcjonalnością będzie analiza nastrojów tekstu, która daje odpowiedź, czy wydźwięk tekstu jest pozytywny, negatywny, neutralny lub mieszany. W tym przypadku ponownie możliwa będzie autodetekcja języka. System ma także pozwolić na wykrycie tekstu z podanego obrazu z opcjami detekcji języka i odczytu tekstu.

### Założenia niefunkcjonalne
Aplikacja ma być hostowana na platformie Azure i być dostępna pod wybranym adresem działającym z poziomu przeglądarki. Funkcjonalność tłumaczenia i analizy tekstu oraz konwersja tekstu na mowę ma być dostarczona przy użyciu gotowych usług udostępnianych przez Azure Cognitive Services.

## Aplikacja
### Architektura
W obrębie systemu zostały wyróżnione moduły przedstawione na diagramie architektury.
![alt text](https://github.com/borowskj/PUCH/blob/master/images/architecture2.png?raw=true)

- <strong>App Services</strong> - moduł Microsoft Azure wykorzystany do wystawienia aplikacji, składający się z backendu i wbudowanego frontendu, napisana w języku Python, przy użyciu frameworka Flask, wdrożona na platformie Azure. Odpowiada za renderowanie widoków w postaci templatów HTML, obsługę akcji generowanych przez użytkownika oraz wykonywanie zapytań i przetwarzanie odpowiedzi pozwalajacych na dostarczenie wybranej funkcjonalności. W ramach aplikacji wykorzystywany jest moduł Cognitive Services.
- <strong>Cognitive Services</strong> - zbiór gotowych usług opartych na chmurze dostarczanych przez Microsoft Azure z udostępnionym API REST i zestawami bibliotek klienckich, które ułatwiają wbudowanie analizy poznawczej w tworzonych aplikacjach. Serwisy te pogrupowane są w pięć kategorii, z których w projekcie zostaną wykorzystane moduły dotyczące języka, mowy i przetwarzania obrazów.
- <strong>Computer vision</strong> - usługa sztucznej inteligencji służąca do analizowania zawartości obrazów i filmów wideo. W projekcie wykorzystywana jest funkcja wyodrębniania z obrazów tekstu drukowanego i pisanego w różnych językach (OCR). 
- <strong>Language</strong> - usługa należąca do Cognitive Service for Language, która zapewnia funkcje przetwarzania języka naturalnego (NLP) do rozumienia i analizowania tekstu. Użyta w projekcie funkcja analizy opinii pozwala na automatyczne wykrywanie tonacji i opinii z tekstu.
- <strong>Translators</strong> - usługa neuronowego tłumaczenia maszynowego, która jest częścią rodziny Cognitive Service for Language. Serwis umożliwia wykonanie tłumaczenia tekstu między obsługiwanymi językami źródłowymi i docelowymi w czasie rzeczywistym. Możliwe jest wykrycie i translację ponad 100 obsługiwanych języków.
- <strong>Speech services</strong> - usługa działająca w ramach Cognitive Service for Speech, które dostarczają funkcjonalności obsługi głosu. Wykorzystywana jest opcja konwersji tekstu na mowę z możliwością wyboru języka.

### Struktura plików
W ramach implementacji kod aplikacji został podzielony na poniższe pliki:
- <em>app.py</em> - główny plik zawierający konfigurację aplikacji oraz definicję obsługi wykonywanych zapytań wykorzystującej funkcje odpowiedzialne za poszczególne funkcjonalności,
- <em>extract.py</em> - plik przechowujący definicję funkcji <em>extractTextFromImage</em>, pozwalającej na utworzenie zapytania do serwisu Azure zwracającego wyodrębniony tekst z obrazu podanego jako argument funkcji,
- <em>sentiment.py</em> - plik określający definicję  funkcji <em>get_sentiment</em>, która generuje zapytanie do odpowiedniego serwisu Azure zwracającego wykonaną analizę nastrojów tekstu,
- <em>synthesize.py</em> - plik zawierający definicję klasy <em>TextToSpeech</em> oraz jej metod <em>get_token</em> i <em>save_audio</em>, odpowiadającej za wykonanie zapytania do serwisu Azure,  zwracającego dźwięk z wymową tekstu podanego razem z wybranym rodzajem głosu jako parametry funkcji.
- <em>translate.py</em> - plik z definicją funkcji <em>get_translation</em> generującej zapytanie o tłumaczenie podanego tekstu na wybrany język.

## Konfiguracja 
Integracja aplikacji internetowej z usługami kognitywnymi Azure Cognitive Services wymagała stworzenia i skonfigurowania czterech osobnych zasobów. Każdy z nich odpowiada wykorzystywanym usługom tj. Computer Vision, Language, Translators, Speech Services. We wszystkich przypadkach udało się zastosować darmowe plany Azure.  Aplikacja webowa komunikuje się z niniejszymi modułami poprzez udostępniane API. W celu autentykacji konieczne jest podanie <em>subscription key</em> oraz <em>location</em> w nagłówkach wysyłanego do Azure żądania.
<br>
Konfiguracja usług:
- Computer Vision Service
  ![alt text](https://github.com/borowskj/PUCH/blob/master/images/computer-vision-service-config.png?raw=true)
- Language Service
  ![alt text](https://github.com/borowskj/PUCH/blob/master/images/language-service-config.png?raw=true)
- Translator Service
  ![alt text](https://github.com/borowskj/PUCH/blob/master/images/translator-service-config.png?raw=true)
- Speech Services
  ![alt text](https://github.com/borowskj/PUCH/blob/master/images/speech-service-config.png?raw=true)

Po ukończeniu prac deweloperskich aplikacja została opublikowana za pomocą modułu Azure App Services. Proces deployment’u ułatwiło zastosowanie rozszerzenia do Visual Studio Code: Azure App Service. <br>
![alt text](https://github.com/borowskj/PUCH/blob/master/images/vs-project.png?raw=true) <br>
<br>Konfiguracja usługi App Service:
![alt text](https://github.com/borowskj/PUCH/blob/master/images/web-app-config.png?raw=true) <br>
Finalna wersja aplikacji jest dostępna pod adresem: <https://app-translator-2.azurewebsites.net/>

## Przebieg prac
Prace nad projektem rozpoczęto od analizy wymagań, która została podsumowana diagramem przypadków użycia. Następnym etapem było zapoznanie z dostępnymi na rynku rozwiązaniami oraz wybór technologii, w wyniku czego powstał zamysł architektury aplikacji.<br>
Jako narzędzie wspierające zarządzanie zadaniami i śledzenie postępu prac została wybrana platforma Github Projects. Udostępniona funkcjonalność Issues umożliwiła podział niezbędnej do wykonania pracy na osobne zadania, przypisane do poszczególnych członków projektu. Dodatkowo zadania miały przypisane etykiety zgodnie z kategorią, której dotyczyły. W narzędziu możliwe jest także powiązanie zadań z dołączanymi zmianami, zorganizowanymi poprzez system kontroli wersji.
Praca zorganizowana była w postaci regularnych workshopów, na których zespół wspólnie omawiał aktualny stan i możliwe do zastosowania pomysły. Początkowo rozplanowane zadania w ramach projektu były następnie rozbudowywane w miarę ustalania się zakresu i wybranych rozwiązań. Członkowie zespołu wykonywali zadania  z różnych kategorii, aby móc poznać wszystkie kwestie związane z usługami chmurowymi.
## Działanie aplikacji
Zakres finalnej wersji aplikacji jest zgodny z założeniami przedstawionymi na pierwszym przeglądzie projektu oraz powyższym diagramem przypadków użycia.<br>
Użytkownik ma dostęp do wszystkich opcji projektu z poziomu strony głównej aplikacji webowej, na której znajduję się formularz danych wejściowych oraz formularz z wynikami translacji.
<br> <br>
Krótka prezentacja funkcjonalności aplikacji: <https://youtu.be/dBikeQEQ8Ys>
