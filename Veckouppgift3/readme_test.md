https://playwright.dev/docs/other-locators

### Test Timer-Vue

### User story [U1] - Verify "Add timer" button
Som användare vill jag kunna öppna och stänga ett fönster för widgeten timer
och ta bort (Erase) densamma.

### Acceptanskriterier [A1]
[A1.1] Navigera till timer-vue app sida, verifiera att knappen "Add timer" syns 
[A1.2] När jag klicka på icon "Add timer" ska timern dyka upp
[A1.3] När jag klickar på icon för Erase/papperskorg ska Timer widgeten släckas

### Testscenario [T1]
[T1.1] Navigera till webbsidan. Verifiera att endast en widget har öppnats
[T1.2] Kontrollera att knappen "Add timer" finns och kan klickas, verifiera att en ny widget öppnats
[T1.3] Verifiera funktionen av knappen Erase och verifiera att nu är endast en widget öppen.

# -----------------------------------------------

### User story [U2] - kunna interagera med timer
Som användare vill jag kunna se att timern startar från 15:00 
och att den kan starta samt pausa. 

### Acceptanskriterier [A2]
[A2.1] Timern ska starta från 15:00.
[A2.2] Testa att Start/paus kan klickas

### Testscenario [T2] – Timer-interaktioner
[T2.2] kontrollera att timern startar med texten 15:00
[T2.2] kontrollera om Start/Paus är synliga och klickbara

#------------------------------------------------

### User story [U3] - Ändra på tiden i timer-inställning, Verifiera/återställ till 15:00,
Som användare vill jag kunna ändra tiden i timern.
Så att jag kan starta en nedräkning med valfritt antal minuter i timer.

### Acceptanskriterier [A3]
[A3.1] Timern ska starta från 15:00.
[A3.2] Testa att Start/paus kan klickas

[T3.1] Ändra tiden i textfönstret från 15:00 till "5:00" samt verifiera texten 5:00. 
[T3.2] Reset till 5:00 samt avsluta med att stänga/erase widgeten

# -----------------------------------------------

### User story [U4] 
Som användare vill jag kunna se att knappen 'Add note' är synlig
och kan klickas. Så att man är redo att göra en note.

### Acceptanskriterier[A4]
[A4.1] När jag klickar på knappen, ska en text "Click to change text" visas på skärmen.

### Testscenario [T4]
[T4.1] Navigera till webbsidan. Kontrollera att knappen "Add note" finns och kan klickas

# -----------------------------------------------

### User story [U5] - kunna interagera med funktionen för knappen "add note"
Som användare vill jag kunna se att knappen 'Add note' kan klickas och addera texter, spara, byta ordning på och radera notes. 
Så att jag själv kan påbörja en note spara, ändra, byta ordning samt radera densamma.

### Acceptanskriterier [A5]
[A5.1] Det ska vara möjligt att finna och klicka på knappen Add note 
[A5.2] Det ska vara möjligt att se och klicka på texten "Click to change text"
[A5.3] Det ska gå att mata in text i fältet, klicka enter, samt se texten
[A5.4] Det ska gå att öppna ett nytt fält samt mata in text i fältet, klicka enter, samt se texten
[A5.5] ordningen på de två fälten ska kunna kastas om
[A5.6] När man trycker på erase/delete, försvinner den widgeten.

### Testscenario [T5] – Kontrollera att knappen 'Add note', addera och delete note!
[T5.1] Navigera till webbsidan. Klicka på knappen "Add notes" 
[T5.2] Klicka/markera textrutan "Click to change text" 
[T5.3] Interagera/markera input fältet och skriv texten "TEST T5.3", klicka med "Enter" för att spara Kontrollera att texten har ändrats till "Test T5.3"
[T5.4] Enligt samma scenario från (T5.2 - T5.4) och fyll i en ny ruta med texten "TEST T5.4" samt kontrollera att det gjorts.
[T5.5] Testa att ändra ordningen på de två texterna samt kontrollera att det gjorts
[T5.6] Testa att radera "TEST T5.3" med "close button", samt kontrollera att det gjorts

