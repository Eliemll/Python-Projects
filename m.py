from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/search?q=moodle+um&oq=moodle+um&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDU0MTVqMGoyqAIAsAIA&sourceid=chrome&ie=UTF-8")
    page.get_by_role("button", name="Tout refuser").click()
    page.get_by_role("link", name="Moodle UM: Accueil Universit").click()
    page.get_by_role("link", name="avec un compte UM").click()
    page.get_by_label("Identifiant :").click()
    page.get_by_label("Identifiant :").fill("elie.molle@etu.umontpellier.fr")
    page.get_by_label("Mot de passe :").click()
    page.get_by_label("Mot de passe :").fill("Solil30140*()")
    page.get_by_role("button", name="SE CONNECTER").click()
    page.get_by_role("link", name=" Tous mes cours").click()

     # Attendre que le bouton de fermeture de la page soit cliqué
    while not page.is_closed():
        # Si le bouton de fermeture est cliqué, arrêter le programme
        if page.query_selector('button[aria-label="Close"]'):
            break

            # Ajouter une courte pause pour éviter une consommation élevée du CPU
            page.wait_for_timeout(1000)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
