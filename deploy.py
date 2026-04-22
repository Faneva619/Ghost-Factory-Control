import os
from github import Github
import brain

# On récupère ton Token que tu as caché dans les Secrets
token = os.getenv('MY_GITHUB_TOKEN')
g = Github(token)
user = g.get_user()

# On génère une idée
domaine, tache = brain.get_random_project()
repo_name = f"Project-{domaine}-{tache.replace(' ', '-')}"

# Création du projet sur ton compte
try:
    repo = user.create_repo(repo_name, description=f"Projet automatique : {tache}", auto_init=True)
    repo.create_file("README.md", "Initial commit", f"# {tache}\nDomaine : {domaine}\n\nGénéré par Ghost-Factory.")
    print(f"SUCCÈS : {repo_name} est en ligne !")
except Exception as e:
    print(f"ERREUR : {e}")
