from playwright.sync_api import sync_playwright
import time

# Fonction pour extraire les données des lignes avec des notes
def extraire_donnees_lignes_notes(url):
    with sync_playwright() as p:
        browser = p.webkit.launch()
        context = browser.new_context()
        page = context.new_page()
        
        # Ouvrir la page de notes
        page.goto(url)
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

        # Attendre que la page charge 
        #time.sleep(2)
        
        # Initialiser une liste pour stocker les données des lignes avec des notes
        donnees_lignes_notes = []
        print("liste créée")

        # Trouver le tbody par son XPath
        html = page.query_selector('div.v-app mainui v-overlay-container valo-ul')
        print("Recherche du code html ")

        if html:
            print("Element HTML trouvé :", html)

        # Fermer le navigateur
        browser.close()
    
    return donnees_lignes_notes

# URL de la page de notes (remplacez par l'URL correcte)
url = "https://www.google.com/search?q=ent+um&oq=ent+um&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDM3MDdqMGoyqAIAsAIA&sourceid=chrome&ie=UTF-8"

# Appeler la fonction pour extraire les données des lignes avec des notes
donnees_lignes_notes = extraire_donnees_lignes_notes(url)

# Afficher les données extraites
print(donnees_lignes_notes)