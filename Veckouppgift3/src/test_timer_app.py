import re

from playwright.sync_api import Page, expect

def test_verify_add_timer_button(page: Page):
    """
    Testscenario [T1]
    Kontrollera att knappen 'Add timer' är synlig och kan klickas
    """
    # T1.1 - Navigera till timer app sidan
    page.goto("https://lejonmanen.github.io/timer-vue/")

    # T1.2 - Kontrollera att knappen "Add timer" finns och kan klickas
    add_timer_button = page.locator('button:has-text("Add timer")')
    expect(add_timer_button).to_be_visible()
    add_timer_button.click()


def test_interaction_timer_button(page: Page):
    """
    Testscenario [T2]
    Kontrollera att knappen 'Add timer' är synlig och kan interageras med.
    """
    page.goto("https://lejonmanen.github.io/timer-vue/")
    add_timer_button = page.locator('button:has-text("Add timer")')
    add_timer_button.click()

###########################################################

def test_verify_add_note_button(page: Page):
    """
    Testscenario [T3]
    Kontrollera att knappen "Add note" är synlig och kan klickas
    """
    # T3.1 - Navigera till timer app sidan
    page.goto("https://lejonmanen.github.io/timer-vue/")

    # T3.2 Kontrollera att knappen "Add note" finns och är synlig och kan klickas
    add_note_button = page.locator('button:has-text("Add note")')
    expect(add_note_button).to_be_visible()
    add_note_button.click()


def test_interaction_add_note_button(page: Page):
    """
    Testscenario [T4]
    Kontrollera att knappen "Add note" är synlig och kan interageras med
    """
    # T4.1 - Navigera till timer app sidan
    page.goto("https://lejonmanen.github.io/timer-vue/")

    # T4.2 Klicka på knappen "Add note"
    #Playwright adds custom pseudo-classes like :visible, :has-text(), :has(), :is(), :nth-match() and more.
    add_note_button = page.locator('button:has-text("Add note")')
    expect(add_note_button).to_be_visible()
    add_note_button.click()

    # T4.3 Klicka/markera textrutan "Click to change text"
    note_text = page.locator('h3:has-text("Click to change text")').first
    expect(note_text).to_be_visible()
    note_text.click()

    #[T4.4] Interagera/markera input fältet och skriv texten "Test T4.4"
    edit_first_note_input = page.locator('input[placeholder="Description"]').first
    expect(edit_first_note_input).to_be_visible()
    edit_first_note_input.fill("Test T4.4")

    # [T4.5] Klicka med "Enter" för att spara och lämna textinmatningen
    page.keyboard.press("Enter")

    # [T4.6] Kontrollera att texten har ändrats till "TEST T4.4"
    edited_first_note_text = page.locator('h3:has-text("TEST T4.4")').first
    expect(edited_first_note_text).to_be_visible()

    # [T4.7] enligt samma scenario från T4.2 - T4.6 och fyll i en ny ruta med texten "TEST T4.7"
    add_note_button.click() # klicka fram ny textinmatningsruta
    second_note_text = page.locator('h3:has-text("Click to change text")').last
    expect(second_note_text).to_be_visible() # vi checkar att det är en oskriven ruta

    second_note_text.click() # öppna för textinmatning
    edit_second_note_input = page.locator('input[placeholder="Description"]').last
    edit_second_note_input.fill("TEST T4.7")
    page.keyboard.press("Enter")
    edited_second_note_text = page.locator('h3:has-text("TEST T4.7")').last
    expect(edited_second_note_text).to_be_visible()

    #[T4.8] Testa att ändra ordningen på de två texterna samt kontrollera att det gjorts
    up_arrow_button = page.locator('.icon.up').first
    up_arrow_button.click()
    expect(page.locator('h3:has-text("TEST T4.7")')).to_be_visible()
    expect(page.locator('h3:has-text("TEST T4.4")')).to_be_visible()

    #[T4.9] Testa att radera/stänga den första texten med "CLOSE" button (papperskorgsikonen) samt kontrollera att det gjorts
    delete_button = page.locator('.icon.close').first
    delete_button.click()
    expect(page.locator('h3:has-text("TEST T4.2")')).not_to_be_visible()
    expect(page.locator('h3:has-text("TEST T4.7")')).to_be_visible()
