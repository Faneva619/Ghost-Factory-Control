import os
from github import Github
import brain


token = os.getenv('MY_GITHUB_TOKEN')

g = Github(token)
user = g.get_user()


domaine, tache = brain.get_random_project()
repo_name = f"Project-{domaine}-{tache.replace(' ', '-')}"

templates = {
    "Physique_L1": "print('Calcul de trajectoire...\\ng = 9.81\\nt = 1.0\\ny = 0.5 * g * t**2\\nprint(f\"Position: {y}m\")')",
    "IA_Data": "import numpy as np\nprint('Chargement du modèle neurone...\\nDone.')",
    "Reseaux": "import socket\nprint(f'Scan du réseau sur le port 80...')",
    "Informatique": "print('Système initialisé. Accès au Kernel KKK...')"
}


code_a_injecter = templates.get(domaine, "print('Hello World')")

try:
    
    repo = user.create_repo(repo_name, description=f"Projet automatique : {tache}", auto_init=True)
    
    
    readme_content = f"# {tache}\nDomaine : {domaine}\n\nGénéré par Ghost-Factory."
    repo.create_file("README.md", "Initial commit", readme_content)
    repo.create_file("main.py", "Ajout du script principal", code_a_injecter)
    
    print(f"SUCCÈS : {repo_name} est en ligne !")
except Exception as e:
    print(f"ERREUR : {e}")
