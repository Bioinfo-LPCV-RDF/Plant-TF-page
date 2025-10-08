import os
import re

# Chemin vers votre fichier HTML
html_file_path = "index-copy.html"

# Contenu minimal pour chaque fichier HTML
minimal_html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="../styles.css">
	<style>
				hr {
				border: 1px solid rgb(187, 187, 187);
				width:100%;
				margin: 20px auto; 
				margin-bottom: 40;
				}

				.img-structure{
					width: 90%;
					margin-bottom: 0px;
				}
	</style>
</head>
<body>
    <hr> 
    <h1>Page en construction</h1>
    <p>Cette page est en cours de création.</p>
    <br><br/>

</body>
</html>
"""

# Fonction pour extraire les liens des fichiers de description
def extract_description_links(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Regex pour trouver les liens des fichiers de description
    links = re.findall(r'data-description-file="([^"]+)"', content)
    return links

# Fonction pour générer les fichiers HTML
def generate_html_files(links):
    for link in links:
        # Créer les dossiers nécessaires
        os.makedirs(os.path.dirname(link), exist_ok=True)
        
        # Écrire le contenu minimal dans chaque fichier
        with open(link, "w", encoding="utf-8") as f:
            f.write(minimal_html_template)
    print(f"{len(links)} fichiers HTML générés avec succès.")

# Extraire les liens des fichiers de description
description_links = extract_description_links(html_file_path)

# Générer les fichiers HTML
generate_html_files(description_links)