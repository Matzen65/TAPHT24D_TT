from playwright.sync_api import Page, expect


import re


def test_verify_add_timer_remove_timer(page: Page):
    """
    Testscenario [T1]
    Kontrollera att knappen 'Add timer' är synlig och kan klickas och öppna timern,
    prova sedan att släcka timer-widgeten med close samt verifiera att den är stängd
    """

    # T1.1 - Navigera till timer app sidan, försäkra att inga andra aktiva widgets finns på sidan
    page.goto("https://lejonmanen.github.io/timer-vue/")
    timer_widget = page.locator('.widget')

    add_timer_button = page.locator('button:has-text("Add timer")')
    expect(add_timer_button).to_be_visible()
    expect(timer_widget).to_have_count(1, timeout=200) # endast en widget öppen

    # T1.2 - Kontrollera att knappen "Add timer" kan klickas och verifiera att en ny widget skapats
    add_timer_button.click() # här öppnas en ny widget (nr2)
    expect(timer_widget).to_have_count(2, timeout=200)  # widget nr 2 öppen och verifierat

    # T1.3 Klicka knappen Erase och verifiera att det därefter endast är en widget öppen.
    erase_button = timer_widget.locator('.icon.close') # stänger ner widget nr 2
    erase_button.click()
    expect(timer_widget).to_have_count(1, timeout=200) #verifierar att widget nr 2 har stängts


def test_interact_with_timer(page: Page):
    """
    kunna interagera med widgeten timer, start/paus och Reset
    """

    # T2.1 - kontrollera att widget för timer har starttid 15:00 samt verifiera start/paus/reset och erase.
    page.goto("https://lejonmanen.github.io/timer-vue/")
    timer_widget = page.locator('.widget')

    expect(timer_widget).to_have_count(1, timeout=200)
    add_timer_button = page.locator('button:has-text("Add timer")')
    expect(add_timer_button).to_be_visible()
    add_timer_button.click()  # här öppnas en ny widget (nr2)
    timer_time_first = timer_widget.locator('.row.time').get_by_text(re.compile("15:00", re.IGNORECASE))
    expect(timer_time_first).to_be_visible(timeout=200)

    #T2.2 - kontrollera om Start/Paus är synliga och klickbara
    start_button = page.locator('button:has-text("Start")')
    expect(start_button).to_be_visible()
    start_button.click()

    pause_button = page.locator('button:has-text("Pause")')
    expect(pause_button).to_be_visible()
    pause_button.click()


def test_change_time_for_timer(page: Page):
    """
    # T3 Ändra tiden i textfönstret från 15:00 till "5:00" samt verifiera 5:00.
    # kontrollera att "Reset" återställer till 15:00 samt avsluta med att stänga
    wwidgeten via iconen Close/papperskorgen samt verifiera stängt widgetfönster
    """
    # T3.1 - Ändra tiden i textfönstret från 15:00 till "5:00" samt verifiera 5:00
    page.goto("https://lejonmanen.github.io/timer-vue/")
    timer_widget = page.locator('.widget')

    add_timer_button = page.locator('button:has-text("Add timer")')
    add_timer_button.click()  # här öppnas en ny widget (nr2)
    timer_time = timer_widget.locator('.row.time').get_by_text(re.compile("5:00", re.IGNORECASE))
    expect(timer_time).to_be_visible(timeout=200)
    timer_widget.locator(".icon.settings").click(timeout=200) # öppna edit fönstret
    timer_input = timer_widget.get_by_role("textbox")
    timer_input.fill("5:00") # skriver in 5:00 sekunder
    timer_time = timer_widget.locator(".row.time").get_by_text(re.compile("5:00", re.IGNORECASE))
    expect(timer_time).to_be_visible(timeout=200)

    # T3.2 - sätt timern tillbaka till 15:00 samt stäng widgeten

    expect(timer_widget).to_have_count(2, timeout=200) # säkerställer att två widgets är öppna
    reset_button = page.locator('button:has-text("Reset")')
    expect(reset_button).to_be_visible()
    #OBS reset återställer enbart till förinställt startvärde, nu är det fortfarande ställt på "5:00"
    timer_time = timer_widget.locator(".row.time").get_by_text(re.compile("5:00", re.IGNORECASE))
    expect(timer_time).to_be_visible(timeout=200)
    reset_button.click(timeout=200)

    erase_button = timer_widget.locator('.icon.close')
    erase_button.click()
    expect(timer_widget).to_have_count(1, timeout=200)  # verifierar att widget nr 2 har stängts

###########################################################

def test_verify_add_note_button(page: Page):
    """
    Testscenario [T4]
    Kontrollera att knappen "Add note" är synlig och kan klickas
    """
    # T4.1 - Navigera till timer app sidan och klicka på knappen "Add note"
    page.goto("https://lejonmanen.github.io/timer-vue/")

    add_note_button = page.locator('button:has-text("Add note")')
    expect(add_note_button).to_be_visible()
    add_note_button.click()


def test_interaction_add_note_button(page: Page):
    """
    Testscenario [T5]
    Kontrollera att knappen "Add note" är synlig och kan interageras med
    """
    # T5.1 - Navigera till timer app sidan
    page.goto("https://lejonmanen.github.io/timer-vue/")
    #Playwright adds custom pseudo-classes like :visible, :has-text(), :has(), :is(), :nth-match() and more.
    add_note_button = page.locator('button:has-text("Add note")')
    expect(add_note_button).to_be_visible()
    add_note_button.click()

    # T5.2 Klicka/markera textrutan "Click to change text"
    note_text = page.locator('h3:has-text("Click to change text")').first
    expect(note_text).to_be_visible()
    note_text.click()

    #[T5.3] Interagera/markera input fältet och skriv texten "Test T5.3",
    # verifiera att texten har ändrats till "TEST T5.3"
    # Klicka med "Enter" för att spara och lämna textinmatningen
    edit_first_note_input = page.locator('input[placeholder="Description"]').first
    expect(edit_first_note_input).to_be_visible()
    edit_first_note_input.fill("Test T5.3")
    page.keyboard.press('Enter')
    edited_first_note_text = page.locator('h3:has-text("TEST T5.3")').first
    expect(edited_first_note_text).to_be_visible()

    # [T5.4] enligt samma scenario från T5.3 fyll i en ny ruta med texten "TEST T5.4"
    add_note_button.click() # klicka fram ny textinmatningsruta
    second_note_text = page.locator('h3:has-text("Click to change text")').last
    expect(second_note_text).to_be_visible() # vi checkar att det är en oskriven ruta
    second_note_text.click() # öppna för textinmatning
    edit_second_note_input = page.locator('input[placeholder="Description"]').last
    edit_second_note_input.fill("TEST T5.4")
    page.keyboard.press("Enter")
    edited_second_note_text = page.locator('h3:has-text("TEST T5.4")').last
    expect(edited_second_note_text).to_be_visible()

    #[T5.5] Testa att ändra ordningen på de två texterna samt kontrollera att det gjorts
    up_arrow_button = page.locator('.icon.up').first
    up_arrow_button.click()
    expect(page.locator('h3:has-text("TEST T5.4")')).to_be_visible()
    expect(page.locator('h3:has-text("TEST T5.3")')).to_be_visible()

    #[T5.6] Testa att radera/stänga den första texten genom att klicka ikonen för papperskorg och kontrollera att det gjorts
    delete_button = page.locator('.icon.close').first
    delete_button.click()
    expect(page.locator('h3:has-text("TEST T5.3")')).not_to_be_visible()
    expect(page.locator('h3:has-text("TEST T5.4")')).to_be_visible()
