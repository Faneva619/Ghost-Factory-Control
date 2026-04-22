import os
import time
from github import Github
import brain

# Sécurité
token = os.getenv('MY_GITHUB_TOKEN')
g = Github(token)
user = g.get_user()

print("🚀 Lancement de la production de 10 projets...")

for i in range(10):
    # On demande une nouvelle idée au cerveau pour chaque projet
    domaine, tache = brain.get_random_project()
    
    # Création d'un nom unique avec l'index i
    repo_name = f"Project-{i+1}-{domaine}-{tache.replace(' ', '-')}"
    
    try:
        # Création du dépôt
        repo = user.create_repo(repo_name, description=f"Projet automatique {i+1} : {tache}", auto_init=True)
        
        # Création du README
        repo.create_file("README.md", "Initial commit", f"# {tache}\n\nDomaine : {domaine}\n\n*Généré automatiquement par Ghost-Factory.*")
        
        # Création du script principal (on varie le contenu selon le domaine)
        content = f"print('Initialisation du projet {tache}...')"
        repo.create_file("main.py", "Script de base", content)
        
        print(f"✅ [{i+1}/10] {repo_name} est en ligne !")
        
        # On attend 2 secondes pour ne pas se faire bloquer par GitHub (Rate Limit)
        time.sleep(2)
        
    except Exception as e:
        print(f"!! Erreur sur le projet {i+1} : {e}")

print("🏁 Production terminée !")
