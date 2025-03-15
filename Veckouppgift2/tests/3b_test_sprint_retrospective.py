import re

from playwright.sync_api import Page, expect


def test_view_sprint_retrospective(page: Page):
    """
    User story:
       Som en användare, vill jag kunna se "Sprint retrospective",
       fokuserar på att granska och fastställa vad som gått bra i det arbete
       som utförts under sprinten. Identifiera problemområden som kan förbättras


       Acceptanskriterier:
       [A1.1] Det går att klicka på knappen "Last"
       [A1.2] Det går att klicka på knappen "Sprint retrospective"
       [A1.3] Kontrollera att ett <dialog> element visas på sidan,
       som innehåller en rubrik med texten "Sprint retrospective"

       Scenario:
       1. Klicka på knappen "Last"
       2. klicka på knappen "Sprint retrospective"
       3. kontrollera att man ser en rubrik med rubriken "Sprint retrospective"

        Genomförandelista:
        1. Gå till sidan https://lejonmanen.github.io/agile-helper/.
        2. Kontrollera att sidans titelrubrik är "Agile helper".
        3. Klicka på knappen "Last".
        4. Klicka på knappen vars text innehåller "Sprint retrospective"
        6. Kontrollera att ett <dialog> element visas på sidan,
        som innehåller en rubrik med texten "Sprint retrospective"

    """

    """test_view_sprint_retrospective"""

    page.goto("https://lejonmanen.github.io/agile-helper/")
    expect(page).to_have_title( re.compile("Agile helper" ))

    # 1. Klicka på knappen "Last"
    button_locator = page.get_by_role("button")
    last_button = button_locator.get_by_text("Last")
    last_button.click(timeout=100) #timeout 100 ms

    # 2. klicka button "Sprint retrospective"
    spring_button = page.get_by_role("button").get_by_text(re.compile("Sprint retrospective"))
    expect(spring_button).to_be_visible()
    spring_button.click(timeout=100)

    # 3. Kontrollera att rubriken "Sprint retrospective" nu syns på sidan som laddas.
    retrospective_heading = page.get_by_role("heading").get_by_text("Sprint retrospective")
    expect(retrospective_heading).to_be_visible()
