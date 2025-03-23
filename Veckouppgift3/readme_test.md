https://playwright.dev/docs/other-locators

## User story [U1] - Verify "Add timer" button
Som användare vill jag kunna se att knappen "Add timer" är synlig 
och kan klickas. Så att man är redo att ställa en timer.

## Acceptanskriterier [A1]
###[A1.1] När jag klickar på knappen "Add timer", ska en timer skapas på skärmen.

## Testscenario [T1]
###[T1.1] Navigera till webbsidan.
###[T1.2] Kontrollera att knappen "Add timer" finns och kan klickas

# -----------------------------------------------

### User story [U2] - kunna interagera med funktionen för knappen "add timer"
Som användare vill jag kunna se att timern startar från 15:00 
och att den kan startas eller återställas. 
Så att jag kan starta samt nollställa en timer.

### Acceptanskriterier [A2]
[A2.1] Timern ska starta från 15:00.
[A2.2] När man klickar på "Start" börjar timern räkna ner.
[A2.2] När man klickar på "Reset" ska timern återställas till 15:00.

### Testscenario [T2] – Timer-interaktioner
[T2.1] Kontrollera att timern visas korrekt på sidan efter att du har klickat på knappen "Add timer".
[T2.2] Kontrollera att timern startar från 15:00.
[T2.3] Klicka på "Start" och kontrollera att timern startar nedräkning.
[T2.4] Klicka på "Reset" och kontrollera att timern återställs till 15:00.

# -----------------------------------------------

### User story [U3] 
Som användare vill jag kunna se att knappen 'Add note' är synlig
och kan klickas. Så att man är redo att göra en note.

### Acceptanskriterier[A3]
[A3.1] När jag klickar på knappen, ska en text "Click to change text" visas på skärmen.

### Testscenario [T3]
[T3.1] Navigera till webbsidan.
[T3.2] Kontrollera att knappen "Add note" finns och kan klickas

# -----------------------------------------------

### User story [U4] - kunna interagera med funktionen för knappen "add note"
Som användare vill jag kunna se att knappen 'Add note' kan klickas och addera texter, spara, byta ordning på och radera notes. 
Så att jag själv kan påbörja en note spara, ändra, byta ordning samt radera densamma.

###Acceptanskriterier[A4]
[A4.1] Det ska vara möjligt att klicka på rutan med texten "Click to change text"
och ändra innehållet.
[A4.2] När man trycker "Enter", sparas texten.
[A4.3] När man trycker på korgen, suddas texten bort.
[A4.4] Genom att trycka på pilarna ska man kunna ändra ordning på sina notes.

### Testscenario [T4] – Kontrollera att knappen 'Add note', addera och delete note!
[T4.1] Navigera till webbsidan.
[T4.2] klicka på knappen "Add notes"
[T4.3] Klicka/markera textrutan "Click to change text" 
[T4.4] Interagera/markera input fältet och skriv texten "TEST T4.4"
[T4.5] klicka med "Enter" för att spara
[T4.6] Kontrollera att texten har ändrats till "Test T4.4"
[T4.7] Enligt samma scenario från (T4.2 - T4.6) och fyll i en ny ruta med texten "TEST T4.7" samt kontrollera att det gjorts.
[T4.8] Testa att ändra ordningen på de två texterna samt kontrollera att det gjorts
[T4.9] Testa att radera med "close button", samt kontrollera att det gjorts

