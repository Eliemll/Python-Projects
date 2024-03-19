from playwright.sync_api import sync_playwright

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
        
        # Initialiser une liste pour stocker les données des lignes avec des notes
        donnees_lignes_notes = []
        print("liste créée")

        # Trouver la table par son XPath
        table = page.wait_for_selector('//*[@id="mdw-107968-overlays"]/div[3]/div/div/div[3]/div/div/div/div[3]/div/div[2]/div/div[2]/div[1]/table')
        # Vérifier si la table est trouvée
        if table:
            print("table trouvée")
            # Extraire toutes les lignes de la table de notes
            lignes_notes = table.query_selector_all('tr')
            print("tr trouvées")

            # Parcourir les lignes et extraire les données
            for ligne_tr in lignes_notes:
                print("début de la boucle")
                # Sélectionner le deuxième et le troisième <td> dans la ligne
                nom_matiere_td = ligne_tr.query_selector_all('td')[1]  # Deuxième <td> (index 1)
                note_td = ligne_tr.query_selector_all('td')[2]         # Troisième <td> (index 2)

                # Extraire le nom de la matière et les notes des <td>
                nom_matiere = nom_matiere_td.inner_text()
                note = note_td.inner_text()

                # Ajouter les données extraites à la liste
                donnees_lignes_notes.append({'nom_matiere': nom_matiere, 'note': note})

        # Fermer le navigateur
        browser.close()

    return donnees_lignes_notes

# URL de la page de notes (remplacez par l'URL correcte)
url = "https://www.google.com/search?q=ent+um&oq=ent+um&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDM3MDdqMGoyqAIAsAIA&sourceid=chrome&ie=UTF-8"

# Extraire les données des lignes avec des notes
donnees_lignes_notes = extraire_donnees_lignes_notes(url)

# Afficher les données extraites
print(donnees_lignes_notes)
