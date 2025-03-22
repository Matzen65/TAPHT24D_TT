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

