#!/usr/bin/env python3

from playwright.sync_api import Playwright, sync_playwright, expect
import time
import os

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/search?q=ent+um&oq=ent+um&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDM3MDdqMGoyqAIAsAIA&sourceid=chrome&ie=UTF-8")
    page.get_by_role("button", name="Tout refuser").click()
    page.get_by_role("link", name="Central Authentication Service: CAS Université de Montpellier https://ent.").click()
    page.get_by_label("Identifiant :").click()
    page.get_by_label("Identifiant :").fill("elie.molle@etu.umontpellier.fr")
    page.get_by_label("Mot de passe :").click()
    page.get_by_label("Mot de passe :").fill("Solil30140*()")
    page.get_by_role("button", name="󰈈 Toggle Password").click()
    page.get_by_label("Mot de passe :").click()
    page.get_by_label("Mot de passe :").fill("Solil30140*()")
    page.get_by_role("button", name="SE CONNECTER").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Mon Dossier Certificat de").click()
    page1 = page1_info.value
    page1.get_by_role("button", name=" Notes & résultats").click()
    page1.get_by_role("button", name="Licence 2 Peip STI").click()

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
