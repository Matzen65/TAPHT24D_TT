"""
1a. Svar: C
    identisk kombination ab

1b. Svar: nisse
    case insensitive

1c. Svar: a, b och d
    *n tar med alla n

1d. Svar: B
    one of "ae-single character" followed by n
    [ae]n matchar alla "a eller e som följs av tecknet n.

1e. Svar: c och d
    punkt är som wildcard och matchar alla tecken utom radbyte. "+" upprepar föregående

1f. Svar: c och d
    \s matchar mellanslag, "?" matchar föregående tecken 0 eller flera ggr, kan alltså exkludera det helt.


1g Svar:
a. line eller lines
b. måste starta med "a" och sluta med "ö"
c. strängen måste innehålla ett eller flera tecken av [aeiouyåäö]
d. "\d" måste matcha en siffra mellan 1-9, "*" upprepar flera siffror, detta fall skulle även fungera med "[1]\d*"
e. Fungerar på ett datumformat typ XXXX-XX-XX

2a Betrakta https://lejonmanen.github.io/agile-helper/ . Skriv en user story som
beskriver att användaren ska kunna läsa hur man gör en "sprint retrospective".

Svar: Scenario:
Gå till sidan https://lejonmanen.github.io/agile-helper/
tryck på knappen "Last"
Tryck sedan på den knappen som har orden "...Sprint retrospective"
Ange ett textavsnitt som bör kvarstå över lång tid
Tryck på knappen "The sprint is complete"

3. Förstår när man läser koden och ser sidan intill, hade varit mkt svårare att själv programmera testet.


"""