https://playwright.dev/docs/other-locators

### Test Timer-Vue

### User story [U1] - Verify "Add timer" button
Som användare vill jag kunna öppna och stänga en widgets för en Timer 
och ta bort densamma.

### Acceptanskriterier [A1]
[A1.1] När jag klickar på knappen "Add timer", ska en timer skapas på skärmen.
[A1.2] När jag klickar på icon "Add timer" ska timern dyka upp
[A1.3] När jag klickar på icon för papperskorg ska Timern släckas

### Testscenario [T1]
[T1.1] Navigera till webbsidan. Verifiera att endast en widget har öppnats
[T1.2] Kontrollera att knappen "Add timer" finns och kan klickas,
[T1.3] Verifiera funktionen av knappen Erase och verifiera att nu är endast en widget öppen.


# -----------------------------------------------

### User story [U2] - kunna interagera med timer
Som användare vill jag kunna se att timern startar från 15:00 
och att den kan starta pausas samt återställas. 

### Acceptanskriterier [A2]
[A2.1] Timern ska starta från 15:00.
[A2.2] Testa att Start kan klickas, testa att paus och erase kan klickas

### Testscenario [T2] – Timer-interaktioner
[T2.2] kontrollera att timern startar med texten 15:00
[T2.2] kontrollera om Start/Paus är synliga och klickbara

#------------------------------------------------

### User story [U3] - Ändra på tiden i timer-inställning
Som användare vill jag kunna ändra tiden i timern.
Så att jag kan starta en bestämd nedräkning i timer.

[T3.1] Ändra tiden i textfönstret från 15:00 till "5:00" samt verifiera texten 5:00. 
kontrollera Reset till 15:00 samt avsluta med att stänga widgeten


# -----------------------------------------------

### User story [U4] 
Som användare vill jag kunna se att knappen 'Add note' är synlig
och kan klickas. Så att man är redo att göra en note.

### Acceptanskriterier[A4]
[A4.1] När jag klickar på knappen, ska en text "Click to change text" visas på skärmen.

### Testscenario [T4]
[T4.1] Navigera till webbsidan.
[T4.2] Kontrollera att knappen "Add note" finns och kan klickas



# -----------------------------------------------

### User story [U5] - kunna interagera med funktionen för knappen "add note"
Som användare vill jag kunna se att knappen 'Add note' kan klickas och addera texter, spara, byta ordning på och radera notes. 
Så att jag själv kan påbörja en note spara, ändra, byta ordning samt radera densamma.

### Acceptanskriterier [A5]
[A5.1] Det ska vara möjligt att klicka på rutan med texten "Click to change text" och ändra innehållet.
[A5.2] När man trycker "Enter", sparas texten.
[A5.3] När man trycker på korgen, suddas texten bort.
[A5.4] Genom att trycka på pilarna ska man kunna ändra ordning på sina notes.

### Testscenario [T5] – Kontrollera att knappen 'Add note', addera och delete note!
[T5.1] Navigera till webbsidan.
[T5.2] klicka på knappen "Add notes"
[T5.3] Klicka/markera textrutan "Click to change text" 
[T5.4] Interagera/markera input fältet och skriv texten "TEST T4.4"
[T5.5] klicka med "Enter" för att spara
[T5.6] Kontrollera att texten har ändrats till "Test T4.4"
[T5.7] Enligt samma scenario från (T4.2 - T4.6) och fyll i en ny ruta med texten "TEST T4.7" samt kontrollera att det gjorts.
[T5.8] Testa att ändra ordningen på de två texterna samt kontrollera att det gjorts
[T5.9] Testa att radera med "close button", samt kontrollera att det gjorts

