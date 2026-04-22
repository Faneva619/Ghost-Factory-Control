import os
from github import Github
import brain

# On utilise os.getenv pour lire la clé cachée dans les Secrets de GitHub
# SANS jamais l'écrire en texte clair ici !
token = os.getenv('MY_GITHUB_TOKEN')

g = Github(token)
user = g.get_user()

# On génère l'idée via le script brain.py
domaine, tache = brain.get_random_project()
repo_name = f"Project-{domaine}-{tache.replace(' ', '-')}"

try:
    # Création du dépôt sur ton compte
    repo = user.create_repo(repo_name, description=f"Projet automatique : {tache}", auto_init=True)
    
    # Création du fichier README
    readme_content = f"# {tache}\nDomaine : {domaine}\n\nGénéré par Ghost-Factory."
    repo.create_file("README.md", "Initial commit", readme_content)
    
    print(f"SUCCÈS : {repo_name} est en ligne !")
except Exception as e:
    print(f"ERREUR : {e}")
