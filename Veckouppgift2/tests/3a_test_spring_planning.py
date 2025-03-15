import re

from playwright.sync_api import Page, expect


def test_view_sprint_planning(page: Page):
    """
    User story:
       Som en användare, vill jag kunna se "Sprint planning",
       som utspelar sig första dagen på en sprint, så att jag vet vad jag ska göra på mötet.

       Acceptanskriterier:
       [A1.1] Det går att klicka på knappen "First"
       [A1.2] Det går att klicka på knappen "Sprint Planning"
       [A1.3] Kontrollera att ett <dialog> element visas på sidan,
       som innehåller en rubrik med texten "Sprint planning"

       Scenario:
       1. Klicka på knappen "First"
       2. klicka på knappen "Sprint planning"
       3. kontrollera att man ser en rubrik med rubriken "Sprint planning"

        Genomförandelista:
        1. Gå till sidan https://lejonmanen.github.io/agile-helper/.
        2. Kontrollera att sidans titelrubrik är "Agile helper".
        3. Klicka på knappen "First".
        4. Klicka på knappen vars text innehåller "Sprint planning"
        6. Kontrollera att ett <dialog> element visas på sidan,
        som innehåller en rubrik med texten "Sprint planning"

    """

    """test_view_sprint_planning"""

    page.goto("https://lejonmanen.github.io/agile-helper/")
    expect(page).to_have_title( re.compile("Agile helper" ))

    # 1. Klicka på knappen "First"
    button_locator = page.get_by_role("button")
    first_button = button_locator.get_by_text("First")
    first_button.click(timeout=100) #timeout 100 ms

    # 2. klicka button "Sprint planning"
    spring_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning"))
    expect(spring_button).to_be_visible()
    spring_button.click(timeout=100)

    # 3. Kontrollera att rubriken "Sprint planning" nu syns på sidan som laddas.
    spring_planning_heading = page.get_by_role("heading").get_by_text("Sprint planning")
    expect(spring_planning_heading).to_be_visible()

