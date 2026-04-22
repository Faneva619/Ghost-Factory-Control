import os
from github import Github
import brain


token = os.getenv('MY_GITHUB_TOKEN')

g = Github(token)
user = g.get_user()


domaine, tache = brain.get_random_project()
repo_name = f"Project-{domaine}-{tache.replace(' ', '-')}"

try:
    
    repo = user.create_repo(repo_name, description=f"Projet automatique : {tache}", auto_init=True)
    
    
    readme_content = f"# {tache}\nDomaine : {domaine}\n\nGénéré par Ghost-Factory."
    repo.create_file("README.md", "Initial commit", readme_content)
    
    print(f"SUCCÈS : {repo_name} est en ligne !")
except Exception as e:
    print(f"ERREUR : {e}")
